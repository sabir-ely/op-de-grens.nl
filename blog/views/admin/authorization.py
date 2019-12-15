from functools import wraps
from flask import redirect, url_for, session, request, abort, g
from flask_oauthlib.client import OAuth
from blog import app

oauth = OAuth(app)

GOOGLE_ID     = app.config.get("GOOGLE_ID")
GOOGLE_SECRET = app.config.get("GOOGLE_SECRET")
ADMIN_EMAILS   = app.config.get("ADMIN_EMAILS")

#Configure OAuth
google = oauth.remote_app(
    'google',
    consumer_key         = GOOGLE_ID,
    consumer_secret      = GOOGLE_SECRET,
    base_url             = 'https://www.googleapis.com/oauth2/v1/',
    request_token_url    = None,
    access_token_method  = 'POST',
    access_token_url     = 'https://accounts.google.com/o/oauth2/token',
    authorize_url        = 'https://accounts.google.com/o/oauth2/auth',
    request_token_params = {
            'scope': 'email'
    },
)


def login_required(func):
    """Decorator that checks if client is logged in"""

    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for('admin_main'))
        return func(*args, **kwargs)
    return decorated_function


@app.route('/admin/login/authorized')
def oauth_callback():
    """Handles OAuth response, checks if client's email address matches the admin's email,
       if so, sets session values accordingly
    """

    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )

    g.google_token = (resp['access_token'], '')
    user_email = google.get('userinfo').data["email"]
    if user_email not in ADMIN_EMAILS:
        return abort(403)

    session["logged_in"] = True
    return redirect(url_for("admin_main"))

@app.route('/admin/logout/')
@login_required
def logout():
    """Logs out admin and redirects to public home page"""

    session.pop('logged_in', None)
    return redirect(url_for("home"))

@google.tokengetter
def get_google_oauth_token():
    return g.google_token

def authorize():
    """Starts OAuth procedure using the given OAuth configuration"""
    return google.authorize(
        callback="https://op-de-grens.nl/admin/login/authorized")

