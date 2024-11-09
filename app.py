from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/mineral-price')
def mineral_price():
    data = {
        "mineral": random.choice(["Gold", "Silver", "Platinum", "Copper"]),
        "price": round(random.uniform(10, 2000), 2),  # ціна від 10 до 2000
        "currency": "USD"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
