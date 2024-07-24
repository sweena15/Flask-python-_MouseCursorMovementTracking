from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/track-mouse', methods=['POST'])
def track_mouse():
    data = request.json
    x = data.get('x')
    y = data.get('y')
    with open('mouse_log.txt', 'a') as f:
        f.write(f"Mouse Position - X: {x}, Y: {y}\n")
    return jsonify({"status": "success"})


if __name__ == '__main__':
    app.run(debug=True)
