// Properties of the languages object are the file extensions of the supported languages.
export const languages = {
  py: {
    name: "python",
    comment: "#",
    color: "#3572A5",
  },
  java: {
    name: "java",
    comment: "//",
    color: "#B07219",
  },
  cpp: {
    name: "c++",
    comment: "//",
    color: "#f34b7d",
  },
} as const;

export type FileExt = keyof typeof languages;

export function getLanguageByExt(ext: FileExt) {
  return languages[ext];
}

export function isValidExt(ext: string): ext is FileExt {
  return ext in languages;
}