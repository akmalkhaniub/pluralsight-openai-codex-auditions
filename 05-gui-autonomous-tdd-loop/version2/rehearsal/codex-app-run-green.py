from decimal import Decimal, ROUND_HALF_UP

class DiscountEngine:
    def calculate_total(self, order_amount: Decimal) -> Decimal:
        """Return the total for a nonnegative, cent-precision Decimal amount."""
        total = order_amount
        if order_amount >= Decimal("100.00"):
            total = order_amount * Decimal("0.90")
        return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
