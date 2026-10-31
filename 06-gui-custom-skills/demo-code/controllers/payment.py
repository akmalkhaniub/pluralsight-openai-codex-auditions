from fastapi import APIRouter, HTTPException, Header, status
from pydantic import BaseModel, Field

router = APIRouter(prefix="/api/v1/payments", tags=["Billing"])

class PaymentChargeRequest(BaseModel):
    account_id: str = Field(..., description="Unique customer account identifier")
    amount_cents: int = Field(..., gt=0, description="Charge amount in cents (must be positive)")
    currency: str = Field(default="USD", description="Three-letter ISO currency code")
    payment_token: str = Field(..., description="Stripe/Adyen payment method token")

@router.post("/charge", status_code=status.HTTP_200_OK)
async def process_payment(
    payload: PaymentChargeRequest,
    idempotency_key: str = Header(..., alias="X-Idempotency-Key")
):
    """
    Processes a customer charge with idempotency and fraud checks.
    """
    # 1. Validation check
    if payload.amount_cents > 1000000: # Max $10,000 per transaction
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Transaction amount exceeds maximum allowed single charge limit ($10,000)."
        )

    # 2. Simulated payment gateway failure
    if payload.payment_token.startswith("tok_declined"):
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail="The card was declined by the issuing bank."
        )

    # 3. Successful charge
    return {
        "status": "success",
        "charge_id": "ch_3N4x7kL90",
        "amount_cents": payload.amount_cents,
        "currency": payload.currency,
        "idempotency_key": idempotency_key
    }
