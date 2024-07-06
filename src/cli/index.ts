import chalk from "chalk";
import runScript from "./views/runScript";
import deleteScript from "./views/deleteScript";
import inquirer from "inquirer";
import clear from "console-clear";

clear();
while (true) {
  const { action } = await inquirer.prompt([
    {
      type: "list",
      name: "action",
      message: "¿Qué deseas hacer?",
      choices: [
        {
          name: "📦 Crear script",
          disabled: "Próximamente",
          value: "create",
        },
        {
          name: "🔍 Buscar script",
          disabled: "Próximamente",
          value: "search",
        },
        {
          name: "🏁 Ejecutar script",
          value: "run",
        },
        {
          name: "📍 Eliminar script",
          value: "delete",
        },
        {
          name: chalk.bold.red("❌ Salir"),
          value: "exit",
        },
      ],
    },
  ]);

  switch (action) {
    case "run":
      await runScript();
      break;
    case "delete":
      await deleteScript();
      break;
    case "exit":
      clear();
      process.exit(0);
    default:
      console.log("Opción no válida");
      clear();
  }
}
