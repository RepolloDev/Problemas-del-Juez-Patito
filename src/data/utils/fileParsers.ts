import { isValidExt, type FileExt } from "./languages";
import { removeInlineComments } from "./removers";
import { formatScriptContent } from "./formatters";
import type { ScriptData } from "@/data/types";
import fs from "fs";

interface PathInfo {
  id: string;
  name: string;
  extension: FileExt;
  filename: string;
  path: string;
}

export async function getPathInfo(filePath: string): Promise<PathInfo> {
  const splitPath = filePath.split("/");
  // get the last element of the array "root/folder/file.ext" => "file.ext
  const filename = splitPath.pop();

  if (!filename) {
    throw new Error(`Error parsing file: ${filePath}`);
  }

  // the structure of the file name is "id_name.ext"
  let [id, ...rest] = filename.split("_");
  let [name, ...exts] = rest.join("_").split(".");

  // get last extension
  let extension = exts.pop();

  if (!extension) {
    throw new Error(`This file has no extension: ${filePath}`);
  }

  if (!isValidExt(extension)) {
    throw new Error(`Invalid extension: ${extension} in file: ${filePath}`);
  }

  if (isNaN(Number(id))) {
    throw new Error(`Invalid id: ${id} in file: ${filePath}`);
  }

  // if the file name has multiple extensions, join them
  name = (name + exts.join(".")).replace(/_/g, " ");

  return {
    id,
    name,
    extension,
    filename,
    path: filePath,
  };
}

interface FileInfo extends PathInfo {
  url: string;
  tags: string[];
  content: string;
}

export async function getFileInfo(value: string | PathInfo): Promise<FileInfo> {
  const pathInfo = typeof value === "string" ? await getPathInfo(value) : value;
  const { path, extension } = pathInfo;

  if (!fs.existsSync(path)) {
    throw new Error(`File not found: ${path}`);
  }

  const plainText = fs.readFileSync(path, "utf-8");

  // idLine and nameLine are not used, but they are here to keep the order
  const [idLine, nameLine, urlLine, tagsLine, ...rest] = plainText.split("\n");

  const url = removeInlineComments(urlLine, extension);
  const tags = removeInlineComments(tagsLine, extension)?.split(" ") ?? [];
  const content = rest.join("\n");

  return {
    ...pathInfo,
    url,
    tags,
    content,
  };
}

export async function getFileData(
  value: string | FileInfo,
): Promise<ScriptData> {
  const data = typeof value === "string" ? await getFileInfo(value) : value;
  const { content, extension } = data;
  const formattedContent = formatScriptContent(content, extension);
  return {
    ...data,
    content: formattedContent,
  };
}
