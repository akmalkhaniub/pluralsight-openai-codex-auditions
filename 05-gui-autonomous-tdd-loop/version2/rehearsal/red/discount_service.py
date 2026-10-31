from decimal import Decimal

class DiscountEngine:
    def calculate_total(self, order_amount: Decimal) -> Decimal:
        """Return the total for a nonnegative, cent-precision Decimal amount."""
        raise NotImplementedError("Implement the bookstore discount rule.")
