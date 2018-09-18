from app import db


class SampleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<SampleModel {}>'.format(self.id)
