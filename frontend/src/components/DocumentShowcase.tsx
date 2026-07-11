import { documentTemplates } from "@/data/catalog";
import { DocumentCard } from "./DocumentCard";

/**
 * Responsive grid of all available document types, sourced from catalog.json.
 */
export function DocumentShowcase() {
  return (
    <section id="documents" className="container-page scroll-mt-20 py-16 sm:py-20">
      <div className="mx-auto max-w-2xl text-center">
        <h2 className="text-3xl font-bold tracking-tight text-brand-navy">
          {documentTemplates.length} agreements, ready to draft
        </h2>
        <p className="mt-3 text-brand-gray">
          Every template is based on CommonPaper Standard Terms. Pick one to see
          how the guided drafting flow works.
        </p>
      </div>

      <div className="mt-12 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {documentTemplates.map((template) => (
          <DocumentCard key={template.filename} template={template} />
        ))}
      </div>
    </section>
  );
}
