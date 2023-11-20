"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLALchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


class User(db.model):
    """Website User."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)


    @property
    def full_name(self):
        """User's full name"""
        return f"{self.first_name} {self.last_name}"
    
def connect_deb(app):
    """Connecting Database with Flask APP"""

    db.app = app
    db.init_app(app)   