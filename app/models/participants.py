from pydantic import BaseModel
from app import db
  
class Participant(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(64), index=True)  
    email = db.Column(db.String(120), index=True, unique=True)  
    phone = db.Column(db.String(20), unique=True)  
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))  

  
    def to_dict(self):  
        return {  
            'id': self.id,  
            'name': self.name,  
            'email': self.email,  
            'phone': self.phone  
        }  
    
    def __repr__(self):
        return super().__repr__()
    

class Participant_pydantic(BaseModel):
    name: str
    email: str
    phone: str
    event_id: int


    