import { UseMetaDB, UseScriptDB } from "../functions";

await UseScriptDB.save();
await UseMetaDB.save();
console.log("⭐ Los datos se han generado correctamente");
