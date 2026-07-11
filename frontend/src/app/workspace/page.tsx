import type { Metadata } from "next";
import { ChatPanel } from "@/components/ChatPanel";
import { PreviewPanel } from "@/components/PreviewPanel";

export const metadata: Metadata = {
  title: "Workspace — Prelegal",
  description:
    "Draft your document by chatting with the assistant while the live preview updates.",
};

/**
 * Document workspace (PL-3): two-column layout with the chat on the left and
 * the live document preview on the right. Layout/mockup only — no logic yet.
 */
export default function WorkspacePage() {
  return (
    <div className="container-page py-8">
      <div className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight text-brand-navy">
          Document workspace
        </h1>
        <p className="mt-1 text-sm text-brand-gray">
          Chat with the assistant on the left; your document takes shape on the
          right.
        </p>
      </div>

      <div className="grid gap-6 lg:grid-cols-2 lg:items-stretch">
        <div className="h-[36rem] lg:h-[calc(100vh-16rem)]">
          <ChatPanel />
        </div>
        <div className="h-[36rem] lg:h-[calc(100vh-16rem)]">
          <PreviewPanel />
        </div>
      </div>
    </div>
  );
}
