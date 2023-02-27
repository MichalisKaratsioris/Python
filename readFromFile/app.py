
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

movie_list = [
    'Forrest Gump', 'Sleepless in Seattle',
    'Philadelphia', 'You\'ve Got Mail',
    'Apollo 13', 'The Green Mile', 'The Terminal'
]

movies = {
    1: 'Forrest Gump',
    2: 'Sleepless in Seattle',
    3: 'Philadelphia',
    4: 'You\'ve Got Mail',
    5: 'Apollo 13',
    6: 'The Green Mile',
    7: 'The Terminal',
    8: 'Cast Away'
}


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', list=movies)


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', list=movies)


@app.route('/<movie_id>', methods=['GET'])
def get_movie(movie_id):
    try:
        file_name = f"./movies/{movie_id}.txt"
        with open(file_name) as file:
            for line in file:
                elements = line.split(":")
                t = elements[0]
                d = elements[1]
            return render_template('movie.html', title=t, description=d)
    except FileNotFoundError:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
