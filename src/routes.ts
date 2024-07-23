import { resolve, join } from "path";

// export const ROOT_DIR = [ROOT-FROM-PROJECT]
export const ROOT_DIR = resolve(".");
export const SRC_DIR = join(ROOT_DIR, "src");
export const DATA_DIR = join(SRC_DIR, "data");
export const CLI_DIR = join(SRC_DIR, "cli");
export const WEB_DIR = join(SRC_DIR, "web");
