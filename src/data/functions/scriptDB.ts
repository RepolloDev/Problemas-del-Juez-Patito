import { JSONFilePreset } from "lowdb/node";
import { getAllScriptsData } from "../utils/scriptsData";
import type { ScriptDataDB } from "../types";
import { scriptsJSONPath } from "../consts";

const defaultData: ScriptDataDB = [];

export const scriptDB = await JSONFilePreset<ScriptDataDB>(
  scriptsJSONPath,
  defaultData,
);

// if (scriptsDB.data.length <= 1) {
//   scriptsDB.data = await getAllScriptsData();
//   scriptsDB.write();
// }

export class UseScriptDB {
  private static isInit = false;
  static JSONPath = scriptsJSONPath;
  static data = scriptDB.data;

  private static async init() {
    if (this.isInit) return;

    // Check if the data is empty
    if (scriptDB.data.length <= 1) {
      scriptDB.data = await getAllScriptsData();
      scriptDB.write();
    }
    this.isInit = true;
  }

  static async getScripts() {
    await this.init();
    return scriptDB.data;
  }

  static async save() {
    await this.init();
    scriptDB.write();
  }

  static async read() {
    await this.init();
    scriptDB.read();
  }

  static async update(fn: (data: ScriptDataDB) => unknown) {
    await this.init();
    await scriptDB.update(fn);
  }
}
