from flask import render_template, request, flash, redirect, url_for
from blog import app
from blog.models import Description
from .authorization import login_required


@app.route("/admin/description/edit/", methods=["GET", "POST"])
@login_required
def edit_description():
    """Edit description showed on public home page"""

    if request.method == "POST":
        Description.set_text(text=request.form["description_text"])
        flash("Omschrijving aangepast")
        return redirect(url_for("admin_main"))

    description = Description.get_text()

    return render_template(
        "admin/edit_description.html",
        description=description
    )
