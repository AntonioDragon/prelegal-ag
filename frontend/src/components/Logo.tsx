/**
 * Prelegal wordmark logo. Uses the brand palette; "pre" in navy, "legal" in blue,
 * with a small yellow accent dot.
 */
export function Logo() {
  return (
    <span className="inline-flex items-baseline gap-0.5 text-2xl font-bold tracking-tight">
      <span className="text-brand-navy">pre</span>
      <span className="text-brand-blue">legal</span>
      <span className="text-brand-yellow">.</span>
    </span>
  );
}
