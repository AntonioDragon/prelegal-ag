import Link from "next/link";

/**
 * Landing-page hero. Sets the value proposition and points down to the
 * document showcase. CTAs are placeholders until the workspace exists.
 */
export function Hero({ documentCount }: { documentCount: number }) {
  return (
    <section className="relative overflow-hidden border-b border-[var(--color-border-subtle)] bg-surface">
      <div className="container-page flex flex-col items-center py-20 text-center sm:py-28">
        <span className="rounded-full bg-brand-yellow/15 px-3 py-1 text-xs font-semibold uppercase tracking-wide text-brand-navy">
          AI-guided legal drafting
        </span>

        <h1 className="mt-6 max-w-3xl text-4xl font-bold tracking-tight text-brand-navy sm:text-6xl">
          Draft legal agreements by simply{" "}
          <span className="text-brand-blue">having a conversation</span>
        </h1>

        <p className="mt-6 max-w-2xl text-lg text-brand-gray">
          Prelegal turns {documentCount} trusted templates into finished
          documents. Tell our assistant what you need, answer a few questions,
          and download a ready-to-sign agreement.
        </p>

        <div className="mt-10 flex flex-col gap-3 sm:flex-row">
          <Link href="/#documents" className="btn-primary">
            Browse documents
          </Link>
          <Link href="/workspace" className="btn-secondary">
            Start a chat
          </Link>
        </div>
      </div>
    </section>
  );
}
