from .var import year, day

month = 'Septembre'
belgium = 'Belgique'
foss4g_be = f'FOSS4G {belgium.capitalize()}'

translations_site = {
    'year': f'{year}',
    'date': f'{day} {month} {year}',
    'title': f'{foss4g_be} - {year}',
    'foss4g_be': f'{foss4g_be}',
    'description': 'FOSS4G Belgique est une communauté d\'enthousiastes du Logiciel Libre et Open Source pour la Géomatique en Belgique.',
    'keywords': 'FOSS4G Geo marqueur GIS Open Source',
    'copyright': f'© {year} FOSS4G Belgique. Tous droits réservés.',
    'not_a_conf': 'Ceci n\'est pas une conférence',
    'only_possible': f'{foss4g_be} is only possible thanks to the support of',
    'partners_and_sponsors': f'our partners and sponsors',
}

translations_page = {
    'home': {
        'name': 'Accueil',
        'banner': {
            'title': 'Bienvenue à FOSS4G Belgique',
            'subtitle': 'Rejoignez notre communauté de Logiciels Libres et Open Source pour la Géomatique'
        },
        'cta': {
            'title': 'Rejoignez Notre Communauté',
            'description': 'Connectez-vous avec d\'autres passionnés de FOSS4G en Belgique et restez informés des dernières nouvelles et événements.',
            'button': 'Rejoindre'
        }
    },
    'sponsors': {
        'name': 'Sponsors',
    },
    'volonteers': {
        'name': 'Bénévoles',
    },
    'about': {
        'title': 'À propos de FOSS4G Belgique',
        'description': 'En savoir plus sur notre communauté et notre mission.',
        'mission': {
            'title': 'Notre Mission',
            'content': 'FOSS4G Belgique vise à promouvoir l\'utilisation des Logiciels Libres et Open Source pour les applications géospatiales en Belgique. Nous organisons des événements, des ateliers et fournissons des ressources pour les débutants et les experts.'
        },
        'team': {
            'title': 'Notre Équipe',
            'content': 'Notre équipe est composée de bénévoles passionnés dédiés à la promotion de FOSS4G en Belgique.'
        }
    },
    'contact': {
        'title': 'Contactez-nous',
        'description': 'Prenez contact avec la communauté FOSS4G Belgique.',
        'form': {
            'name': 'Nom',
            'email': 'Email',
            'message': 'Message',
            'submit': 'Envoyer le Message'
        },
        'success': 'Merci pour votre message ! Nous vous répondrons bientôt.',
        'error': 'Une erreur s\'est produite lors de l\'envoi de votre message. Veuillez réessayer plus tard.'
    },
    'footer': {
        'links': {
            'home': 'Accueil',
            'about': 'À propos',
            'events': 'Événements',
            'contact': 'Contact'
        }
    }
} 