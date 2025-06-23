import en from './locales/en.json'
import fr from './locales/fr.json'
import nl from './locales/nl.json'

import { defineI18nConfig } from '#imports'

export default defineI18nConfig(() => ({
    legacy: false,
    locales: [
        {
            code: "fr",
            iso: "fr-BE",
            file: "fr-FR.js",
            name: "Français",
        },
        {
            code: "en",
            iso: "en-US",
            file: "en-US.js",
            name: "English",
        },
        {
            code: "nl",
            iso: "nl-BE",
            file: "nl-NL.js",
            name: "Nederlands",
        },
    ],
    messages: {
        en,
        fr,
        nl
    }
}));
