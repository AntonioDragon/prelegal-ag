// Copies the root catalog.json into the frontend so it can be imported by the
// app (Next.js/Turbopack cannot import files outside the project root).
// The root catalog.json remains the single source of truth; this generated
// copy is git-ignored.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = resolve(here, "../../catalog.json");
const destDir = resolve(here, "../src/data");
const dest = resolve(destDir, "catalog.json");

mkdirSync(destDir, { recursive: true });
copyFileSync(source, dest);
console.log(`Copied catalog.json -> ${dest}`);
