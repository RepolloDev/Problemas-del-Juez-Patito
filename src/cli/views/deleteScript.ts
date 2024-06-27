import search from "../utils/search";
import { showBasic } from "../utils/show";
import clear from "console-clear";
import inquirer from "inquirer";
import { deleteScript } from "../utils/delete";
import wait from "../utils/wait";

export default async function view() {
  clear();
  const script = await search();
  clear();
  showBasic(script);
  const { confirm } = await inquirer.prompt({
    type: "confirm",
    name: "confirm",
    message: "¿Desea eliminar el script?",
  });

  if (confirm) {
    deleteScript(script);
    console.log("🗑️ Script eliminado");
  } else {
    console.log("🫠 Cancelado");
  }

  await wait();
  clear();
}
