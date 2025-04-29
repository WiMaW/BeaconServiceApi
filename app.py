from flask import Flask, request, jsonify, send_from_directory
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])

@app.route('/html')
def html():
    return send_from_directory('.', 'main.html')

def scrape():
    url = request.args.get('https://actioncreatorapi.onrender.com/html') #url 
    tag = request.args.get ('div') #div?
    class_name = request.args.get('element')#class name to download


    try:
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        if class_name:
            elements = soup.find_all(tag, class_=class_name)
        else:
            elements = soup.find_all(tag)
        texts = [el.get_text(strip=True) for el in elements]
        return jsonify({'status': 'ok', 'data': texts})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)