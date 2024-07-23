import { JSONFilePreset } from "lowdb/node";
import type { MetaDataDB, MetaData } from "@/data/types";
import { emptyMetaData, listMeta, getAllMeta } from "@/data/utils/metaData";
import { metaJSONPath } from "@/data/consts";

const defaultData: MetaDataDB = emptyMetaData;

export const metaDB = await JSONFilePreset<MetaDataDB>(
  metaJSONPath,
  defaultData,
);

export class UseMetaDB {
  private static isInit = false;
  static JSONPath = metaJSONPath;
  static data = metaDB.data;

  private static async init() {
    if (this.isInit) return;

    for (const key of listMeta) {
      if (metaDB.data[key].length <= 1) {
        metaDB.data = await getAllMeta();
        metaDB.write();
        break;
      }
    }
    this.isInit = true;
  }

  static async getMeta(key: keyof MetaDataDB) {
    await this.init();
    return metaDB.data[key];
  }

  static async getAllMeta() {
    await this.init();
    return metaDB.data;
  }

  static async save() {
    await this.init();
    metaDB.write();
  }

  static async read() {
    await this.init();
    metaDB.read();
  }

  static async update(fn: (data: MetaData) => unknown) {
    await this.init();
    await metaDB.update(fn);
  }
}
