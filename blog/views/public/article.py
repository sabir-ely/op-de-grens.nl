from flask import render_template, session, abort
from blog import app
from blog.models import Article




@app.route("/<int:id>/")
@app.route("/<int:id>/<slug>/")
def article(id, slug=None):

    article = Article.get_by_id(id)

    if not article:
        return abort(404)

    if not article.public and not session.get("logged_in"):
        return abort(404)

    article.date_created = Article.convert_date(
            date_created=article.date_created,
            pretty=True
    )

    return render_template("public/article.html", article=article)
