import { JSONFilePreset } from "lowdb/node";
import { getAllScriptsData } from "../utils/scriptsData";
import type { ScriptDataDB } from "../types";
import { scriptsJSONPath } from "../consts";

const defaultData: ScriptDataDB = [];

const scriptsDB = await JSONFilePreset<ScriptDataDB>(
  scriptsJSONPath,
  defaultData
);

if (scriptsDB.data.length <= 1) {
  scriptsDB.data = await getAllScriptsData();
  scriptsDB.write();
}

export { scriptsDB };
