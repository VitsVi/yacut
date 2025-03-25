from datetime import datetime
import string, random

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(256), nullable=False)
    timestamp = db.Column(
        db.DateTime,
        index=True,
        default=datetime.utcfromtimestamp
    )

    def get_unique_short_id(self, length:int=6):
        """Генерация уникального короткого идентификатора случайной длины"""

        characters = string.ascii_letters + string.digits
        self.short = ''.join(random.choice(characters) for _ in range(length))
        return self.short