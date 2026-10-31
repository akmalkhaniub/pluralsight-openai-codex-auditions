from decimal import Decimal, ROUND_HALF_UP

class DiscountEngine:
    def calculate_total(self, order_amount: Decimal) -> Decimal:
        """Apply 10% off at $100 and round the final total half up."""
        multiplier = (
            Decimal("0.90") if order_amount >= Decimal("100.00") else Decimal("1.00")
        )
        return (order_amount * multiplier).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
