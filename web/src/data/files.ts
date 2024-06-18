import fs from "fs";
import { genRange, readdirSync } from "./utils";
import { fileExtList, __dirname } from "./constants";
import type { FileExt, FileInfo } from "./types";

/**
 * @returns dirs: List of directories of the form [a-b] where a and b are numbers
 */
function allDirs() {
  const range = genRange();
  let [a, b] = range.next().value;
  const dirs = [];

  while (fs.existsSync(`${__dirname}/${a}-${b}`)) {
    dirs.push(`${a}-${b}`);
    [a, b] = range.next().value;
  }

  return dirs;
}

/**
 * Return only the files with the following extensions:
 * - .py
 * - .java
 * - .cpp
 * * See the fileExtList constant in src/data/constants.ts
 * @returns files: List of all files in the directories
 */
export function allFilePaths() {
  const dirs = allDirs();
  const listFiles = dirs.map((dir) => {
    const files = readdirSync(dir);
    return files.map((file) => `${dir}/${file}`);
  });

  return listFiles.flat().filter((file) => {
    return fileExtList.some((ext) => file.endsWith(ext));
  });
}

/**
 * @param filePath : string of the form [a-b]/[id]_[name].[ext]
 * @returns fileInfo: Object with the following properties:
 * - id: The id of the file
 * - name: The name of the file
 * - ext: The extension of the file
 * - fileName: The name of the file with the extension
 * - path: The path of the file
 */
function parseFileInfo(filePath: string): FileInfo {
  const splitPath = filePath.split("/");
  const fileName = splitPath.pop() as string;

  try {
    const [id, ...rest] = fileName.split("_");
    const [name, ...ext] = rest.join("_").split(".");
    const data = {
      id: parseInt(id),
      name: name.replace(/_/g, " "),
      ext: ext.pop() as FileExt,
      fileName,
      path: filePath,
    };
    return data;
  } catch (error) {
    throw new Error(`Error parsing file: ${filePath}`);
  }
}

/**
 * @param index : number greater or equal to 0 --> range [a_0, b_0]
 * @returns filesObj: List of objects with the following properties:
 * - id: The id of the file
 * - name: The name of the file
 * - ext: The extension of the file
 */
export function getAllFilesInfo(): FileInfo[] {
  const files = allFilePaths();
  return files.map((file) => {
    return parseFileInfo(file);
  });
}

/**
 * @param id : id of the file
 * @returns fileInfo: Object with the following properties:
 * - id: The id of the file
 * - name: The name of the file
 * - ext: The extension of the file
 * - fileName: The name of the file with the extension
 * - path: The path of the file
 */

export function getFileInfoById(id: number) {
  const pathFile = getAllFilesInfo().find((file) => file.id === id);
  if (!pathFile) {
    throw new Error(`File with id ${id} not found`);
  }
  return pathFile;
}
