import { codeHTML, markdownHTML } from "./parsers";
import type { FileRead } from "./types";
import { readFileById, readAllFiles } from "./read";

async function contentHtml(fileContent: FileRead): Promise<FileRead> {
  const { description, code, steps } = fileContent.content;
  const stepsHtml = await markdownHTML(steps);
  const codeHtml = await codeHTML(code);
  const descriptionHtml = await markdownHTML(description);
  return {
    ...fileContent,
    content: {
      description: descriptionHtml,
      steps: stepsHtml,
      code: codeHtml,
    },
  };
}

export async function contentHtmlById(id: number) {
  const fileContent = readFileById(id);
  return await contentHtml(fileContent);
}

export async function allContentHtml(): Promise<FileRead[]> {
  const filesContent = readAllFiles();
  const parsedFilesContent = filesContent.map((fileContent) =>
    contentHtml(fileContent),
  );
  return await Promise.all(parsedFilesContent);
}
