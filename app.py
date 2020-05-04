from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/movies")
def list_movies():
    with open("movies.txt", "r") as file:
        movie_list = file.readlines()

    return "".join(movie_list)

if __name__ == "__main__":
    app.run()
