import path from "node:path";
import type { FileExt } from "./types";

export const languages = {
  py: {
    name: "python",
    ext: "py",
    comment: "#",
    color: "#3572A5",
  },
  java: {
    name: "java",
    ext: "java",
    comment: "//",
    color: "#B07219",
  },
  cpp: {
    name: "c++",
    ext: "cpp",
    comment: "//",
    color: "#f34b7d",
  },
} as const;

export const fileExtList: FileExt[] = Object.keys(languages) as FileExt[];

// This is the path to the root directory of the project
// ! This resolve root repo directory
export const __dirname = path.resolve(path.dirname("../../"));
