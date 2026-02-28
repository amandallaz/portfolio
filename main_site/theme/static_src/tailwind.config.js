/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
  content: [
    "../templates/**/*.html",        // theme templates
    "../../**/templates/**/*.html",  // ALL Django templates (this is the key one)
  ],
  // theme: {
  //     extend: {},
  // },
  theme: {
    extend: {
      colors: {
        cream: "#fcf1dd",
        sand: "#f5e5c0",
        charcoal: "#2e2e2e",
      },
      fontFamily: {
        serif: ["Playfair Display", "serif"],
        sans: ['"DM Sans"', 'ui-sans-serif', 'system-ui'],
      },
    },
  },
  plugins: [
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/aspect-ratio"),
    require("daisyui") /** added to use daisy */,
  ],
};


