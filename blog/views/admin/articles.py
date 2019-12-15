from datetime import datetime
from flask import render_template, request, flash, redirect, url_for, abort, jsonify
from blog import app
from blog.models import Article
from .authorization import login_required


@app.route("/admin/articles/all")
@login_required
def get_all_articles():
    articles = Article.get_all()
    for article in articles:
        article.date_created = Article.convert_date(article.date_created)

    return jsonify([
        render_template(
            "admin/article_row.html",
            article=article
        ) for article in articles
    ])

@app.route("/admin/article/new", methods=["GET", "POST"])
@login_required
def add_article():
    if request.method == "POST":

        article, errors = validate_article(request.form, new=True)
        if errors != {}:
            return render_template(
                "admin/edit_article.html",
                errors=errors,
                article=article,
                new=True
            )

        article.date_created = datetime.now()
        article.store()

        flash("Artikel gepubliceerd")
        return redirect(url_for("admin_main"))

    return render_template("admin/edit_article.html", new=True)


@app.route("/admin/article/edit/<int:id>/", methods=["GET", "POST"])
@login_required
def edit_article(id):

    current_article = Article.get_by_id(id)
    if not current_article:
        return abort(404)

    if request.method == "POST":
        new_article, errors = validate_article(request.form)
        if errors != {}:
            return render_template(
                "admin/edit_article.html",
                errors=errors,
                article=new_article
            )

        new_article.id = current_article.id
        new_article.date_created = current_article.date_created
        new_article.store()
        flash("Artikel bijgewerkt")
        return redirect(url_for("admin_main"))

    return render_template("admin/edit_article.html", article=current_article)

@app.route("/admin/article/delete/<int:id>/", methods=["GET", "POST"])
@login_required
def delete_article(id):

    article = Article.get_by_id(id)
    if not article:
        return abort(404)

    if request.method == "POST":

        article.delete()
        flash("Artikel verwijderd")
        return redirect(url_for("admin_main"))

    return render_template("admin/delete_article.html", article=article)




def validate_article(form, new=False):

    errors = dict()
    data = {
        "title"   : form.get("article_title"),
        "content" : form.get("article_content"),
        "public"  : form.get("article_public") != None
    }

    if data["title"] == None or data["title"] == "":
        errors["title"] = "Titel ontbreekt"

    if new:
        if Article.title_exists(data["title"]):
            errors["title"] = "Artikel met deze titel bestaat al"

    elif len(data["title"]) > 100:
        errors["title"] = "Titel kan niet langer zijn dan 100 tekens"

    if data["content"] == None or data["content"] == "":
        errors["content"] = "Tekst ontbreekt"

    article = Article(
        title=data["title"],
        content=data["content"],
        date_created=None,
        public=data["public"]
    )

    return article, errors
