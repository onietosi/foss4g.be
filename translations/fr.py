from .var import year, day

month = "Septembre"
belgium = "Belgique"
foss4g_be = f"FOSS4G {belgium.capitalize()}"

translations_site = {
    "year": f"{year}",
    "date": f"{day} {month} {year}",
    "title": f"{foss4g_be} - {year}",
    "foss4g_be": f"{foss4g_be}",
    "description": "FOSS4G Belgique est une communauté d'enthousiastes du Logiciel Libre et Open Source pour la Géomatique en Belgique.",
    "keywords": "FOSS4G Geo marqueur GIS Open Source",
    "copyright": f"© {year} FOSS4G Belgique. Tous droits réservés.",
    "not_a_conf": "Ceci n'est pas une conférence",
    "only_possible": f"{foss4g_be} is only possible thanks to the support of",
    "partners_and_sponsors": f"our partners and sponsors",
}

translations_page = {
    "home": {
        "name": "Accueil",
    },
    "sponsors": {
        "title": "Nos sponsors",
        "name": "Sponsors",
        "looking_for_sponsors": "Nous sommes à la recherche de sponsors pour financer ce super événement qu'est le FOSS4G Belgique. Si vous êtes intéressé, veuillez nous contacter.",
    },
    "volunteers": {
        "title": "A la recherche de bénévoles",
        "name": "Bénévoles",
        "looking_for_volunteers": "Nous recherchons des bénévoles pour nous aider à organiser le FOSS4G Belgique. Si vous êtes intéressé, veuillez nous contacter.",
    },
    "previous_editions": {
        "title": "Nos précédentes éditions",
        "name": "Éditions Précédentes",
        "content": "FOSS4G-be est organisé depuis de nombreuses années. Voici la liste des précédentes éditions : ",
    },
    "previous_sponsors": {
        "title": "Merci !",
        "name": "Sponsors Précédents",
        "content": "Merci à nos sponsors précédents sans qui l'aventure n'auait pas été possible.",
    },
    "about_us": {
        "name": "À propos de nous",
        "title": "Qui sommes nous ?",
        "content": """<p>Nous sommes le chapitre belge de la Open Source Geospatial Foundation (OSGeo).</p>
<p>OSGeo est une organisation à but non lucratif dont la mission est de soutenir le développement de logiciels géospatiaux open source et de promouvoir leur utilisation. La fondation fournit un soutien financier, organisationnel et juridique à la communauté géospatiale open source au sens large. Elle sert également d'entité juridique indépendante à laquelle les membres de la communauté peuvent contribuer par du code, des financements et d'autres ressources, en étant assurés que leurs contributions seront préservées pour le bénéfice public. OSGeo agit également en tant qu'organisation de sensibilisation et de plaidoyer pour la communauté géospatiale open source et offre un forum commun ainsi qu'une infrastructure partagée pour améliorer la collaboration entre projets.</p>
<p>Les projets de la fondation sont tous librement disponibles et utilisables sous une licence open source certifiée par l'OSI.</p>
""",
    },
    "contact": {
        "name": "Contact",
        "title": "Contactez-nous",
        "content": "Pour toute demande, vous pouvez envoyer un courriel à info at foss4g.be.",
    },
}
