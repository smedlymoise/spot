from flask import Blueprint, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
import requests

top_tracks_route = Blueprint('top_tracks_route', __name__)

class TopTracksForm(FlaskForm):
    artist_id = StringField('Artist ID', validators=[InputRequired()])
    submit = SubmitField('Get Top Tracks')

def get_spotify_token():
    # Function to get Spotify access token (same as before)
    # ...

 def get_top_tracks(artist_id, access_token):
    # Function to get an artist's top tracks (same as before)
    # ...

  @top_tracks_route.route('/top-tracks', methods=['GET', 'POST'])
  def top_tracks():
    print("############")
    print("############")
    print(token)
    form = TopTracksForm()

    if form.validate_on_submit():
        artist_id = form.artist_id.data
        access_token = get_spotify_token()
        top_tracks_result = get_top_tracks(artist_id, access_token)

        if 'tracks' in top_tracks_result:
            tracks = top_tracks_result['tracks']
            return render_template('top_tracks.html', artist_id=artist_id, tracks=tracks)
        else:
            flash('No top tracks found for the artist.', 'error')
            return redirect(url_for('error', error_message='No top tracks found for the artist.'))

    return render_template('top_tracks_form.html', form=form)
