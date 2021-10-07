from run import mongodb

class User(mongodb.Document):
    name = mongodb.StringField()
    email = mongodb.StringField()
    
    def to_json(self):
        return {
                "name": self.name,
                "email": self.email
                }