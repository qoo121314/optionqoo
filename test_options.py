import numpy as np
import pytest
from options import long_call_payoff, short_call_payoff, long_put_payoff, short_put_payoff

K = 9100
CALL_PREMIUM = 195
PUT_PREMIUM = 18.5
PRICES = np.arange(K - 500, K + 500)


class TestLongCall:
    def test_payoff_below_strike_is_negative_premium(self):
        # Below strike: option expires worthless, lose the premium
        prices = np.array([8000, 8500, 9099])
        payoff = long_call_payoff(prices, K, CALL_PREMIUM)
        np.testing.assert_array_equal(payoff, -CALL_PREMIUM)

    def test_payoff_at_strike(self):
        payoff = long_call_payoff(np.array([K]), K, CALL_PREMIUM)
        assert payoff[0] == -CALL_PREMIUM

    def test_payoff_above_strike(self):
        prices = np.array([K + 100, K + 500])
        payoff = long_call_payoff(prices, K, CALL_PREMIUM)
        expected = np.array([100 - CALL_PREMIUM, 500 - CALL_PREMIUM])
        np.testing.assert_array_equal(payoff, expected)

    def test_breakeven(self):
        breakeven = K + CALL_PREMIUM
        payoff = long_call_payoff(np.array([breakeven]), K, CALL_PREMIUM)
        assert payoff[0] == 0


class TestShortCall:
    def test_short_call_is_opposite_of_long_call(self):
        long_p = long_call_payoff(PRICES, K, CALL_PREMIUM)
        short_p = short_call_payoff(PRICES, K, CALL_PREMIUM)
        np.testing.assert_array_equal(short_p, -long_p)

    def test_sum_of_long_and_short_is_zero(self):
        long_p = long_call_payoff(PRICES, K, CALL_PREMIUM)
        short_p = short_call_payoff(PRICES, K, CALL_PREMIUM)
        np.testing.assert_array_equal(long_p + short_p, 0)

    def test_profit_below_strike(self):
        prices = np.array([8000, 8500, 9099])
        payoff = short_call_payoff(prices, K, CALL_PREMIUM)
        np.testing.assert_array_equal(payoff, CALL_PREMIUM)


class TestLongPut:
    def test_payoff_above_strike_is_negative_premium(self):
        prices = np.array([9101, 9500, 10000])
        payoff = long_put_payoff(prices, K, PUT_PREMIUM)
        np.testing.assert_array_equal(payoff, -PUT_PREMIUM)

    def test_payoff_at_strike(self):
        payoff = long_put_payoff(np.array([K]), K, PUT_PREMIUM)
        assert payoff[0] == -PUT_PREMIUM

    def test_payoff_below_strike(self):
        prices = np.array([K - 100, K - 500])
        payoff = long_put_payoff(prices, K, PUT_PREMIUM)
        expected = np.array([100 - PUT_PREMIUM, 500 - PUT_PREMIUM])
        np.testing.assert_array_equal(payoff, expected)

    def test_breakeven(self):
        breakeven = K - PUT_PREMIUM
        payoff = long_put_payoff(np.array([breakeven]), K, PUT_PREMIUM)
        assert payoff[0] == 0


class TestShortPut:
    def test_short_put_is_opposite_of_long_put(self):
        long_p = long_put_payoff(PRICES, K, PUT_PREMIUM)
        short_p = short_put_payoff(PRICES, K, PUT_PREMIUM)
        np.testing.assert_array_equal(short_p, -long_p)

    def test_sum_of_long_and_short_is_zero(self):
        long_p = long_put_payoff(PRICES, K, PUT_PREMIUM)
        short_p = short_put_payoff(PRICES, K, PUT_PREMIUM)
        np.testing.assert_array_equal(long_p + short_p, 0)

    def test_profit_above_strike(self):
        prices = np.array([9101, 9500, 10000])
        payoff = short_put_payoff(prices, K, PUT_PREMIUM)
        np.testing.assert_array_equal(payoff, PUT_PREMIUM)
