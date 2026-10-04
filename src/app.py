"""
Main application module
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Welcome to CI/CD Pipeline Project',
        'status': 'success'
    })


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'running'
    })


@app.route('/api/v1/data')
def get_data():
    """Sample API endpoint"""
    return jsonify({
        'data': [1, 2, 3, 4, 5],
        'count': 5
    })


if __name__ == '__main__':
    print('SERVICE RUNNING')
    app.run(host='0.0.0.0', port=8000, debug=False)
