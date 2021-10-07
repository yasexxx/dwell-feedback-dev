from app import mongodb
import datetime
from mongoengine import signals

class Feedback(mongodb.Document):
    feedback_id = mongodb.SequenceField(unique=True)
    name = mongodb.StringField(max_length=200, required=True)
    project_id = mongodb.StringField(max_length=100, required=True)
    email = mongodb.StringField(max_length=100, required=True)
    occupation = mongodb.StringField(max_length=200, required=True)
    feedback_1 = mongodb.IntField(required=True)
    feedback_2 = mongodb.IntField(required=True)
    total = mongodb.FloatField( required=True)
    created_at = mongodb.DateTimeField(default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    updated_at = mongodb.DateTimeField(default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    def to_json(self):
        return {
                "feedback_id": self.feedback_id,
                "name": self.name,
                "email": self.email,
                "project_id": self.project_id,
                "occupation": self.occupation,
                "feedback_1": self.feedback_1,
                "feedback_2": self.feedback_2,
                "total": self.total,
                "created_at": self.created_at,
                "updated_at": self.updated_at
                }
    
    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

signals.pre_save.connect(Feedback.pre_save, sender=Feedback)