from server.app import db

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)

    # Relationships
    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')