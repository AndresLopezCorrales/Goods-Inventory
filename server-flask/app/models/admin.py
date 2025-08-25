from app.database import db

class Admin(db.Model):
    __tablename__ = "admin"

    id_admin = db.Column(db.Integer, primary_key=True)
    name = db.Column (db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id_admin,
            'name': self.name,
            'password': self.password
        }