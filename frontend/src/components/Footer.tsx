import { Logo } from "./Logo";

/**
 * Global site footer with brand mark, short tagline, and the CommonPaper /
 * CC BY 4.0 attribution required by the template source.
 */
export function Footer() {
  const year = 2026;

  return (
    <footer className="mt-auto border-t border-[var(--color-border-subtle)] bg-surface">
      <div className="container-page flex flex-col gap-4 py-8 sm:flex-row sm:items-center sm:justify-between">
        <div className="flex flex-col gap-1">
          <Logo />
          <p className="text-sm text-brand-gray">
            Draft legal agreements with AI, from trusted templates.
          </p>
        </div>

        <p className="text-xs text-brand-gray">
          © {year} Prelegal. Templates based on{" "}
          <a
            href="https://commonpaper.com/"
            target="_blank"
            rel="noopener noreferrer"
            className="text-brand-blue hover:underline"
          >
            CommonPaper
          </a>{" "}
          Standard Terms, licensed under{" "}
          <a
            href="https://creativecommons.org/licenses/by/4.0/"
            target="_blank"
            rel="noopener noreferrer"
            className="text-brand-blue hover:underline"
          >
            CC BY 4.0
          </a>
          .
        </p>
      </div>
    </footer>
  );
}
