from flask import Flask, render_template

from translations import get_translations

LANGUAGES = {"en": "English", "fr": "Français", "nl": "Nederlands"}

PAGES = ["home", "contact", "sponsors", "volunteers"]

app = Flask(__name__, static_folder="static", static_url_path="/static")

# Page for choosing the language
@app.route("/")
def index():
    return render_template("choose_your_language.html")


# Generic route for all pages and all the languages
@app.route("/<lang>/<page>.html")
def generic_page(lang, page):
    translations_page, translations_site = get_translations(lang, page=page)

    return render_template(
        f"{page}.html",
        page=translations_page,
        site=translations_site,
        lang=lang,
        languages=LANGUAGES.keys(),
    )


if __name__ == "__main__":
    app.run(debug=True)
