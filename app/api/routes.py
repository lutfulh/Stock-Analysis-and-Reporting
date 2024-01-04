
from flask import Blueprint, request, jsonify
from app.services.openai_service import get_gpt3_response
from app.services.financial_service import get_financial_data
from app.services.financial_service import get_symbol_from_name
from app.services.analysis import process_financial_data
from app.services.analysis import create_analysis_prompt


api = Blueprint('api', __name__)

@api.route('/gpt3', methods=['POST'])
def gpt3():
    data = request.get_json()
    prompt = data['prompt']
    response = get_gpt3_response(prompt)
    return jsonify(response)

@api.route('/analyze', methods=['POST'])
def analyze_stock():
    data = request.get_json()
    company_name = data.get('name')  # Assuming 'name' is the key for company names

    try:
        symbol = get_symbol_from_name(company_name)
        if not symbol:
            return jsonify({'error': 'Stock symbol not found for the given company name'}), 404

        financial_data = get_financial_data(symbol)
        simple_return, date = process_financial_data(financial_data)
        prompt = create_analysis_prompt(symbol, simple_return, date)

        analysis = get_gpt3_response(prompt)
        return jsonify({'analysis': analysis}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
