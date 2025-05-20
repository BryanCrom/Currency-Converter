from config import app
from flask import request, jsonify
from converter import exchange_currency

@app.route("/", methods=["POST"])
def receive_input():
    current_currency = request.json.get("currentCurrency")
    current_amount = request.json.get("amount")
    new_currency = request.json.get("newCurrency")

    if not current_currency or not current_amount or not new_currency:
        return jsonify({"message": "You must enter a current currency, an amount, and a new currency to exchange into"}), 400

    return jsonify(exchange_currency(current_currency, current_amount, new_currency))

def give_output():
    print()


if __name__ == "__main__":
    app.run(debug=True)

