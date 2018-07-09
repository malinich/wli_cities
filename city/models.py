from pymongo import IndexModel, ASCENDING
from umongo import Document, fields, EmbeddedDocument

from ..app import MetaBaseTemplate


class Point(EmbeddedDocument, metaclass=MetaBaseTemplate):
    latitude = fields.FloatField()
    longitude = fields.FloatField()


class City(Document, metaclass=MetaBaseTemplate):
    __collection__ = 'cities'

    geonameid = fields.IntegerField(required=True)
    code_name = fields.StringField(required=True)
    iso_name = fields.StringField()
    count_journeys = fields.IntegerField(required=True, missing=0)
    count_articles = fields.IntegerField(required=True, missing=0)
    points = fields.ListField(fields.EmbeddedField(Point), required=True)

    class Meta:
        indexes = [IndexModel([('geonameid', ASCENDING),
                              ('code_name', ASCENDING)], unique=True)]
