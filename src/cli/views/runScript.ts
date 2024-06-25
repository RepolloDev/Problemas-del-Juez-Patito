import search from "../utils/search";
import run from "../utils/run";
import { showBasic } from "../utils/show";
import clear from "console-clear";
import inquirer from "inquirer";
import chalk from "chalk";

async function continueRun(): Promise<boolean> {
  const { confirm } = await inquirer.prompt([
    {
      type: "confirm",
      name: "confirm",
      message:
        chalk.bold.yellow("🫠 Desea volver a ejecutar el script?") +
        "\n" +
        chalk.dim.cyan("[Por defecto es No]"),
      default: false,
    },
  ]);
  return confirm;
}

export default async function view() {
  clear();
  const script = await search();
  do {
    clear();
    showBasic(script);
    await run(script);
  } while (await continueRun());
  clear();
}