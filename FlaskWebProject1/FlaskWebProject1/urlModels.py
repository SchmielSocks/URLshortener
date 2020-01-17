from app import db

class Url(db.Model):
    url = db.Column(db.String(128), index=True, unique=True)
    shortenedUrl = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<URL {}>'.format(self.url)