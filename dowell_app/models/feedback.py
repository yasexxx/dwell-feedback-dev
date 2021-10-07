from app import mongodb
import datetime

class Feedback(mongodb.Document):
    _id = mongodb.IntField(db_field='id', unique=True)
    name = mongodb.StringField(max_length=200, required=True)
    project_id = mongodb.StringField(max_length=100, required=True)
    email = mongodb.StringField(max_length=100, required=True)
    occupation = mongodb.StringField(max_length=200, required=True)
    feedback_1 = mongodb.StringField(max_length=50, required=True)
    feedback_2 = mongodb.StringField(max_length=50, required=True)
    total = mongodb.StringField(max_length=100, required=True)
    created_at = mongodb.DateTimeField()
    updated_at = mongodb.DateTimeField(default=datetime.datetime.now)
    
    def to_json(self):
        return {
                "id": self._id,
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