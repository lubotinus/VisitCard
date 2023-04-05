from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime
from forms import TestForm
from models import tests

app = Flask(__name__)
app.config["SECRET_KEY"] = "laba"

@app.route("/tests/", methods=["GET", "POST"])
def tests_list():
    form = TestForm()
    error = ""
    
    if request.method == "POST":
        if form.validate_on_submit():
            tests.create(form.data)
            tests.save_all()
            
        return redirect(url_for("tests_list"))

    return render_template("test.html", form=form, tests=tests.all(), error=error)


@app.route("/tests/<int:test_id>/", methods=["GET", "POST"])
def test_details(test_id):
    test = tests.get(test_id-1)
    form = TestForm(data=test)

    if request.method == "POST":
        if form.validate_on_submit():
            tests.update(test_id-1, form.data)
        return redirect(url_for("tests_list"))
    return render_template("test_id.html", form=form, test_id=test_id)


if __name__ == "__main__":
    app.run(debug=True)