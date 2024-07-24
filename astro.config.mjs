import { defineConfig } from "astro/config";
import icon from "astro-icon";
import markdownIntegration from "@astropub/md";
import rehypeMathjax from "rehype-mathjax";
import remarkMath from "remark-math";
import callouts from "remark-callouts";
import rehypePrettyCode from "rehype-pretty-code";
import tailwind from "@astrojs/tailwind";
import { BASE_SITE } from "./src/routes";

// https://astro.build/config
export default defineConfig({
  srcDir: "./src/web",
  // ? If not working npm run dev, try to change root to "./src/web"
  //root: "./src/web",
  outDir: "./src/web/dist",
  output: "static",
  publicDir: "./public",
  devToolbar: {
    enabled: false,
  },
  integrations: [
    icon({
      iconDir: "./src/web/assets/icons",
      include: ["**/*.svg"],
    }),
    markdownIntegration(),
    tailwind(),
  ],
  markdown: {
    gfm: true,
    remarkPlugins: [remarkMath, callouts],
    rehypePlugins: [
      rehypeMathjax,
      [
        rehypePrettyCode,
        {
          theme: "catppuccin-mocha",
          defaultLang: "bash",
        },
      ],
    ],
  },
  site: "https://repollodev.github.io",
  base: BASE_SITE,
});
