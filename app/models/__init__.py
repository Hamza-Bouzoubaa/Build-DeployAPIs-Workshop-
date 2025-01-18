from app.models import participants, events
from app import db,app

import datetime
with app.app_context():
    db.drop_all()
    db.create_all()
    event1 = events.Event(name='Intro to Machine Learning', date=datetime.datetime(2025, 1, 18, 11, 0, 0), location='CRX 100', max_participants=35) 
    db.session.add(event1)
    event2 = events.Event(name='How to Build and Deploy APIs', date=datetime.datetime(2025, 1, 18, 10, 0, 0), location='CRX 101', max_participants=25)
    db.session.add(event2)
    event3 = events.Event(name='How to Master the Art of Networking', date=datetime.datetime(2025, 1, 18, 12, 0, 0), location='CRX 102', max_participants=40)
    db.session.add(event3)
    db.session.commit()

