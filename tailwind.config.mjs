/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      fontFamily: {
        "geist-sans": ["Geist Sans", "sans-serif"],
        "fira-code": ["Fira Code", "monospace"],
      },
    },
  },
  plugins: [require("daisyui"), require("@tailwindcss/typography")],
  daisyui: {
    themes: [
      {
        catpuccin: {
          primary: "#ef9f76",
          secondary: "#f4b8e4",
          accent: "#ca9ee6",
          neutral: "#eff1f5",
          "base-100": "#1e1e2e",
          info: "#8caaee",
          success: "#a6d189",
          warning: "#f1d296",
          error: "#e78284",
        },
      },
    ],
  },
};
