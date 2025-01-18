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
    

@app.get('/api/v1/participants/{event_id}')
def read_participants(event_id: int):
    

@app.post('/api/v1/participants/', response_model= participants.Participant_pydantic)
def create_participant(participant: participants.Participant_pydantic):
   

@app.get('/api/v1/events/{event_id}')
def read_event(event_id: int):
    

@app.post('/api/v1/events/', response_model= events.Event_pydantic)
def create_event(event: events.Event_pydantic):
   


    

