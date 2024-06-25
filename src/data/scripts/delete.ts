import { __dirname } from "@/utils/paths";
import { metaJSONPath, scriptsJSONPath } from "../consts";
import fs from "fs";
import path from "path";

const paths = [
  path.join(__dirname, scriptsJSONPath),
  path.join(__dirname, metaJSONPath),
];

for (const p of paths) {
  if (fs.existsSync(p)) {
    fs.unlinkSync(p);
  }
}

console.log("⭐ Los datos se han eliminado correctamente");
