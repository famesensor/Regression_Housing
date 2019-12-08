from app import db

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
    date = db.Column(db.Integer)
    price_predict = db.Column(db.Float)

    def __init__(self, detail):
        self.room = detail[0]
        self.bedroom = detail[3]
        self.bathroom = detail[4]
        self.buildarea = detail[6]
        self.carspots = detail[5]
        self.type_p = detail[9]
        self.distance = detail[2]
        self.region = detail[10]
        self.councilarea = detail[7]
        self.age = detail[8]
        self.date = detail[1]
        self.price_predict = detail[11]

    def __repr__(self):
        return '<Data %r>' % (self.room, self.bedroom,
        self.bathroom,
        self.buildarea,
        self.carspots,
        self.type_p,
        self.distance,
        self.region,
        self.councilarea,
        self.age,
        self.date,
        self.price_predict)