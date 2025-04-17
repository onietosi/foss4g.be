from .var import year, day

month = 'September'
belgium = 'België'
foss4g_be = f'FOSS4G {belgium.capitalize()}'

translations_site = {
    'year': f'{year}',
    'date': f'{day} {month} {year}',
    'title': f'{foss4g_be} - {year}',
    'foss4g_be': f'{foss4g_be}',
    'description': 'FOSS4G België is een gemeenschap van Free and Open Source Software voor Geospatial enthousiastelingen in België.',
    'keywords': 'Foss4G Geo GIS Open Source OSGeo OSGeoBE België Nederland',
    'copyright': '© {year} FOSS4G België. Alle rechten voorbehouden.',
    'not_a_conf': 'This is not a conference',
    'only_possible': f'{foss4g_be} is only possible thanks to the support of',
    'partners_and_sponsors': f'our partners and sponsors',
    'more_info': 'If you want more information',
    'contact_us': 'contact us',
}


translations_page = {
    'home': {
        'name': 'Welkom',
        'banner': {
            'title': 'Welkom bij FOSS4G België',
            'subtitle': 'Sluit je aan bij onze gemeenschap van Free and Open Source Software voor Geospatial'
        },
        'cta': {
            'title': 'Word Lid van Onze Gemeenschap',
            'description': 'Maak contact met andere FOSS4G enthousiastelingen in België en blijf op de hoogte van het laatste nieuws en evenementen.',
            'button': 'Word Lid'
        }
    },
    'sponsors': {
        'name': 'Sponsors',
    },
    'volonteers': {
        'name': 'Bénévoles',
    },
    'about': {
        'title': 'Over FOSS4G België',
        'description': 'Lees meer over onze gemeenschap en missie.',
        'mission': {
            'title': 'Onze Missie',
            'content': 'FOSS4G België streeft ernaar het gebruik van Free and Open Source Software voor Geospatial toepassingen in België te bevorderen. We organiseren evenementen, workshops en bieden hulpmiddelen voor zowel beginners als experts.'
        },
        'team': {
            'title': 'Ons Team',
            'content': 'Ons team bestaat uit gepassioneerde vrijwilligers die zich inzetten voor de promotie van FOSS4G in België.'
        }
    },
    'contact': {
        'title': 'Neem Contact Op',
        'description': 'Neem contact op met de FOSS4G België gemeenschap.',
        'form': {
            'name': 'Naam',
            'email': 'E-mail',
            'message': 'Bericht',
            'submit': 'Verstuur Bericht'
        },
        'success': 'Bedankt voor je bericht! We nemen zo spoedig mogelijk contact met je op.',
        'error': 'Er is een fout opgetreden bij het versturen van je bericht. Probeer het later opnieuw.'
    },
    'footer': {
        'links': {
            'home': 'Home',
            'about': 'Over',
            'events': 'Evenementen',
            'contact': 'Contact'
        }
    }
}
