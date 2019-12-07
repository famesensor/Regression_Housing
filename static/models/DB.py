from server import db

class Data(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.Integer)
    bedroom = db.Column(db.Integer)
    bathroom = db.Column(db.Integer)
    buildarea = db.Column(db.Float)
    carspots = db.Column(db.Integer)
    type_p = db.Column(db.String(20))
    distance = db.Column(db.Float)
    region = db.Column(db.String(20))
    councilarea = db.Column(db.Integer)
    age = db.Column(db.Integer)
    year = db.Column(db.Integer)
    price_predict = db.Column(db.Float)

    def __init__(self, data):
        self.room = data[0]
        self.bedroom = data[1]
        self.bathroom = data[]
        self.buildarea = data[]
        self.carspots = data[2]
        self.type_p = data[3]
        self.distance = data[]
        self.region = data[4]
        self.councilarea = data[]
        self.age = data[]
        self.year = data[5]
        self.price_predict = data[]

    def __repr__(self):
        return '<Data %r>' % self.price_predict