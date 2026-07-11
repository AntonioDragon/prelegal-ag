import Link from "next/link";
import { Logo } from "./Logo";

/**
 * Global site header: logo on the left, primary nav + sign-in on the right.
 * Purely presentational for now (PL-1) — actions are placeholders.
 */
export function Header() {
  return (
    <header className="sticky top-0 z-40 border-b border-[var(--color-border-subtle)] bg-surface/90 backdrop-blur">
      <div className="container-page flex h-16 items-center justify-between">
        <Link href="/" className="flex items-center" aria-label="Prelegal home">
          <Logo />
        </Link>

        <nav className="flex items-center gap-6">
          <Link
            href="/#documents"
            className="hidden text-sm font-medium text-brand-gray transition-colors hover:text-brand-navy sm:inline"
          >
            Documents
          </Link>
          <button type="button" className="btn-primary text-sm" disabled>
            Sign in
          </button>
        </nav>
      </div>
    </header>
  );
}
