/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", //template for at the project level app
    "./**/templates/**/*.html", //template for inside app
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

