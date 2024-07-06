import { __dirname } from "@/utils/paths";
import { genRange } from "@/utils/genRange";
import fs from "fs";
import path from "path";
import { isValidExt } from "./languages";
import { getFileData } from "./fileParsers";

export async function getAllFilesPaths() {
  const dirRange = genRange();
  let [a, b] = dirRange.next().value;
  let dir = path.join(__dirname, `${a}-${b}`);
  const filePaths = [];

  while (fs.existsSync(dir)) {
    const files = fs.readdirSync(dir);
    const filesConverted = files.map((file) => `${a}-${b}/${file}`);
    filePaths.push(...filesConverted);
    [a, b] = dirRange.next().value;
    dir = path.join(__dirname, `${a}-${b}`);
  }

  return filePaths.filter((file) =>
    isValidExt(file.split(".").pop() as string),
  );
}

export async function getAllScriptsData() {
  const filePaths = await getAllFilesPaths();
  const files = await Promise.all(filePaths.map((path) => getFileData(path)));
  return files;
}
