from concurrent.futures import thread
from flask import Flask, render_template, request
import threading
from .server import start_server


app = Flask(__name__)
app.run(debug=True, use_debugger=False, use_reloader=False)

@app.route('/', methods=['POST', 'GET'])
def index():
  if request.method == 'POST':
    inputted_message = request.form["ComposedMessage"]
    return render_template('index.html', past_message=inputted_message)
  else:
    return render_template('index.html')


@app.route('/messages', methods=['POST', 'GET'])
def messages():
  if request.method == 'POST':
    pass
    # Save message and username into database
    # return 200 success code message
  else:
    return render_template('index.html')

def run_server_file():
  start_server()

x = threading.Thread(target=run_server_file)
x.start()
print(threading.activeCount())
