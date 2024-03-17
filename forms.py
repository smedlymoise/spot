from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SearchForm(FlaskForm):
    artist_name = StringField('Artist Name')
    submit = SubmitField('Search')

class TopTracksForm(FlaskForm):
    artist_id = StringField('Artist ID')
    submit = SubmitField('Get Top Tracks')
