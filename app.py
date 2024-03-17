from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from requests import post, get
from flask import request
import random
import string
import os 
from dotenv import dotenv_values
import base64
import json
from forms import SearchForm 

config = dotenv_values(".env")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'cant_tell_you'  

# Spotify API credentials
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_API_BASE_URL = 'https://api.spotify.com/v1/'
SPOTIFY_REDIRECT_URI = 'motify.com%0A'


# Function to get Spotify access token
def get_spotify_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    auth_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" :  "Basic " + auth_base64,
        "Content-type" :   "application/x-www-form-urlencoded"
        }
    auth_data = {
        'grant_type': 'client_credentials'
        }
    result = post(auth_url, headers=headers, data=auth_data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token 

def get_auth_header(token):
    return {"Authorization": "Bearer "  + token}

# Function to search for an artist
def artist_search(artist_name, token):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query 
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("no artist with this name exist...")
        return None
    artist_id = json_result[0]["id"]
    return json_result[0]

# Function to generate a random string for state
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        artist_name = form.artist_name.data
        access_token = get_spotify_token()
        result = artist_search(artist_name, access_token)

        if result:
            artist_id = result['id']
            return redirect(url_for('get_top_tracks', artist_id=artist_id, token=access_token))
        else:
            flash('No artists found.', 'error')
            return redirect(url_for('error', error_message='No artists found.'))

    return render_template('index.html', form=form)

@app.route('/top-tracks/<artist_id>')
def get_top_tracks(artist_id):
    token = request.headers.get('Authorization')  
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)

    try:
        json_result = result.json()
    except json.JSONDecodeError as e:
        return None

    if 'tracks' in json_result:
        tracks = json_result['tracks']
        return tracks
    else:
        return None

# Error route
@app.route('/error/<error_message>')
def error(error_message):
    return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
