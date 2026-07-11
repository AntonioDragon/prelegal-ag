/**
 * Right column of the workspace: a mockup of the live document preview (PL-3).
 * Shows a paper-like sheet with skeleton lines and disabled Save / Download
 * actions. Real preview rendering and PDF export come later.
 */
export function PreviewPanel() {
  return (
    <div className="flex h-full flex-col rounded-[var(--radius-card)] border border-[var(--color-border-subtle)] bg-surface">
      {/* Panel header with actions */}
      <div className="flex items-center justify-between border-b border-[var(--color-border-subtle)] px-5 py-4">
        <div>
          <p className="text-sm font-semibold text-brand-navy">
            Document preview
          </p>
          <p className="text-xs text-brand-gray">Updates as you chat</p>
        </div>
        <div className="flex items-center gap-2">
          <button type="button" className="btn-secondary text-sm" disabled>
            Save
          </button>
          <button type="button" className="btn-primary text-sm" disabled>
            Download
          </button>
        </div>
      </div>

      {/* Paper sheet mockup */}
      <div className="flex-1 overflow-y-auto bg-surface-muted p-6">
        <div className="mx-auto max-w-xl rounded-md bg-white p-8 shadow-sm ring-1 ring-[var(--color-border-subtle)]">
          <div className="text-center">
            <h3 className="text-lg font-bold uppercase tracking-wide text-brand-navy">
              Mutual Non-Disclosure Agreement
            </h3>
            <div className="mx-auto mt-2 h-px w-16 bg-brand-yellow" />
          </div>

          <SkeletonBlock label="Parties" lines={2} />
          <SkeletonBlock label="Purpose" lines={3} />
          <SkeletonBlock label="Confidentiality Term" lines={2} />
          <SkeletonBlock label="Governing Law" lines={1} />
        </div>
      </div>
    </div>
  );
}

function SkeletonBlock({ label, lines }: { label: string; lines: number }) {
  return (
    <div className="mt-6">
      <p className="text-xs font-semibold uppercase tracking-wide text-brand-gray">
        {label}
      </p>
      <div className="mt-2 space-y-2" aria-hidden="true">
        {Array.from({ length: lines }).map((_, i) => (
          <div
            key={i}
            className="h-3 rounded bg-surface-muted"
            style={{ width: `${100 - i * 12}%` }}
          />
        ))}
      </div>
    </div>
  );
}
