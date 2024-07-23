import { ROOT_DIR } from "@/routes";
import { metaJSONPath, scriptsJSONPath } from "@/data/consts";
import fs from "fs";
import path from "path";

const paths = [
  path.join(ROOT_DIR, scriptsJSONPath),
  path.join(ROOT_DIR, metaJSONPath),
];

for (const p of paths) {
  if (fs.existsSync(p)) {
    fs.unlinkSync(p);
  }
}

console.log("⭐ Los datos se han eliminado correctamente");
