import type { DocumentTemplate } from "@/data/catalog";

/**
 * A single document type card for the landing-page showcase.
 * Presentational only (PL-2) — clicking is wired up in a later task.
 */
export function DocumentCard({ template }: { template: DocumentTemplate }) {
  const initials = getInitials(template.name);

  return (
    <article className="group flex h-full flex-col rounded-[var(--radius-card)] border border-[var(--color-border-subtle)] bg-surface p-6 transition-shadow hover:shadow-lg">
      <div
        className="flex h-11 w-11 items-center justify-center rounded-lg bg-brand-blue/10 text-sm font-bold text-brand-blue"
        aria-hidden="true"
      >
        {initials}
      </div>

      <h3 className="mt-4 text-lg font-semibold leading-snug text-brand-navy">
        {template.name}
      </h3>
      <p className="mt-2 flex-1 text-sm leading-relaxed text-brand-gray">
        {template.description}
      </p>

      <span className="mt-4 inline-flex items-center gap-1 text-sm font-semibold text-brand-purple opacity-0 transition-opacity group-hover:opacity-100">
        Draft this
        <svg
          width="16"
          height="16"
          viewBox="0 0 16 16"
          fill="none"
          aria-hidden="true"
        >
          <path
            d="M6 3l5 5-5 5"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        </svg>
      </span>
    </article>
  );
}

/** Build up to two-letter initials from the significant words of a name. */
function getInitials(name: string): string {
  const stop = new Set(["of", "and", "the", "for", "a", "an"]);
  const words = name
    .split(/\s+/)
    .filter((w) => w.length > 0 && !stop.has(w.toLowerCase()));
  const letters = words.map((w) => w[0].toUpperCase());
  return letters.slice(0, 2).join("");
}
