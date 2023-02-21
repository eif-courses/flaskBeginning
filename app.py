from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    response = requests.get('https://api.sampleapis.com/cartoons/cartoons2D')

    cartoons = response.json()
    for i in range(0, len(cartoons) - 1):
        for j in range(len(cartoons) - 1):
            if cartoons[j]['title'] < cartoons[j + 1]['title']:
                temp = cartoons[j]
                cartoons[j] = cartoons[j + 1]
                cartoons[j + 1] = temp

    return render_template('index.html', cartoons=cartoons)


@app.route('/search/<title>')
def search(title):
    response = requests.get('https://api.sampleapis.com/cartoons/cartoons2D')
    cartoons = response.json()
    for i in range(0, len(cartoons)):
        if cartoons[i]['title'] == title:
            return render_template('search.html', cartoon=cartoons[i])


@app.route('/about')
def about():
    d = "aew"
    return render_template('about.html', d=d)


if __name__ == '__main__':
    app.run()
