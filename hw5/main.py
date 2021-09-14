import flask
favTvShows = ['Breaking Bad', 'Normal People', 'Avatar the Last Airbender', 'The Boys', 'Cowboy Bebop']

app = flask.Flask(__name__)

@app.route('/')
def index():
	return flask.render_template("index.html", length = len(favTvShows), favTvShows = favTvShows)

app.run(
debug=True
)
