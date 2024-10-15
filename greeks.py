import numpy as np
import math
import operator
from scipy.stats import norm
from utils import normal_cdf, normal_pdf, d

def delta(s, x, r, sigma, tau, option_type):
    d1 = d(s, x, r, sigma, tau)
    if option_type == 'call':
        return normal_cdf(d1)
    elif option_type == 'put':
        return normal_cdf(d1) - 1
    

def gamma(s, x, r, sigma, tau):
    d1 = d(s, x, r, sigma, tau)
    return normal_pdf(d1) / (s * sigma * np.sqrt(tau))

def vega(s, x, r, sigma, tau):
    d1 = d(s, x, r, sigma, tau)
    return s * normal_pdf(d1) * np.sqrt(tau)


def theta(s, x, r, sigma, tau, option_type):
    d1 = d(s, x, r, sigma, tau)
    d2 = d(s, x, r, sigma, tau, operator=operator.sub)
    if option_type == 'call':
        theta_value = (- (s * normal_pdf(d1) * sigma) / (2 * np.sqrt(tau))
                       - r * x * np.exp(-r * tau) * normal_cdf(d2))
    elif option_type == 'put':
        theta_value = (- (s * normal_pdf(d1) * sigma) / (2 * np.sqrt(tau))
                       + r * x * np.exp(-r * tau) * normal_cdf(-d2))
    return theta_value


def rho(s, x, r, sigma, tau, option_type):
    d2 = d(s, x, r, sigma, tau, operator=operator.sub)
    if option_type == 'call':
        return x * tau * np.exp(-r * tau) * normal_cdf(d2)
    elif option_type == 'put':
        return -x * tau * np.exp(-r * tau) * normal_cdf(-d2)
    

