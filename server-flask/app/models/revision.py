from app.database import db

class Revision(db.Model): 
    __tablename__ = 'revision'

    id_revision = db.Column(db.Integer, primary_key=True)
    id_location = db.Column(db.Integer, db.ForeignKey('location.id_location'), nullable=False)
    date_time_revision = db.Column(db.DateTime, nullable=False)
    comment = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        return {
            'id': self.id_revision,
            'id_location': self.id_location,
            'date_time_revision': self.date_time_revision.isoformat(),
            'comment': self.comment
        }