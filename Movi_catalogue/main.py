from flask import Flask, render_template
import tmdb_client
import random
from flask import request

app = Flask(__name__)

#@app.route("/")
#def homepage():
#    selected_list = request.args.get('list_type', 'popular')
#    movies = tmdb_client.get_movies_list('popular')
 #   return render_template("homepage.html", movies=movies, current_list=selected_list)

@app.route("/")
def homepage():
    selected_list = request.args.get('list_type', 'popular')
    movies = tmdb_client.get_movies_list(list_type=selected_list)['results'][:8]
    if selected_list == 'popular':
        css_button_popular='btn btn-primary'
        css_button_top_rated = css_button_upcoming = css_button_now_playing = 'btn btn-outline-primary'
    elif  selected_list == 'top_rated':
       css_button_top_rated='btn btn-primary'
       css_button_popular = css_button_upcoming = css_button_now_playing = 'btn btn-outline-primary'
    elif selected_list == 'upcoming':
        css_button_upcoming='btn btn-primary'
        css_button_popular = css_button_top_rated = css_button_now_playing = 'btn btn-outline-primary'
    elif selected_list == 'now_playing':
        css_button_now_playing='btn btn-primary'
        css_button_popular = css_button_upcoming = css_button_top_rated = 'btn btn-outline-primary'
    return render_template("homepage.html", movies=movies, current_list=selected_list, css_button_popular=css_button_popular, css_button_top_rated = css_button_top_rated, css_button_upcoming=css_button_upcoming, css_button_now_playing=css_button_now_playing)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=selected_backdrop)
