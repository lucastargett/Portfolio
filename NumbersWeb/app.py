from flask import Flask, request, jsonify, render_template
from mpmath import mp
import numpy as np
import math

app = Flask(__name__)

def fibonacci_numpy(n):
    fib_seq = np.zeros(n, dtype=int)
    fib_seq[0], fib_seq[1] = 0, 1
    for i in range(2, n):
        fib_seq[i] = fib_seq[i-1] + fib_seq[i-2]
    return fib_seq

def primefactorise(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/numbers')
def numbers_page():
    return render_template('numbers.html')

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    n = int(request.args.get('n'))
    result = fibonacci_numpy(n).tolist()  # Convert numpy array to list
    return jsonify(result)

@app.route('/primefactorise', methods=['GET'])
def primefactor():
    n = int(request.args.get('n'))
    result = primefactorise(n)
    return jsonify(result)

@app.route('/is_prime', methods=['GET'])
def prime():
    n = int(request.args.get('n'))
    result = is_prime(n)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)