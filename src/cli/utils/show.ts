import chalk from "chalk";
import type { ScriptData } from "@/data/types";

export function showBasic(data: ScriptData) {
  const { id, name, path } = data;
  console.log(chalk.bold.yellowBright(`💠 Información del script`));
  console.log("- " + chalk.bold(`ID: `) + chalk.blueBright(id));
  console.log("- " + chalk.bold(`Nombre: `) + chalk.blueBright(name));
  console.log("- " + chalk.bold(`Ruta: `) + chalk.blueBright(path));
}

export function showFull(data: ScriptData) {
  const { id, name, path, extension, filename, tags, url } = data;
  console.log(chalk.bold.yellowBright(`💠 Información del script`));
  console.log("- " + chalk.bold(`ID: `) + chalk.blueBright(id));
  console.log("- " + chalk.bold(`Nombre: `) + chalk.blueBright(name));
  console.log("- " + chalk.bold(`Ruta: `) + chalk.blueBright(path));
  console.log("- " + chalk.bold(`Extensión: `) + chalk.blueBright(extension));
  console.log(
    "- " + chalk.bold(`Nombre del archivo: `) + chalk.blueBright(filename)
  );
  console.log(
    "- " + chalk.bold(`Etiquetas: `) + chalk.blueBright(tags.join(", "))
  );
  console.log("- " + chalk.bold(`URL: `) + chalk.blueBright(url));
}