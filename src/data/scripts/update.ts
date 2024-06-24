import "./clear";
import { metaDB, scriptsDB } from "../functions";

await metaDB.read();
await scriptsDB.read();

console.log("🗂️ Los datos se cargaron correctamente");