/** @type {import('tailwindcss').Config} */

export default {
  content: ['./src/**/*.{js,ts,jsx,tsx,mdx}'],
  theme: {
    extend: {
      fontFamily: {
        "fira-code": ["Fira Code Variable", "monospace"],
        "pitagon": ["Pitagon Sans", "sans-serif"]
      }
    },
  },
};
