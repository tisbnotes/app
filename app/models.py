from datetime import datetime
from app import db


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_name = db.Column(db.String(64), index=True, unique=True)
    display_name = db.Column(db.String(64))
    path = db.Column(db.String(64), index=True, unique=True)
    updates = db.relationship('Update', backref='subject', lazy='dynamic')

    def __repr__(self):
        return '<Subject ' + self.display_name + ', ' + str(self.id_name) + ', at ' + self.path + '>'


class Update(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_id_name = db.Column(db.String(64), db.ForeignKey('subject.id_name'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    text = db.Column(db.String(256))

    def __repr__(self):
        return '<Update for subject ' + str(self.subject) + ' at ' + str(self.timestamp) + ': ' + self.text + '>'
