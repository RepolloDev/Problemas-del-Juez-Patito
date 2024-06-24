import { getLanguageByExt, type FileExt } from "./languages";

/**
 * @param text : line of code
 * @param ext : file extension of the code
 * @returns : line of code without comments
 */
export function removeInlineComments(text: string, ext: FileExt) {
  const { comment } = getLanguageByExt(ext);
  return text.replace(comment, "").trim().replace(/\n/g, "");
}
