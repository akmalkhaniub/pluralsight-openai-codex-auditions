# Bookstore discount specification

Implement DiscountEngine.calculate_total(order_amount).

- Inputs in this lesson are nonnegative Decimal values with at most two decimal places.
- Below $100, charge the original amount.
- At $100 or more, apply a 10% discount. There is no second tier and no coupon.
- Round the final total to two decimal places using ROUND_HALF_UP.
- Return a Decimal and preserve the public method signature.
- Invalid input handling, tax and currency conversion are outside this lesson.

Examples: $99.99 costs $99.99; $100 costs $90; $100.01 costs $90.01.
Rounding: $100.05 times 0.90 is $90.045, which rounds to $90.05.

Run: python -m unittest -v test_discounts
