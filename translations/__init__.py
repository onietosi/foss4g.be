def get_translations(language='en', page=None):
    if language == 'fr':
        from .fr import translations_site, translations_page
    elif language == 'nl':
        from .nl import translations_site, translations_page
    else:
        from .en import translations_site, translations_page

    if page in translations_page:
        # if we have a page-specific translation, merge it with the global one
        return translations_page[page], translations_site

    # if we don't have a page-specific translation, return the global one
    return {}, translations_site


def get_translated_page_names(pages, language='en'):
    pages_with_name = []

    for page in pages:
        translations_page, _ = get_translations(language, page=page)

        pages_with_name.append(
            {'page_id': page, 'name': translations_page.get('name', page)}
        )

    return pages_with_name