import { Hero } from "@/components/Hero";
import { DocumentShowcase } from "@/components/DocumentShowcase";
import { documentTemplates } from "@/data/catalog";

/**
 * Landing page (PL-2): hero + responsive showcase of all document types.
 */
export default function Home() {
  return (
    <>
      <Hero documentCount={documentTemplates.length} />
      <DocumentShowcase />
    </>
  );
}
