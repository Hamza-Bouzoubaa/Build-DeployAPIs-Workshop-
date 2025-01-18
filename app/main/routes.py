from flask import render_template, request  
from app.models.participants import Participant
from app.models.events import Event
from app import db

from . import bp  # Import the blueprint from this package  
  
@bp.route('/')  
def index():  
    return render_template('index.html')  


@bp.route('/register', methods=['GET', 'POST'])  
def register():  
    print(request.form)
    if request.method == 'POST':  
        name = request.form['name']  
        email = request.form['email']  
        phone = request.form['phone']  
        event_id = request.form['event_id']  
        participant = Participant(name=name, email=email, phone=phone, event_id=event_id)  
        db.session.add(participant) 
        db.session.commit()
        return render_template('index.html')
    return render_template('register.html')  

  
@bp.route('/participants')  
def participants():  
    # Get all events  
    events = Event.query.all()  
  
    # Get event_id from form data  
    event_id = request.args.get('event_id')  
  
    participants = []  
    if event_id:  
        # Get participants for the selected event  
        participants = Participant.query.filter_by(event_id=event_id).all()  
  
    return render_template('participants.html', events=events, participants=participants)  
    