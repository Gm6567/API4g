from pyproj import Transformer
from django.db import connection, close_old_connections

_transformer = Transformer.from_crs("EPSG:2154", "EPSG:4326", always_xy=True)

# get longitude and latitude from x and y 
def lamber93_to_gps(x, y):
    lon, lat = _transformer.transform(x, y)
    return lon, lat

def get_nearest_operators(*args):
    close_old_connections()
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT operator_name,
       		BOOL_OR(is_2g AND ST_DWithin(
                ST_SetSRID(ST_MakePoint(long, lat), 4326)::geography,
                ST_SetSRID(ST_MakePoint(%s, %s), 4326)::geography,
                %s
            )) AS has_2g,
       		BOOL_OR(is_3g AND ST_DWithin(
                ST_SetSRID(ST_MakePoint(long, lat), 4326)::geography,
                ST_SetSRID(ST_MakePoint(%s, %s), 4326)::geography,
                %s
            )) AS has_3g,
       		BOOL_OR(is_4g AND ST_DWithin(
                ST_SetSRID(ST_MakePoint(long, lat), 4326)::geography,
                ST_SetSRID(ST_MakePoint(%s, %s), 4326)::geography,
                %s
            )) AS has_4g
			FROM public."addressApplication_operatortable"
			GROUP BY operator_name
            """, args)
        rows = cursor.fetchall()
    return {operator: {"2G" : has_2g, "3G": has_3g, "4G": has_4g} 
        	for operator, has_2g, has_3g, has_4g in rows}