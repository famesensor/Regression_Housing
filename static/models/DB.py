from server import db

class Data(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.Integer)
    bedroom = db.Column(db.Integer)
    carspots = db.Column(db.Integer)
    type_p = db.Column(db.String(20))
    region = db.Column(db.String(20))
    year = db.Column(db.Integer)

    def __init__(self, notes):
        self.room = notes[0]
        self.bedroom = notes[1]
        self.carspots = notes[2]
        self.type_p = notes[3]
        self.region = notes[4]
        self.year = notes[5]

    def __repr__(self):
        return '<Data %r>' % self.notes