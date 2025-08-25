from app.database import db

class Location(db.Model):
    __tablename__ = 'location'

    id_location = db.Column(db.Integer, primary_key = True)
    id_responsible = db.Column(db.Integer, db.ForeignKey('responsible.id_responsible'), nullable = False)
    number_location = db.Column(db.Integer, nullable = False, unique = True)
    description = db.Column(db.String(500), nullable = True)

    def to_dict(self):
        return {
            'id': self.id_location,
            'id_responsible': self.id_responsible,
            'number_location': self.number_location,
            'description': self.description
        }