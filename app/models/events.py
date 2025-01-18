from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel  
from app import db
  

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    date = db.Column(db.DateTime)
    location = db.Column(db.String(120), index=True)
    max_participants = db.Column(db.Integer)
    participants = db.relationship('Participant', backref='event', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date,
            'location': self.location,
            'participants': [participant.to_dict() for participant in self.participants],
            'participant_count': self.participants.count(),
            'max_participants': self.max_participants
        }

    def __repr__(self):
        return super().__repr__()
    
class Event_pydantic(BaseModel):
    name: str
    date: datetime
    location: str
    max_participants: int