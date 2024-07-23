import { spawn } from "child_process";
import chalk from "chalk";
import fs from "fs";
import path from "path";
import type { ScriptData } from "@/data/types";
import { CLI_DIR } from "@/routes";

async function runPythonScript(scriptPath: string): Promise<string> {
  const tempDir = path.join(CLI_DIR, "temp");
  if (!fs.existsSync(tempDir)) {
    fs.mkdirSync(tempDir, { recursive: true });
  }

  if (!fs.existsSync(scriptPath)) {
    throw new Error("El script no existe");
  }

  return new Promise((resolve, reject) => {
    // set up temp file
    const tempOutputPath = path.join(tempDir, "output.md");
    const outputStream = fs.createWriteStream(tempOutputPath);

    const pythonProcess = spawn("python", [scriptPath], {
      stdio: ["inherit", "pipe", "pipe"],
    });

    // save output
    pythonProcess.stdout.pipe(outputStream);
    pythonProcess.stderr.pipe(outputStream);

    // cases
    pythonProcess.on("close", (code) => {
      outputStream.close();
      resolve(tempOutputPath);
    });

    pythonProcess.on("error", (error) => {
      outputStream.close();
      reject(error);
    });
  });
}

export default async function run(data: ScriptData) {
  // mensaje de bienvenida
  const inputMessage = chalk.green.bold.underline(
    `🎹 Ingrese los datos para el script\n`,
  );
  console.log(inputMessage);

  // ejecutar el script y mostrar el resultado
  const output = await runPythonScript(data.path);
  const outputMessage = chalk.blue.bold.underline(
    `\n🚀 Resultado del script\n`,
  );
  console.log(outputMessage);
  console.log(fs.readFileSync(output, "utf-8"));
}
