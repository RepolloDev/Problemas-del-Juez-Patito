import rehypeStringify from "rehype-stringify";
import remarkParse from "remark-parse";
import remarkRehype from "remark-rehype";
import rehypeMathjax from "rehype-mathjax";
import remarkMath from "remark-math";
import { unified } from "unified";
import callouts from "remark-callouts";
import rehypePrettyCode from "rehype-pretty-code";
import remarkGfm from "remark-gfm";

export const codeProcessor = unified()
  .use(remarkParse)
  .use(remarkRehype)
  .use(rehypePrettyCode, {
    theme: "github-dark",
    defaultLang: "plaintext",
    keepBackground: false,
  })
  .use(rehypeStringify);

export const markdownProcessor = unified()
  .use(remarkParse)
  .use(remarkGfm)
  .use(callouts)
  .use(remarkMath)
  .use(remarkRehype)
  .use(rehypePrettyCode, {
    theme: "github-dark",
    defaultLang: "bash",
  })
  .use(rehypeMathjax)
  .use(rehypeStringify);

export async function markdownHTML(markdown: string) {
  const result = await markdownProcessor.process(markdown);
  return result.toString();
}

export async function codeHTML(code: string) {
  const result = await codeProcessor.process(code);
  return result.toString();
}
