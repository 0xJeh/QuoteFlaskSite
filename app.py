from flask import Flask, jsonify, render_template
import csv
import random

app = Flask(__name__)


def get_random_quote():
    try:
        with open('quotes.csv', 'r') as csv_file:
            quotes = list(csv.reader(csv_file))
            if not quotes:
                raise ValueError("No quotes found in the CSV file.")
            return random.choice(quotes)
    except FileNotFoundError:
        raise FileNotFoundError("CSV file 'quotes.csv' not found.")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

@app.route('/', methods=['GET'])
def random_quote():
    author, quote = get_random_quote()
    return render_template('index.html', author=author, quote=quote)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
