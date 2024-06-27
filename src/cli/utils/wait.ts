import PressToContinuePrompt from "inquirer-press-to-continue";
import type { KeyDescriptor } from "inquirer-press-to-continue";
import inquirer from "inquirer";

export default async function wait() {
  inquirer.registerPrompt("press-to-continue", PressToContinuePrompt);
}
