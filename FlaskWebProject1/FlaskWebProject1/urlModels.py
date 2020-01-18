from FlaskWebProject1 import db

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(128), index=True, unique=True)
    shortenedUrl = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '{} --> http://urlshortener.com/{}'.format(self.url, self.shortenedUrl)