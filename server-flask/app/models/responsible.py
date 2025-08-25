from app.database import db

class Responsible(db.Model):
    __tablename__ = 'responsible'

    id_responsible = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def to_dict(self):
        return {
            'id': self.id_responsible,
            'name': self.name
        }