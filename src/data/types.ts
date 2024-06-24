export interface MetaData {
  // all properties are always arrays
  tags: string[];
}

export interface ScriptContent {
  description: string;
  steps: string;
  code: string;
}

export interface ScriptData extends MetaData {
  id: string;
  name: string;
  url: string;
  extension: string;
  filename: string;
  path: string;
  content: ScriptContent;
}

export type ScriptDataDB = ScriptData[];
export type MetaDataDB = MetaData;
