from app import db

class internal_user(db.Model):
    u_id = db.Column(db.Integer, primary_key=True)
    s_ID = db.Column(db.String(64), index=True, unique=True)
    user_type = db.Column(db.Integer)
    email = db.Column(db.String(64), index=True, unique=True)
    phone = db.Column(db.String(10), index=True, unique=True)
    department = db.Column(db.String(64),index=True)
    password = db.Column(db.String(128))
    def __repr__(self):
        return '<User %r>' % (self.email)

class customer(db.Model):
    c_id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), index=True, unique=True)
    phone = db.Column(db.String(10), index=True, unique=True)
    password = db.Column(db.String(128))
    fname = db.Column(db.String(64), index=True, unique=False)
    lname = db.Column(db.String(64), index=True, unique=False)
    gender = db.Column(db.Integer)
    address = db.Column(db.String(64), index=True, unique=False)
    state = db.Column(db.String(2), index=True, unique=False)
    city = db.Column(db.String(64), index=True, unique=False)
    zip = db.Column(db.String(5), index=True, unique=False)
    date_of_birth =db.Column(db.DateTime)
    # fishing, runing , bicyling, jogging

    def __repr__(self):
        return '<customer %r>' % (self.fname)