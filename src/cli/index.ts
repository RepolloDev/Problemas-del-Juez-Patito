import search from "./search";
import run from "./run";
import { showBasic } from "./show";

const data = await search();
showBasic(data);
await run(data);
