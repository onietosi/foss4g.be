import animate from "tailwindcss-animate"

/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: ["class"],
    safelist: ["dark"],
    prefix: "",

    theme: {
        container: {
            center: true,
            padding: "2rem",
            screens: {
                "2xl": "1400px",
            },
        },
        extend: {
            colors: {
                map: '#e2c6a0',
                'map-dark': '#c6a77f',
                primary: '#7a5c3e',
                'primary-dark': '#5a3f27',
                accent: '#d0b67b',
                'accent-dark': '#b89c5f',
                secondary: '#5CAB23', // FOSS4G green
                'secondary-dark': '#297D29',
                'text-main': '#3b2e20',
                'text-muted': '#7e6b53',
                'btn-base': '#a7794e',
                'btn-hover': '#925f39',
                'border-default': '#bfa078',
                /** grey */
                neutral: '#7C7C7C',        // BELGIUM grey
                /** yellow/red highlights */
                warning: '#F2C100',        // n’est yellow
                danger: '#B72A2A',         // conférence red
                bronze: '#CD7F32',
                silver: '#C0C0C0',
                gold: '#FFD700',

                deepMapBlue: "#01295A",

                /** off-white background */
                'off-white': '#F9FBF9',
            },
            fontFamily: {
                sans: ['Space Grotesk', 'Noto Sans', 'sans-serif'],
            },
            backgroundImage: {
                logo: "url('/images/logo.svg')",
                typology: "url('/images/background-topology.png')",
            },
            borderRadius: {
                lg: "var(--radius)",
                md: "calc(var(--radius) - 2px)",
                sm: "calc(var(--radius) - 4px)",
            },
            keyframes: {
                "accordion-down": {
                    from: {height: '0'},
                    to: {height: "var(--radix-accordion-content-height)"},
                },
                "accordion-up": {
                    from: {height: "var(--radix-accordion-content-height)"},
                    to: {height: '0'},
                },
            },
            animation: {
                "accordion-down": "accordion-down 0.2s ease-out",
                "accordion-up": "accordion-up 0.2s ease-out",
            },
        },
    },
    plugins: [animate],
}
