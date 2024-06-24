import { JSONFilePreset } from "lowdb/node";
import type { MetaDataDB } from "../types";
import { emptyMetaData, listMeta, getAllMeta } from "../utils/metaData";
import { metaJSONPath } from "../consts";

const defaultData: MetaDataDB = emptyMetaData;

const metaDB = await JSONFilePreset<MetaDataDB>(metaJSONPath, defaultData);

for (const key of listMeta) {
  if (metaDB.data[key].length <= 1) {
    metaDB.data = await getAllMeta();
    metaDB.write();
    break;
  }
}

export { metaDB };
