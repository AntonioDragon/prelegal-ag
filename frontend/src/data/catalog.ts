// catalog.json is synced from the repo-root source of truth by
// scripts/copy-catalog.mjs (runs on predev/prebuild). The copy is git-ignored.
import catalogJson from "./catalog.json";

export interface DocumentTemplate {
  name: string;
  description: string;
  filename: string;
}

interface Catalog {
  source: string;
  license: string;
  templates: DocumentTemplate[];
}

const catalog = catalogJson as Catalog;

/**
 * The 11 primary document types offered by Prelegal.
 * The catalog also contains the "Mutual NDA Cover Page", which is a companion
 * to the Mutual NDA rather than a standalone document, so it is filtered out.
 */
export const documentTemplates: DocumentTemplate[] = catalog.templates.filter(
  (t) => t.filename !== "Mutual-NDA-coverpage.md"
);

export const catalogSource = catalog.source;
export const catalogLicense = catalog.license;
