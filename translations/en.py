from .var import year, day

month = "September"
belgium = "Belgium"
foss4g_be = f"FOSS4G {belgium.capitalize()}"

translations_site = {
    "year": f"{year}",
    "date": f"{day} {month} {year}",
    "title": f"{foss4g_be} - {year}",
    "foss4g_be": f"{foss4g_be}",
    "description": "FOSS4G Belgium is a community of Free and Open Source Software for Geospatial enthusiasts in Belgium.",
    "keywords": "FOSS4G Geo marker GIS Open Source",
    "copyright": f"© {year} FOSS4G Belgique. All rights reserved.",
    "not_a_conf": "This is not a conference",
    "only_possible": f"{foss4g_be} is only possible thanks to the support of",
    "partners_and_sponsors": f"our partners and sponsors",
    "bronze": "bronze",
    "silver": "silver",
    "gold": "gold",
}

translations_page = {
    "home": {
        "name": "Home",
    },
    "about_us": {
        "name": "About Us",
        "title": "Who are we?",
        "content": """<p>We are the Belgian chapter of the Open Source Geospatial Foundation (OSGeo).</p>
<p>OSGeo is a non-profit organization dedicated to supporting the development of open source geospatial software and promoting their use. The foundation provides financial, organizational, and legal support to the open source geospatial community at large. It also serves as an independent legal entity to which members of the community can contribute code, funding, and other resources, with the assurance that their contributions will be preserved for the public good. OSGeo also acts as an outreach and advocacy organization for the open source geospatial community and provides a common forum and shared infrastructure to improve collaboration between projects.</p>
<p>The foundation's projects are all freely available and usable under an open source license certified by the OSI.</p>
""",
    },
    "call_for_presentations": {
        "name": "Call for Presentations",
        "title": "Call for Presentations",
        "content": """TODO""",
    },
    "sponsors": {
        "title": "Our Sponsors",
        "name": "Sponsors",
        "looking_for_sponsors": "We are looking for sponsors to fund this amazing event known as FOSS4G Belgium. If you are interested, please get in touch with us.",
        "level": "level",
        "price": "price",
        "stand": "presentation stand",
        "page_in_pgm": "page in the program booklet",
        "main_page_logo": "logo on the main page of the website",
        "sponsor_page_logo": "logo on the sponsors page of the website",
        "participant_list": "participant list",
        "page": "page",
        "level_and_advantages_title": "Levels and Advantages",
        "level_and_advantages_desc": """
<p><b>Presentation Stand</b>: A spot with a table, two chairs, and a power outlet.</p>
<p><b>Page in the Program Booklet</b>: Our sponsors must provide us with their logo, image, and text by August 25, 2025.</p>
""",
    },
    "volunteers": {
        "title": "Looking for Volunteers",
        "name": "Volunteers",
        "looking_for_volunteers": "We are looking for volunteers to help us with the organization of FOSS4G Belgium. If you are interested, please get in touch with us.",
    },
    "previous_editions": {
        "title": "Our Previous Editions",
        "name": "Previous Editions",
        "content": "FOSS4G-be has been organized for many years. Here is the list of previous editions: ",
    },
    "previous_sponsors": {
        "title": "Thank You!",
        "name": "Previous Sponsors",
        "content": "Thanks to our previous sponsors without whom this adventure would not have been possible.",
    },
    "contact": {
        "name": "Contact Us",
        "title": "Contact Us",
        "content": "For any inquiries you can send an email to info at foss4g.be",
    },
}
