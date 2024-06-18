import { languages, __dirname } from "./constants";
import type { FileExt } from "./types";
import fs from "fs";

/**
 * @param ext : FileExt
 * @returns Object with the properties of the language with the given extension
 */

export function getLanguage(ext: FileExt) {
  return languages[ext];
}

/**
 * Remove comment lines and format the lines,
 * this depends on the language of the file
 * @param lines : string
 * @returns formatted lines without comments
 */

export function removeComment(lines: string, ext: FileExt) {
  const { comment } = getLanguage(ext);
  return lines.replace(comment, "").trim().replace(/\n/g, "");
}

/**
 * Generate a range of numbers from a given index
 * 0 -> [1000, 1199]
 * 1 -> [1200, 1399]
 * 2 -> [1400, 1599]
 * the current step is 199
 * @param index : number greater than 0
 */

export function* genRange(index: number = 0): Generator<[number, number]> {
  const init = 1000;
  const step = 199;

  let [a, b] = [init + index * (step + 1), init + index * (step + 1) + step];
  while (true) {
    yield [a, b];
    a = b + 1;
    b = a + step;
  }
}

export function readFileSync(pathFile: string) {
  const path = `${__dirname}/${pathFile}`;
  return fs.readFileSync(path, "utf-8");
}

export function readdirSync(pathDir: string) {
  const path = `${__dirname}/${pathDir}`;
  return fs.readdirSync(path);
}
