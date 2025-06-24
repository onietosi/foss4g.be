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
                /** greens */
                primary: '#5CAB23',        // FOSS green
                'primary-dark': '#297D29', // “4G” dark green
                /** grey */
                neutral: '#7C7C7C',        // BELGIUM grey
                /** lime accent */
                accent: '#6DBE47',         // 2025 lime
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
