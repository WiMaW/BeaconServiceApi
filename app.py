from flask import Flask, request, jsonify, send_from_directory
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# endpoint do pobierania danych z zew stron 
# @app.route('/scrape', methods=['GET'])

# def scrape():
#     url = request.args.get('...') #url 
#     tag = request.args.get ('div') #div?
#     class_name = request.args.get('element')#class name to download


#     try:
#         html = requests.get(url).text
#         soup = BeautifulSoup(html, 'html.parser')
#         if class_name:
#             elements = soup.find_all(tag, class_=class_name)
#         else:
#             elements = soup.find_all(tag)
#         texts = [el.get_text(strip=True) for el in elements]
#         return jsonify({'status': 'ok', 'data': texts})
#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)}), 500

# endpoint do pliku html 
@app.route('/html')
def html():
    return send_from_directory('.', 'main.html')

#endpoint do pobierania i przetwarzania danych z main
@app.route('/api/dane')
def get_data():
    try:
        url = 'https://actioncreatorapi.onrender.com/html'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        
        elements = soup.find_all(class_='element')
        wynik = []

        for el in elements:
            name = el.find(class_='name')
            tekst = el.find(class_='tekst')
            image = el.find(class_='image')
            video = el.find(class_='video')
            audio = el.find(class_='audio')

            wynik.append({
                'name': name.text.strip() if name else '',
                'tekst': tekst.text.strip() if tekst else '',
                'image': image.text.strip() if image else '',
                'video': video.text.strip() if video else '',
                'audio': audio.text.strip() if audio else '',
            })

        return jsonify(wynik)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)