import { defineConfig } from "astro/config";
import icon from "astro-icon"

export default defineConfig({
  srcDir: "./src/web",
  // ? If not working npm run dev, try to change root to "./src/web"
  //root: "./src/web",
  outDir: "./src/web/build",
  output: "static",
  publicDir: "./src/web/assets",
  integrations: [
    icon({
      iconDir: "./src/web/assets/icons", include: ["**/*.svg"], output: "./src/web/build/icons"
    })
  ],
});
