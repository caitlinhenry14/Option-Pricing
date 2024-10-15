import argparse
from pricing import option_price, monte_carlo_option_price
from greeks import delta, gamma, vega, theta, rho
from utils import time_to_expiry

def main():
    parser = argparse.ArgumentParser(description="Option Pricing Tool")
    parser.add_argument('-s', '--s', help='float: stock price.', type=float, action='store', required=True)
    parser.add_argument('-x', '--x', help='float: strike price.', type=float, action='store', required=True)
    parser.add_argument('-r', '--r', help='float: risk-free interest rate.', type=float, action='store', required=True)
    parser.add_argument('-v', '--sigma', help='float: volatility (standard deviation of log returns).', type=float, action='store')
    parser.add_argument('-mp', '--mp', help='float: market price of option (for implied volatility).', type=float, action='store')
    parser.add_argument('-t', '--tau', help='float: time to expiration in years.', type=float, action='store')
    parser.add_argument('-ed', '--expirydate', help='str: expiry date of option in dd/mm/yyyy format.', type=str, action='store')
    parser.add_argument('-ot', '--optiontype', help='str: call or put. default: call.', type=str, default="call", action='store')
    parser.add_argument('-m', '--mode', help='str: optionprice, montecarlo, or greeks.', type=str, default="optionprice", action='store')

    args = parser.parse_args()

    s = args.s
    x = args.x
    r = args.r
    sigma = args.sigma
    option_type = args.optiontype
    mode = args.mode

    if args.tau:
        tau = args.tau
    else:
        tau = time_to_expiry(args.expirydate)

    if mode == "montecarlo":
        print("Monte Carlo Option Price:", monte_carlo_option_price(s, x, r, sigma, tau, option_type))
    elif mode == "greeks":
        print("Delta:", delta(s, x, r, sigma, tau, option_type))
        print("Gamma:", gamma(s, x, r, sigma, tau))
        print("Vega:", vega(s, x, r,))