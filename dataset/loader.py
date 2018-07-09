import asyncio
import csv

from wli_cities.city.models import City, Point

f = open('RU.csv')
data = csv.DictReader(f, fieldnames=['geonameid', 'name', 'asciiname', 'alternatenames', 'latitude', 'longitude',
                                     'feature_class', "feature_code", "country_code", 'cc2', "admin1_code",
                                     "admin2_code",
                                     "admin3_code", "admin4_code", "population", "elevation", 'dem', "timezone",
                                     "date"],
                      dialect=csv.excel_tab)


async def main(data: csv.DictReader):
    for d in data:
        c = City(
            geonameid=d['geonameid'],
            code_name=d['name'],
            iso_name=d['alternatenames'].split(",")[-1]
        )
        # is_exists = await City.find_one({"geonameid": c.geonameid, "name": c.name})
        # if is_exists:
        #     c = is_exists

        c.points.append(Point(latitude=d['latitude'], longitude=d['longitude']))
        await c.commit()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(data))

