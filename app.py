from flask import Flask, request, jsonify
import sys
import io

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    user_code = request.json['code']

    # Capture the output of the code
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    try:
        exec(user_code)
        output = new_stdout.getvalue()
    except Exception as e:
        output = f"Error: {str(e)}"

    sys.stdout = old_stdout

    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)
