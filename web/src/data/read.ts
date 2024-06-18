import { getFileInfoById, getAllFilesInfo } from "./files";
import { getLanguage, removeComment, readFileSync } from "./utils";
import type { FileExt, FileInfo, FileRead, FileContent } from "./types";

function parseFileContent(text: string, lang: FileExt): FileContent {
  const descRegex = /"""description[\r\n]+([\s\S]*?)[\r\n]+"""/g;
  const stepsRegex = /"""steps[\r\n]+([\s\S]*?)[\r\n]+"""/g;

  const description = descRegex.exec(text)?.[1] || "";
  const steps = stepsRegex.exec(text)?.[1] || "";
  const code = text.replace(descRegex, "").replace(stepsRegex, "").trim();

  const { name: language } = getLanguage(lang);
  const codeWithLanguage = `\`\`\`${language}\n${code}\n\`\`\``;

  const result = {
    description,
    steps,
    code: codeWithLanguage,
  };
  return result;
}

function parseToFileContent(fileInfo: FileInfo): FileRead {
  const plainText = readFileSync(fileInfo.path);

  const [, , urlLine, tagsLine, ...rest] = plainText.split("\n");
  const url = removeComment(urlLine, fileInfo.ext);
  const tags = removeComment(tagsLine, fileInfo.ext).split(" ");
  const text = rest.join("\n");

  return {
    ...fileInfo,
    url,
    tags,
    content: parseFileContent(text, fileInfo.ext),
  };
}

export function readFileById(idFile: number): FileRead {
  const fileInfo = getFileInfoById(idFile);
  return parseToFileContent(fileInfo);
}

export function readAllFiles(): FileRead[] {
  const filesInfo = getAllFilesInfo();
  return filesInfo.map((fileInfo) => {
    return parseToFileContent(fileInfo);
  });
}
