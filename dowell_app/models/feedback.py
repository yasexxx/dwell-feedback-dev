from app import mongodb
import datetime
from mongoengine import signals

class Feedback(mongodb.Document):
    feedback_id = mongodb.SequenceField(unique=True)
    si_number = mongodb.StringField(max_length=200, required=True)
    date = mongodb.StringField(required= True)
    project_number = mongodb.StringField(max_length=150, required=True)
    name = mongodb.StringField(max_length=200, required=True)
    phone = mongodb.IntField(required=True)
    email = mongodb.StringField(required=True)
    dowellID = mongodb.IntField( required=True)
    country = mongodb.StringField(required=True)
    role = mongodb.StringField(required=True)
    q01 = mongodb.IntField(max_length=100, required=True)
    q02 = mongodb.IntField(max_length=200, required=True)
    q03 = mongodb.IntField(required=True)
    q04 = mongodb.IntField(required=True)
    q05 = mongodb.IntField( required=True)
    q06 = mongodb.IntField(required=True)
    q07 = mongodb.IntField(required=True)
    q08 = mongodb.IntField(max_length=100, required=True)
    q09 = mongodb.IntField(max_length=200, required=True)
    q10 = mongodb.IntField(required=True)
    q11 = mongodb.IntField(required=True)
    q12 = mongodb.IntField( required=True)
    q13 = mongodb.IntField( required=True)
    q14 = mongodb.IntField( required=True)
    total = mongodb.IntField( required=True)
    percentage = mongodb.FloatField( required=True)
    feedback1 = mongodb.StringField( required=True)
    feedback2 = mongodb.StringField( required=True)
    updated_at = mongodb.DateTimeField(default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    created_at = mongodb.DateTimeField(default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    def to_json(self):
        return {
                "feedback_id": self.feedback_id,
                "si_number": self.si_number,
                "date": self.date,
                "project_number": self.project_number,
                "name": self.name,
                "phone": self.phone,
                "email": self.email,
                "dowellID": self.dowellID,
                "country": self.country,
                "role": self.role,
                "q01": self.q01,
                "q02": self.q02,
                "q03": self.q03,
                "q04": self.q04,
                "q05": self.q05,
                "q06": self.q06,
                "q07": self.q07,
                "q08": self.q08,
                "q09": self.q09,
                "q10": self.q10,
                "q11": self.q11,
                "q12": self.q12,
                "q13": self.q13,
                "q14": self.q14,
                "total": self.total,
                "percentage": self.percentage,
                "feedback1": self.feedback1,
                "feedback2": self.feedback2,
                "total": self.total,
                "created_at": self.created_at,
                "updated_at": self.updated_at,
                }
    
    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

signals.pre_save.connect(Feedback.pre_save, sender=Feedback)