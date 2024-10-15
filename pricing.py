import math
import numpy as np
from scipy.stats import norm

def option_price(s, x, r, sigma, tau, option_type):
    """
    Black-Scholes option pricing for European options.

    Args:
        s (float): Current stock price
        x (float): Strike price
        r (float): Risk-free interest rate
        sigma (float): Volatility
        tau (float): Time to expiration in years
        option_type (str): 'call' or 'put'

    Returns:
        float: Option price
    """
    d1 = (math.log(s / x) + (r + (sigma**2) / 2) * tau) / (sigma * math.sqrt(tau))
    d2 = d1 - sigma * math.sqrt(tau)

    if option_type == 'call':
        price = s * norm.cdf(d1) - x * math.exp(-r * tau) * norm.cdf(d2)
    elif option_type == 'put':
        price = x * math.exp(-r * tau) * norm.cdf(-d2) - s * norm.cdf(-d1)
    return price

def monte_carlo_option_price(s, x, r, sigma, tau, option_type, simulations=10000):
    """
    Monte Carlo simulation to price a European option.
    
    Args:
        s (float): Current stock price
        x (float): Strike price
        r (float): Risk-free interest rate
        sigma (float): Volatility
        tau (float): Time to expiration in years
        option_type (str): 'call' or 'put'
        simulations (int): Number of simulations to run
        
    Returns:
        float: Monte Carlo estimated option price
    """
    z = np.random.standard_normal(simulations)
    stock_prices = s * np.exp((r - 0.5 * sigma**2) * tau + sigma * np.sqrt(tau) * z)
    
    if option_type == 'call':
        payoffs = np.maximum(stock_prices - x, 0)
    elif option_type == 'put':
        payoffs = np.maximum(x - stock_prices, 0)
    
    option_price = np.exp(-r * tau) * np.mean(payoffs)
    
    return option_price