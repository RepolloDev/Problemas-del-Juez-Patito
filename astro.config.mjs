import { defineConfig } from "astro/config";
import icon from "astro-icon";

export default defineConfig({
  srcDir: "./src/web",
  // ? If not working npm run dev, try to change root to "./src/web"
  //root: "./src/web",
  outDir: "./src/web/dist",
  output: "static",
  publicDir: "./public",
  cacheDir: "./node_modules/.cache/astro",
  devToolbar: {
    enabled: false
  },
  integrations: [
    icon({
      iconDir: "./src/web/assets/icons",
      include: ["**/*.svg"],
    }),
  ],
  site: "https://repollodev.github.io",
  base: "Problemas-del-Juez-Patito",
});
