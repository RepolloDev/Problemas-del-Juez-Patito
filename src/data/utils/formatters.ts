import type { ScriptContent } from "@/data/types";
import { getLanguageByExt, type FileExt } from "./languages";

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
  const descRegex = /"""description[\r\n]+([\s\S]*?)[\r\n]+"""/g;
  const stepsRegex = /"""steps[\r\n]+([\s\S]*?)[\r\n]+"""/g;

  const description = descRegex.exec(content)?.[1] || "";
  const steps = stepsRegex.exec(content)?.[1] || "";
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
