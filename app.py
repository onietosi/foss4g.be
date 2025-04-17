from flask import Flask, render_template

from translations import get_translations

# UTILISER FLASK STATIC

# ATTENTION UTILISERL ES LANGUE (choix FR/NL/EN) DANS L'URL

LANGUAGES = {
    'en': 'English',
    'fr': 'Français',
    'nl': 'Nederlands'
}


app = Flask(__name__,
    static_folder='static',
    static_url_path='/static'
)


@app.route('/')
@app.route('/<lang>')
def home(lang='en'):
    # Get translations for the requested language, default to English
    translations_page, translations_site = get_translations(lang, page='home')

    print(translations_page)
    print(translations_site)

    return render_template(
        'home.html',
        page=translations_page,
        site=translations_site,
        lang=lang,
        languages=LANGUAGES.keys()
    )


@app.route('/contact')
@app.route('/<lang>/contact')
def contact(lang='en'):
    translations_page, translations_site = get_translations(lang, page='home')

    return render_template(
        'contact.html',
        page=translations_page,
        site=translations_site,
        lang=lang,
        languages=LANGUAGES.keys()
    )

@app.route('/sponsors')
@app.route('/<lang>/sponsors')
def sponsors(lang='en'):
    translations_page, translations_site = get_translations(lang, page='home')

    return render_template(
        'sponsors.html',
        page=translations_page,
        site=translations_site,
        lang=lang,
        languages=LANGUAGES.keys()
    )


@app.route('/volunteers')
@app.route('/<lang>/volunteers')
def volunteers(lang='en'):
    translations_page, translations_site = get_translations(lang, page='home')

    return render_template(
        'volunteers.html',
        page=translations_page,
        site=translations_site,
        lang=lang,
        languages=LANGUAGES.keys()
    )

if __name__ == '__main__':
    app.run(debug=True)