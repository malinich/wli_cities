import pymongo
import tornado

from city.models import City
from handlers import BaseHandler
from utils import Routers


@Routers("/")
class CityList(BaseHandler):
    async def get(self, *args, **kwargs):
        blogs = await City.find({})
        self.write(blogs)

    async def post(self, *args, **kwargs):
        data = tornado.escape.json_decode(self.request.body)
        city_data = City(**data)
        city = await city_data.commit()
        self.write("%s" % city)


@Routers("/top")
class CityTop(BaseHandler):
    schema = City.Schema

    async def get(self, *args, **kwargs):
        cursor = City \
            .find({"count_articles": {"$gte": 0}}) \
            .sort([("count_articles", pymongo.ASCENDING)]) \
            .limit(4)
        cities = await cursor.to_list(None)
        data = self.dumps(cities, True)
        self.write(data)
