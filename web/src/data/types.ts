import type { languages } from "./constants";

export type FileExt = keyof typeof languages;

export interface FileInfo {
  id: number;
  name: string;
  ext: FileExt;
  fileName: string;
  path: string;
}

export interface FileContent {
  description: string;
  steps: string;
  code: string;
}

export interface FileRead extends FileInfo {
  url: string;
  tags: string[];
  content: FileContent;
}
