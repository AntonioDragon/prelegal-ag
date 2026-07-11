/**
 * Left column of the workspace: a static mockup of the AI chat (PL-3).
 * No real messaging yet — this establishes the layout, message bubbles, and
 * the composer. Wiring to the backend comes in a later task.
 */
export function ChatPanel() {
  return (
    <div className="flex h-full flex-col rounded-[var(--radius-card)] border border-[var(--color-border-subtle)] bg-surface">
      {/* Panel header */}
      <div className="flex items-center gap-3 border-b border-[var(--color-border-subtle)] px-5 py-4">
        <span
          className="flex h-9 w-9 items-center justify-center rounded-full bg-brand-blue/10 text-sm font-bold text-brand-blue"
          aria-hidden="true"
        >
          AI
        </span>
        <div>
          <p className="text-sm font-semibold text-brand-navy">
            Drafting assistant
          </p>
          <p className="text-xs text-brand-gray">Guides you through the document</p>
        </div>
      </div>

      {/* Messages */}
      <div className="flex flex-1 flex-col gap-4 overflow-y-auto p-5">
        <AssistantBubble>
          Hi! I can help you draft a legal agreement. What kind of document do
          you need today?
        </AssistantBubble>
        <UserBubble>I need a mutual NDA with a partner company.</UserBubble>
        <AssistantBubble>
          Great choice. Who are the two parties entering into this NDA? Please
          share each company&apos;s legal name.
        </AssistantBubble>
      </div>

      {/* Composer (disabled placeholder) */}
      <div className="border-t border-[var(--color-border-subtle)] p-4">
        <div className="flex items-end gap-2">
          <textarea
            rows={1}
            disabled
            placeholder="Message the assistant…"
            className="flex-1 resize-none rounded-lg border border-[var(--color-border-subtle)] bg-surface-muted px-3 py-2 text-sm text-brand-navy placeholder:text-brand-gray focus:outline-none disabled:cursor-not-allowed"
          />
          <button type="button" className="btn-primary text-sm" disabled>
            Send
          </button>
        </div>
        <p className="mt-2 text-center text-xs text-brand-gray">
          Chat is a preview — messaging is coming soon.
        </p>
      </div>
    </div>
  );
}

function AssistantBubble({ children }: { children: React.ReactNode }) {
  return (
    <div className="max-w-[85%] self-start rounded-2xl rounded-tl-sm bg-surface-muted px-4 py-2.5 text-sm leading-relaxed text-brand-navy">
      {children}
    </div>
  );
}

function UserBubble({ children }: { children: React.ReactNode }) {
  return (
    <div className="max-w-[85%] self-end rounded-2xl rounded-tr-sm bg-brand-blue px-4 py-2.5 text-sm leading-relaxed text-white">
      {children}
    </div>
  );
}
