import autocomplete from "inquirer-autocomplete-standalone";
import searchData from "@/utils/searchData";
import chalk from "chalk";

export default async function search() {
  const result = await autocomplete({
    message: chalk.bold("🔍 Buscar un script"),
    source: async (input) => {
      const filtered = await searchData(input);
      return filtered.map((item) => ({
        name: `[${item.id}] - ${item.name}`,
        value: item,
        description: chalk.blue(
          `🗂️ Este archivo esta ubicado en /${item.path}`
        ),
      }));
    },
    emptyText: chalk.underline("Escribe para comenzar a buscar: "),
    pageSize: 10,
  });
  return result;
}
