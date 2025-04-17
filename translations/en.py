from .var import year, day

month = 'Septembre'
belgium = 'Belgium'
foss4g_be = f'FOSS4G {belgium.capitalize()}'

translations_site = {
    'year': f'{year}',
    'date': f'{day} {month} {year}',
    'title': f'{foss4g_be} - {year}',
    'foss4g_be': f'{foss4g_be}',
    'description': 'FOSS4G Belgium is a community of Free and Open Source Software for Geospatial enthusiasts in Belgium.',
    'keywords': 'FOSS4G Geo marker GIS Open Source',
    'copyright': f'© {year} FOSS4G Belgique. Tous droits réservés.',
    'not_a_conf': 'This is not a conference',
    'only_possible': f'{foss4g_be} is only possible thanks to the support of',
    'partners_and_sponsors': f'our partners and sponsors',
}

translations_page = {
    'home': {
        'name': 'Home',
        'banner': {
            'title': 'Welcome to FOSS4G Belgium',
            'subtitle': 'Join our community of Free and Open Source Software for Geospatial enthusiasts'
        },
        'cta': {
            'title': 'Join Our Community',
            'description': 'Connect with other FOSS4G enthusiasts in Belgium and stay updated with the latest news and events.',
            'button': 'Join Now'
        }
    },
    'sponsors': {
        'name': 'Sponsors',
    },
    'volonteers': {
        'name': 'Bénévoles',
    },
    'about': {
        'title': 'About FOSS4G Belgium',
        'description': 'Learn more about our community and mission.',
        'mission': {
            'title': 'Our Mission',
            'content': 'FOSS4G Belgium aims to promote the use of Free and Open Source Software for Geospatial applications in Belgium. We organize events, workshops, and provide resources for both beginners and experts.'
        },
        'team': {
            'title': 'Our Team',
            'content': 'Our team consists of passionate volunteers dedicated to promoting FOSS4G in Belgium.'
        }
    },
    'contact': {
        'title': 'Contact Us',
        'description': 'Get in touch with the FOSS4G Belgium community.',
        'form': {
            'name': 'Name',
            'email': 'Email',
            'message': 'Message',
            'submit': 'Send Message'
        },
        'success': 'Thank you for your message! We will get back to you soon.',
        'error': 'There was an error sending your message. Please try again later.'
    },
    'footer': {
        'copyright': '© 2024 FOSS4G Belgium. All rights reserved.',
        'links': {
            'home': 'Home',
            'about': 'About',
            'events': 'Events',
            'contact': 'Contact'
        }
    }
} 