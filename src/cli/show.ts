import chalk from "chalk";
import type { BasicData } from "./types";

export function showBasic<T extends BasicData>(data: T) {
  const { id, name, path } = data;
  console.log(chalk.bold("Información del script:"));
  console.log(chalk.yellow(`- ID: ${id}`));
  console.log(chalk.yellow(`- Nombre: ${name}`));
  console.log(chalk.yellow(`- Ruta: /${path}`));
}
