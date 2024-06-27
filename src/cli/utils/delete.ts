import { __dirname } from "@/utils/paths";
import path from "path";
import fs from "fs";
import type { ScriptData } from "@/data/types";

export function deleteScript(script: ScriptData) {
  const { path: scriptPath } = script;
  const resolvedPath = path.join(__dirname, scriptPath);
  if (!fs.existsSync(resolvedPath)) {
    throw new Error("❌ El script no existe");
  }
  fs.unlinkSync(resolvedPath);
}
