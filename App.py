from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/send-location', methods=['POST'])
def send_location():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    print(f"Received location: Latitude = {latitude}, Longitude = {longitude}")

    return jsonify({"status": "success", "message": "Location received"}), 200

if __name__ == '__main__':
    app.run(debug=True)
