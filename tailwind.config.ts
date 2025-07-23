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
                'off-white': '#DCDED6',
                'stone-light': '#CED0C3',
                'stone': '#B4BAB1',
                'teal-light': '#859393',
                'teal-dark': '#5D726F',

                'white': '#dbdbd9fe',

                'main-color-1': '#459939',
                'main-color-2': '#998d39',
                'main-color-3': '#8d3999',
                'main-color-4': '#394599',

                primary: {
                    DEFAULT: '#859393',     // teal-light
                    dark: '#5D726F',        // teal-dark
                },
                neutral: {
                    DEFAULT: '#B4BAB1',     // stone
                    dark: '#5D726F',        // for text contrast
                },
                accent: {
                    DEFAULT: '#CED0C3',     // optional accent
                    dark: '#859393',
                },
                /** yellow/red highlights */
                warning: '#F2C100',        // yellow logo
                danger: '#B72A2A',         // red logo
                bronze: '#CD7F32',
                silver: '#C0C0C0',
                gold: '#FFD700',

                deepMapBlue: "#01295A",
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
