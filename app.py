from flask import Flask, jsonify, send_from_directory
import json

app = Flask(__name__)

# Endpoint do pobierania danych JSON z pliku elements.json
@app.route('/api/elements')
def get_elements():
    try:
        with open('elements.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
