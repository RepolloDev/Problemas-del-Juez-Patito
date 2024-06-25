import { UseScriptDB } from "@/data";
import type { ScriptData } from "@/data/types";
import FlexSearch from "flexsearch";

async function searchData(input?: string) {
  if (!input) {
    return [];
  }

  const index = new FlexSearch.Document<ScriptData, true>({
    tokenize: "forward",
    preset: "performance",
    cache: true,
    document: {
      id: "id",
      index: ["id", "name", "tags"],
      store: true,
    },
  });

  const files = await UseScriptDB.getScripts();
  files.forEach((file) => index.add(file));

  const results = await index.searchAsync(input, {
    limit: 10,
    enrich: true,
  });

  return results[0]?.result.map((item) => item.doc) || [];
}

export default searchData;
