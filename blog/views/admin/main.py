from flask import redirect, abort, url_for, session, render_template, request, jsonify
from blog import app
from blog.models import Article, Description
from .authorization import authorize, login_required


@app.route('/admin/')
def admin_main():
    """Loads main page for the admin interface"""

    if app.config.get("DEBUG"):
        session["logged_in"] = True


    if not session.get("logged_in"):
        return authorize()

    description = Description.get_text()
    return render_template("admin/main.html", description=description)
