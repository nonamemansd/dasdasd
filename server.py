from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='static')  # Указываем папку для статических файлов
CORS(app)  # Enable CORS for cross-origin requests

website_url = None  # Store the website URL

@app.route('/open', methods=['POST'])
def open_website():
    global website_url
    data = request.get_json()
    website_url = data.get('url')
    if website_url:
        print(f"Received website URL: {website_url}")
        return jsonify({'message': 'Website URL received successfully!'})
    else:
        return jsonify({'error': 'No URL provided'}), 400

@app.route('/get_url', methods=['GET'])
def get_website_url():
    global website_url
    if website_url:
        url = website_url
        website_url = None  # Clear the URL after sending it
        return jsonify({'url': url})
    else:
        return jsonify({'url': None})

# Добавляем маршрут для отображения index.html
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')