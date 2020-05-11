import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

from app import db, ma


class Search(db.Model):
    __tablename__ = 'searches'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid.uuid4)
    location = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, default=datetime.today)
    start_time = db.Column(db.String(10), nullable=False)
    end_time = db.Column(db.String(10), nullable=True)
    type = db.Column(db.String(255))
    oic = db.Column(db.String(255))
    sm = db.Column(db.String(255))
    so = db.Column(db.String(255))
    sl = db.Column(db.String(255))
    ro = db.Column(db.String(255))
    scribe = db.Column(db.String(255))
    notes = db.Column(db.Text)

    def __init__(self, location, date, start_time, type, oic, sm, so, sl, ro, scribe):
        self.location = location
        self.date = date
        self.start_time = start_time
        self.type = type
        self.oic = oic
        self.sm = sm
        self.so = so
        self.sl = sl
        self.ro = ro
        self.scribe = scribe


class SearchSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Search

    uuid = ma.auto_field()
    location = ma.auto_field()
    date = ma.auto_field()
    start_time = ma.auto_field()
    end_time = ma.auto_field()
    type = ma.auto_field()
    oic = ma.auto_field()
    sm = ma.auto_field()
    so = ma.auto_field()
    sl = ma.auto_field()
    ro = ma.auto_field()
    scribe = ma.auto_field()
    notes = ma.auto_field()


search_schema = SearchSchema()
searches_schema = SearchSchema(many=True)


def create_new_search(location, date, start_time, type, oic, sm, so, sl, ro, scribe):
    search = Search(location, date, start_time, type, oic, sm, so, sl, ro, scribe)
    db.session.add(search)
    db.session.commit()

    return search


def get_all_searches():
    return Search.query.all()


def get_search_by_uuid(uuid):
    return Search.query.filter_by(uuid=uuid).first()
