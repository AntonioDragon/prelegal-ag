/**
 * Home page — PL-1 placeholder.
 * The visual foundation (layout, header, footer, design tokens) is in place.
 * PL-2 replaces this with the hero + document showcase.
 */
export default function Home() {
  return (
    <section className="container-page flex flex-col items-center py-24 text-center">
      <span className="rounded-full bg-brand-yellow/15 px-3 py-1 text-xs font-semibold uppercase tracking-wide text-brand-navy">
        Design system ready
      </span>
      <h1 className="mt-6 max-w-2xl text-4xl font-bold tracking-tight text-brand-navy sm:text-5xl">
        Visual foundation for Prelegal
      </h1>
      <p className="mt-4 max-w-xl text-brand-gray">
        Global layout, header, footer, and brand design tokens are in place.
        The landing page and document workspace come next.
      </p>
    </section>
  );
}
