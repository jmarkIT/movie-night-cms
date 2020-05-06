from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/movies")
def list_movies():
    with open("movies.txt", "r") as file:
        movie_list = "".join(file.readlines())

    return movie_list

@app.route("/sorted_movies")
def list_sorted_movies():
    with open("movies.txt", "r") as file:
        movie_list = file.readlines()

    movie_list.sort()
    sorted_movie_list = "".join(movie_list)
    return sorted_movie_list

if __name__ == "__main__":
    app.run()
