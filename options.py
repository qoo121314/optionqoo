import numpy as np


def long_call_payoff(prices, strike, premium):
    """Long call option payoff at expiration."""
    return np.maximum(prices - strike, 0) - premium


def short_call_payoff(prices, strike, premium):
    """Short call option payoff at expiration."""
    return -long_call_payoff(prices, strike, premium)


def long_put_payoff(prices, strike, premium):
    """Long put option payoff at expiration."""
    return np.maximum(strike - prices, 0) - premium


def short_put_payoff(prices, strike, premium):
    """Short put option payoff at expiration."""
    return -long_put_payoff(prices, strike, premium)
