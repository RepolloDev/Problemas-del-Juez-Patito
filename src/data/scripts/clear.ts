// ! This script only removes the data
import { __dirname } from "@/utils/paths";
import { metaJSONPath, scriptsJSONPath } from "../consts";

import fs from "fs";
import path from "path";

const deletePaths = [
  path.join(__dirname, scriptsJSONPath),
  path.join(__dirname, metaJSONPath),
];

let sw = true;
for (const deletePath of deletePaths) {
  try {
    fs.unlinkSync(deletePath);
  } catch (error) {
    console.error(`❌ No se puedo eliminar: ${deletePath}`);
    sw = false;
  }
}

if (sw) {
  console.log("✅ Data removed successfully");
}
