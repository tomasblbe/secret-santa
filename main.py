from flask import Flask, render_template, redirect
from api import get_joke, get_joke_of_day

app = Flask(__name__)

joke_text = get_joke()
joke_of_day_text = get_joke_of_day()

@app.route('/')
def hello_world():
    return render_template('base.html', joke=joke_text, joke_of_day=joke_of_day_text)

@app.route('/joke', methods=['POST'])
def joke():
    global joke_text
    joke_text = get_joke()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)