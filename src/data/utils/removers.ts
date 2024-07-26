import { getLanguageByExt, type FileExt } from "./languages";

/**
 * @param text : line of code
 * @param ext : file extension of the code
 * @returns : line of code without comments
 */
export function removeInlineComments(text: string, ext: FileExt) {
  const { comment } = getLanguageByExt(ext);
  return text?.replace(comment, "").trim().replace(/\n/g, "");
}

export function removeManyInlineComments(text: string, ext: FileExt) {
  const { comment } = getLanguageByExt(ext);
  const comments = text.split("\n").map((line) => line.replace(comment, ""));
  const result = comments.join("\n").trim();
  if (result.includes("TODO")) return "";
  return result;
}