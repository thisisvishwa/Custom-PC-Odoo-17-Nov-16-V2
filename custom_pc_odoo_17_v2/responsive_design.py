```python
import os
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_responsive', methods=['POST'])
def check_responsive():
    user_agent = request.headers.get('User-Agent')
    if "Mobile" in user_agent:
        return {"status": "success", "message": "Mobile device detected", "responsiveCheck": True}
    else:
        return {"status": "success", "message": "Desktop device detected", "responsiveCheck": False}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```
This Python script uses Flask and Flask-Bootstrap to create a simple web server. The server has two routes: the index route, which serves the homepage, and the check_responsive route, which checks the User-Agent header of the incoming request to determine if the request is coming from a mobile device or a desktop device. The check_responsive route returns a JSON response indicating whether the request is from a mobile device or a desktop device.