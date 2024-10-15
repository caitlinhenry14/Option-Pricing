from datetime import datetime
import math
import operator

def time_to_expiry(expiry_date):
    """
    Calculate time to expiry of option expressed as fraction of year.

    Args:
        expiry_date (str): Expiry date in format 'dd/mm/yyyy'

    Returns:
        float: Fraction of year until expiry
    """
    expiry_date_lst = list(map(int, expiry_date.split('/')))
    dd, mm, yyyy = expiry_date_lst
    expiry = datetime(yyyy, mm, dd, 23, 59, 59)
    now = datetime.now()

    return (expiry - now).days / 365.0


def normal_pdf(x):
    """
    Probability density function of a standard normal distribution.

    Args:
        x (float): Input value

    Returns:
        float: PDF value
    """
    return math.exp(-x**2 / 2) / math.sqrt(2 * math.pi)


def normal_cdf(x):
    """
    Cumulative distribution function of a standard normal distribution.

    Args:
        x (float): Input value

    Returns:
        float: CDF value
    """
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0


def d(s, x, r, sigma, tau, operation=operator.add):
    """
    Calculate d1 or d2 in the Black-Scholes model.

    Args:
        s (float): Stock price
        x (float): Strike price
        r (float): Risk-free rate
        sigma (float): Volatility
        tau (float): Time to expiration in years
        operation (function): operator.add for d1 or operator.sub for d2

    Returns:
        float: Value of d1 or d2
    """
    numerator = math.log(s / x) + operation(r, (sigma ** 2) / 2) * tau
    denominator = sigma * math.sqrt(tau)
    return numerator / denominator