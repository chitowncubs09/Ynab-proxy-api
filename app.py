from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

YNAB_TOKEN = os.getenv("YNAB_TOKEN")
BASE_URL = "https://api.youneedabudget.com/v1"
BUDGET_ID = "853af48c-8dac-43ec-9c6f-082233ffe068"

headers = {
    "Authorization": f"Bearer {YNAB_TOKEN}"
}

@app.route("/budgets", methods=["GET"])
def get_budgets():
    response = requests.get(f"{BASE_URL}/budgets", headers=headers)
    return jsonify(response.json())

@app.route("/budgets/<budget_id>/accounts", methods=["GET"])
def get_accounts(budget_id):
    response = requests.get(f"{BASE_URL}/budgets/{budget_id}/accounts", headers=headers)
    return jsonify(response.json())

@app.route("/budgets/<budget_id>/transactions", methods=["GET"])
def get_transactions(budget_id):
    response = requests.get(f"{BASE_URL}/budgets/{budget_id}/transactions", headers=headers)
    return jsonify(response.json())

@app.route("/budgets/<budget_id>/categories", methods=["GET"])
def get_categories(budget_id):
    response = requests.get(f"{BASE_URL}/budgets/{budget_id}/categories", headers=headers)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
