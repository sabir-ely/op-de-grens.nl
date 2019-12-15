from flask import render_template
from blog import app
from blog.models import Description, Article

PREVIEW_LENGTH = 50


@app.route("/")
def home():

    description = Description.get_text()
    articles = get_articles(3)

    return render_template(
        "public/index.html",
        description=description,
        articles=articles
    )

@app.route("/browse/")
def browse():

    articles = get_articles()
    return render_template("public/browse.html", articles=articles)



#7d5782
def add_preview(article, length):
    """
    Cuts down article's content to the first few word in order to
    create preview text
    """

    word_list = [word for word in article.content.split() if "]" not in word and "[" not in word]
    word_list = [word.replace("*", "").replace("_", "") for word in word_list]

    article.preview_text = " ".join(word_list[:length]) + "..."
    article.date_created = Article.convert_date(
            date_created=article.date_created,
            pretty=True
        )

    return article

def get_articles(amount=None):
    articles = [article for article in Article.get_all() if article.public]
    articles = [add_preview(article, PREVIEW_LENGTH) for article in articles]

    if amount != None:
        articles = articles[0:amount]

    return articles
