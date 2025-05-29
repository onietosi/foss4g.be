# Freeze the pages for github pages
from flask_frozen import Freezer
from app import app, LANGUAGES, PAGES

# Set the base URL for the frozen site
app.config["FREEZER_BASE_URL"] = "https://www.foss4g.be/"

freezer = Freezer(app)


@freezer.register_generator
def generic_page():
    for lang in LANGUAGES:
        for page in PAGES:
            yield {"lang": lang, "page": page, "_file": f"{lang}/{page}.html"}


if __name__ == "__main__":
    freezer.freeze()
