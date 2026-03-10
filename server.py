from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/proxy', methods=['POST'])
def proxy_request():
    # Get the JSON data from the request
    data = request.get_json()
    
    # Process the data here (for example, forwarding it to another service)
    # This is a placeholder for your actual logic

    # Return a sample response
    return jsonify({'message': 'Request received', 'data': data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)