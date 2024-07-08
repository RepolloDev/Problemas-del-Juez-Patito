import type { ScriptContent } from "@/data/types";
import { getLanguageByExt, type FileExt } from "./languages";
import { removeManyInlineComments } from "./removers";

/**
 * Formats the content of a script file.
 * Read the README.md for more information of the structure of the script file.
 * @param content : plain text content of the script
 * @param ext : file extension of the script
 * @returns : object with the description, steps and code of the script
 */
export function formatScriptContent(
  content: string,
  ext: FileExt,
): ScriptContent {
  const { name: langName } = getLanguageByExt(ext);
  // const descRegex = /"""description[\r\n]+([\s\S]*?)[\r\n]+"""/g;
  const descRegex = /# description[\r\n]+((?:#[^\n]*\n)+)/;
  // const stepsRegex = /"""steps[\r\n]+([\s\S]*?)[\r\n]+"""/g;
  const stepsRegex = /# steps[\r\n]+((?:#[^\n]*\n)+)/;

  const description = removeManyInlineComments(
    descRegex.exec(content)?.[1] || "",
    ext,
  );
  const steps = removeManyInlineComments(
    stepsRegex.exec(content)?.[1] || "",
    ext,
  );
  const codeReplaced = content
    .replace(descRegex, "")
    .replace(stepsRegex, "")
    .trim();
  const code = `\`\`\`${langName}\n${codeReplaced}\n\`\`\``;

  return {
    description,
    steps,
    code,
  };
}
