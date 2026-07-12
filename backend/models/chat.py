"""Pydantic schemas for the AI chat.

ChatResponse is a single flat structured-output schema: every field that any of
the 11 document types might need is Optional, so one response shape supports
incremental field extraction across the whole conversation regardless of which
document the user is drafting.
"""

from typing import Literal, Optional

from pydantic import BaseModel


class Message(BaseModel):
    """A single chat message."""

    role: Literal["user", "assistant"]
    content: str


class ChatRequest(BaseModel):
    """Request body for the chat endpoint."""

    messages: list[Message]


class PartyInfo(BaseModel):
    """Details for one party to an agreement."""

    name: Optional[str] = None
    title: Optional[str] = None
    company: Optional[str] = None
    noticeAddress: Optional[str] = None


class ChatResponse(BaseModel):
    """Structured AI reply: the conversational text plus any extracted fields."""

    response: str

    # Document type detection.
    documentType: Optional[str] = None
    suggestedDocument: Optional[str] = None  # when the request is unsupported

    # Common fields shared across document types.
    purpose: Optional[str] = None
    effectiveDate: Optional[str] = None
    governingLaw: Optional[str] = None
    jurisdiction: Optional[str] = None
    fees: Optional[str] = None
    paymentTerms: Optional[str] = None

    # Mutual NDA.
    mndaTermType: Optional[Literal["expires", "continues"]] = None
    mndaTermYears: Optional[int] = None
    confidentialityTermType: Optional[Literal["years", "perpetuity"]] = None
    confidentialityTermYears: Optional[int] = None

    # Cloud Service Agreement.
    providerName: Optional[str] = None
    customerName: Optional[str] = None
    subscriptionPeriod: Optional[str] = None
    technicalSupport: Optional[str] = None

    # Pilot Agreement.
    pilotPeriod: Optional[str] = None
    evaluationPurpose: Optional[str] = None

    # Design Partner Agreement.
    programName: Optional[str] = None
    feedbackRequirements: Optional[str] = None
    accessPeriod: Optional[str] = None

    # Service Level Agreement.
    uptimeTarget: Optional[str] = None
    responseTimeCommitment: Optional[str] = None
    serviceCredits: Optional[str] = None

    # Professional Services.
    deliverables: Optional[str] = None
    projectTimeline: Optional[str] = None
    paymentSchedule: Optional[str] = None
    ipOwnership: Optional[str] = None

    # Partnership Agreement.
    partnershipScope: Optional[str] = None
    trademarkRights: Optional[str] = None
    revenueShare: Optional[str] = None

    # Software License.
    licensedSoftware: Optional[str] = None
    licenseType: Optional[str] = None
    licenseFees: Optional[str] = None
    supportTerms: Optional[str] = None

    # Data Processing Agreement.
    dataSubjects: Optional[str] = None
    processingPurpose: Optional[str] = None
    dataCategories: Optional[str] = None
    subprocessors: Optional[str] = None

    # Business Associate Agreement.
    phiDescription: Optional[str] = None
    permittedUses: Optional[str] = None
    safeguards: Optional[str] = None

    # AI Addendum.
    aiFeatures: Optional[str] = None
    trainingDataRights: Optional[str] = None
    outputOwnership: Optional[str] = None

    # Party information (common to all documents).
    party1: Optional[PartyInfo] = None
    party2: Optional[PartyInfo] = None

    # Set true once all required fields for the chosen document are gathered.
    isComplete: bool = False
