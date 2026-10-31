import pytest
from discount_service import DiscountEngine

def test_no_discount_under_threshold():
    """Orders under $100 receive 0% discount."""
    engine = DiscountEngine()
    result = engine.calculate_discount(order_amount=85.00, coupon_code=None)
    assert result["discount_amount"] == 0.00
    assert result["final_amount"] == 85.00
    assert result["applied_tier"] == "NONE"

def test_tier_one_volume_discount():
    """Orders between $100 and $499.99 receive a 10% volume discount."""
    engine = DiscountEngine()
    result = engine.calculate_discount(order_amount=250.00, coupon_code=None)
    assert result["discount_amount"] == 25.00
    assert result["final_amount"] == 225.00
    assert result["applied_tier"] == "TIER_1_10_PERCENT"

def test_tier_two_volume_discount():
    """Orders of $500 or more receive a 20% volume discount."""
    engine = DiscountEngine()
    result = engine.calculate_discount(order_amount=600.00, coupon_code=None)
    assert result["discount_amount"] == 120.00
    assert result["final_amount"] == 480.00
    assert result["applied_tier"] == "TIER_2_20_PERCENT"

def test_coupon_stacking_and_rounding():
    """
    Coupon 'SAVE15' adds an extra $15 discount after tier discount.
    Amounts must be rounded to two decimal places.
    """
    engine = DiscountEngine()
    # $150 -> 10% discount = $15. Subtotal = $135. Coupon 'SAVE15' -> $15 off = $120.
    result = engine.calculate_discount(order_amount=150.00, coupon_code="SAVE15")
    assert result["discount_amount"] == 30.00
    assert result["final_amount"] == 120.00
    assert result["applied_coupon"] == "SAVE15"
