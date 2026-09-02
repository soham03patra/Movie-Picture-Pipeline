from flask import jsonify,request
from flask.views import MethodView

# Dummy database to hold movie examples
movies = {
    "123": {"title": "Top Gun: Maverick", "description": "Fighter planes"},
    "456": {"title": "Sonic the Hedgehog", "description": "Blue Sega character"},
    "789": {"title": "A Quiet Place", "description": "Scary monsters"},
}


class Movies(MethodView):

    def get(self, movie_id):
        if movie_id is None:
            # Return a list of all movies
            return jsonify({
                "movies": [
                    {"title": movie["title"], "id": movie_id}
                    for movie_id, movie in movies.items()
                ]
            })
        else:
            # Return the details of a specific movie
            movie = movies.get(str(movie_id))

            if movie is None:
                return jsonify({"error": "Movie not found"}), 404

            return jsonify({"movie": movie})