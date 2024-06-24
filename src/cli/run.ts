import { spawn } from "child_process";
import chalk from "chalk";
import fs from "fs";
import path from "path";
import { __dirname } from "@/utils/paths";
import type { BasicData } from "./types";

async function runPythonScript(scriptPath: string): Promise<string> {
  const tempDir = path.join(__dirname, "src", "cli", "temp");
  if (!fs.existsSync(tempDir)) {
    fs.mkdirSync(tempDir, { recursive: true });
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

async function run<T extends BasicData>(data: T) {
  // mensaje de bienvenida
  const inputMessage = chalk.green.bold.underline(
    `🎹 Ingrese los datos para el script\n`
  );
  console.log(inputMessage);

  // ejecutar el script y mostrar el resultado
  const output = await runPythonScript(data.path);
  const outputMessage = chalk.blue.bold.underline(
    `\n🚀 Resultado del script\n`
  );
  console.log(outputMessage);
  console.log(fs.readFileSync(output, "utf-8"));
}

export default run;
