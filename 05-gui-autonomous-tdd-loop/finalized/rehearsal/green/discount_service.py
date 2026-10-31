from decimal import Decimal, ROUND_HALF_UP

class DiscountEngine:
    def calculate_total(self, order_amount: Decimal) -> Decimal:
        """Return the total for a nonnegative, cent-precision Decimal amount."""
        if order_amount >= Decimal("100.00"):
            return (order_amount * Decimal("0.90")).quantize(
                Decimal("0.01"), rounding=ROUND_HALF_UP
            )
        return order_amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
