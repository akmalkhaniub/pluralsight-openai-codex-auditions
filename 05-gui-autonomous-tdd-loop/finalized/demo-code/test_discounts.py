"""Focused examples for one prepared TDD cycle. Also discoverable by pytest."""
from decimal import Decimal
import unittest
from discount_service import DiscountEngine

class DiscountTests(unittest.TestCase):
    def setUp(self):
        self.engine = DiscountEngine()

    def test_zero_order(self):
        self.assertEqual(
            self.engine.calculate_total(Decimal("0.00")), Decimal("0.00")
        )

    def test_below_threshold(self):
        self.assertEqual(
            self.engine.calculate_total(Decimal("85.00")), Decimal("85.00")
        )

    def test_one_cent_below_threshold(self):
        self.assertEqual(
            self.engine.calculate_total(Decimal("99.99")), Decimal("99.99")
        )

    def test_exactly_at_threshold(self):
        self.assertEqual(
            self.engine.calculate_total(Decimal("100.00")), Decimal("90.00")
        )

    def test_one_cent_above_threshold(self):
        self.assertEqual(
            self.engine.calculate_total(Decimal("100.01")), Decimal("90.01")
        )

    def test_larger_order(self):
        self.assertEqual(
            self.engine.calculate_total(Decimal("150.00")), Decimal("135.00")
        )

    def test_no_second_tier(self):
        self.assertEqual(
            self.engine.calculate_total(Decimal("500.00")), Decimal("450.00")
        )

    def test_half_cent_rounds_up(self):
        self.assertEqual(
            self.engine.calculate_total(Decimal("100.05")), Decimal("90.05")
        )

if __name__ == "__main__":
    unittest.main()
