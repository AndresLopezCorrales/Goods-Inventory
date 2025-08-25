from app.database import db

class Items(db.Model):
    __tablename__ = 'items'

    id_item = db.Column(db.Integer, primary_key=True)
    id_location = db.Column(db.Integer, db.ForeignKey('location.id_location'), nullable=False)
    account_name = db.Column(db.String(11), nullable=False)
    description = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        return {
            'id': self.id_item,
            'id_location': self.id_location,
            'name': self.account_name,
            'description': self.description
        }