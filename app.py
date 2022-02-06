from flask import Flask, render_template, request
# from server import start
# from client import *

app = Flask(__name__)
app.run(debug=True, use_debugger=False, use_reloader=False)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    return render_template('index.html')
  else:
    return render_template('index.html')
    # start()
