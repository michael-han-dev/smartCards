/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/**/*.{html,js,vue}',
    './src/*.{html,js,vue}'
  ],
  theme: {
    extend: {
      fontFamily: {
        'roboto': ['Roboto', 'sans-serif']
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms')
  ],
}