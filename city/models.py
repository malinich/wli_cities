from pymongo import IndexModel, ASCENDING
from umongo import Document, fields

from app import MetaBaseTemplate


class City(Document, metaclass=MetaBaseTemplate):
    __collection__ = 'cities'

    code = fields.StringField(required=True)
    name = fields.StringField(required=True)
    count_journeys = fields.IntegerField(required=True, missing=0)
    count_articles = fields.IntegerField(required=True, missing=0)

    class Meta:
        indexes = [IndexModel([('code', ASCENDING),
                              ('name', ASCENDING)], unique=True)]
