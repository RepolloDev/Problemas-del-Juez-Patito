import type { MetaData } from "../types";
import { getAllFilesPaths } from "./scriptsData";
import { getFileInfo } from "./fileParsers";

// this variable only exists to get the keys of the MetaData interface
export const emptyMetaData: MetaData = {
  tags: [],
};

export const listMeta = Object.keys(emptyMetaData) as (keyof MetaData)[];

export async function getAllMeta() {
  const paths = await getAllFilesPaths();
  const files = await Promise.all(paths.map((path) => getFileInfo(path)));
  let meta: MetaData = { ...emptyMetaData };
  for (const file of files) {
    for (const key of listMeta) {
      for (const item of file[key]) {
        if (!meta[key].includes(item)) {
          meta[key].push(item);
        }
      }
    }
  }
  return meta;
}
