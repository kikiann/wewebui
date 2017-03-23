from app import db

class Changes(db.Model):
    timestamp = db.Column(db.BigInteger, primary_key=True)
    filepath = db.Column(db.String(256))

    def __init__(self, timestamp, filepath):
        self.timestamp = timestamp
        self.filepath = filepath
