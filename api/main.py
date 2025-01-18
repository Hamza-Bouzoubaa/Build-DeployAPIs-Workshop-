import random
from fastapi import FastAPI, HTTPException
from app.models import participants, events
import sqlalchemy
from sqlalchemy.orm import sessionmaker



app = FastAPI()

db = sqlalchemy.create_engine('sqlite:///instance/test.db')
Session = sessionmaker(bind=db)
session = Session()

@app.get('/')
def read_root():
    return {"message": "Hello, World!"}

@app.get('/api/v1/event_list')
def read_events():
    event_list = session.query(events.Event).all()
    return {"events": [event.to_dict() for event in event_list]}

@app.get('/api/v1/participants/{event_id}')
def read_participants(event_id: int):
    participant_list = session.query(participants.Participant).filter_by(event_id=event_id).all()
    return {"participants": [participant.to_dict() for participant in participant_list]}

@app.post('/api/v1/participants/', response_model= participants.Participant_pydantic)
def create_participant(participant: participants.Participant_pydantic):
    existing_email = session.query(participants.Participant).filter_by(email=participant.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered.")

    existing_phone = session.query(participants.Participant).filter_by(phone=participant.phone).first()
    if existing_phone:
        raise HTTPException(status_code=400, detail="Phone number already registered.")
    
    participant = participants.Participant(**participant.dict())
    session.add(participant)
    session.commit()
    return participant

@app.get('/api/v1/events/{event_id}')
def read_event(event_id: int):
    event = session.query(events.Event).get(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found.")
    return event.to_dict()

@app.post('/api/v1/events/', response_model= events.Event_pydantic)
def create_event(event: events.Event_pydantic):
    event = events.Event(**event.dict())
    session.add(event)
    session.commit()
    return event


    

