# artist_search.py

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
import requests

search_artist_route = Blueprint('search_artist_route', __name__)

class ArtistSearchForm(FlaskForm):
    artist_name = StringField('Artist Name', validators=[InputRequired()])
    submit = SubmitField('Search Artist')

def get_spotify_token():
    # Function to get Spotify access token (same as before)
    # ...

 def search_artist(artist_name, access_token):
    # Function to search for an artist (same as before)
    # ...

  @search_artist_route.route('/search-artist', methods=['GET', 'POST'])
  def search_artist_view():
    form = ArtistSearchForm()

    if form.validate_on_submit():
        artist_name = form.artist_name.data
        access_token = get_spotify_token()
        artist_info_result = search_artist(artist_name, access_token)

        if 'artists' in artist_info_result and 'items' in artist_info_result['artists']:
            artists = artist_info_result['artists']['items']
            return render_template('search_artist.html', artists=artists)
        else:
            flash('No artist with this name exists. Try again.', 'error')
            return redirect(url_for('error', error_message='No artist with this name exists. Try again.'))

    return render_template('search_artist_form.html', form=form)
