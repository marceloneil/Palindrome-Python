from flask import Flask, render_template
from palindromes import Palindromes

def set_palindromes_list(data):
    'Set value of palindromes_list'
    global palindromes_list 
    palindromes_list = data

def set_palindromes_sum(data):
    'Set value of palindromes_sum'
    global palindromes_sum 
    palindromes_sum = str(data)

# Initializing app
app = Flask(__name__)

@app.route('/palindromes')
def list_palindromes():
    'Returns list of palindromes'
    return render_template('index.html', palindromes=palindromes_list)

@app.route('/palindromes/count')
def count_palindromes():
    'Returns number of palindromes'
    return palindromes_sum

