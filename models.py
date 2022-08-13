



#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#


# # import json
# # from xmlrpc.client import DateTime
# # import dateutil.parser
# # import babel
# from flask import Flask, render_template, request, Response, flash, redirect, url_for
# from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
# # import logging
# # from logging import Formatter, FileHandler
# # from flask_wtf import Form
# # from forms import *
# from flask_migrate import Migrate
# # from datetime import datetime, timezone




# # app = Flask(__name__)
# moment = Moment(app)
# # app.config.from_object('config')
db = SQLAlchemy()
# migrate = Migrate(app, db)
# db.init_app(app)


class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    city = db.Column(db.String(120), nullable = False)
    state = db.Column(db.String(120), nullable = False)
    address = db.Column(db.String(120)) 
    phone = db.Column(db.String(120) ) 
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # I added the the following to the venue
    num_upcoming_shows = db.Column(db.Integer)
    num_past_shows = db.Column(db.Integer)
    genres = db.Column(db.String(500))
    website = db.Column(db.String(500))
    seeking_talent = db.Column(db.String(20)) 
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='venue', lazy='dynamic')
  
    

    def __repr__(self):
      return f'<Venue {self.id}, {self.name}, {self.city}, {self.state}, {self.address}, {self.phone}, {self.image_link}, {self.facebook_link}, {self.genres}, {self.num_past_shows}, {self.num_upcoming_shows}, {self.website}, {self.seeking_description}, {self.seeking_talent}>'
    

    # TODO: implement any missing fields, as a database migration using Flask-Migrate (Done)

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    city = db.Column(db.String(120), nullable = False)
    state = db.Column(db.String(120), nullable = False)
    phone = db.Column(db.String(120)) 
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # I added the the following to the artist
    upcoming_shows_count = db.Column(db.Integer)
    past_shows_count = db.Column(db.Integer)
    website = db.Column(db.String(500))

    seeking_venue = db.Column(db.String(10)) 
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='artist', lazy='dynamic')
    

    def __repr__(self):
      return f'<Venue {self.id}, {self.name}, {self.city}, {self.state}, {self.phone}, {self.image_link}, {self.facebook_link}, {self.genres}, {self.website}, {self.seeking_description}, {self.seeking_venue}>'
    


    # TODO: implement any missing fields, as a database migration using Flask-Migrate (Done)

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration (Done).
class Show(db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    start_time = db.Column(db.DateTime(timezone=True))
