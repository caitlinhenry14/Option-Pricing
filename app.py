from flask import Flask, render_template, request
from pricing import option_price, monte_carlo_option_price
from greeks import delta, gamma, vega, theta, rho

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    s = float(request.form['s'])
    x = float(request.form['x'])
    r = float(request.form['r'])
    sigma = float(request.form['sigma'])
    tau = float(request.form['tau'])
    option_type = request.form['option_type']
    mode = request.form['mode']

    if mode == 'price':
        result = option_price(s, x, r, sigma, tau, option_type)
    elif mode == 'greeks':
        result = {
            "Delta": delta(s, x, r, sigma, tau, option_type),
            "Gamma": gamma(s, x, r, sigma, tau),
            "Vega": vega(s, x, r, sigma, tau),
            "Theta": theta(s, x, r, sigma, tau, option_type),
            "Rho": rho(s, x, r, sigma, tau, option_type)
        }
    else:
        result = "Invalid mode. Please select 'price' or 'greeks'."

    return render_template('result.html', result=result, mode=mode)

if __name__ == '__main__':
    app.run(debug=True)