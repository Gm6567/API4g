import asyncio
import httpx
import re
from adrf.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from addressApplication.functions import lamber93_to_gps, get_nearest_operators

GEOCODE_URL = "https://data.geopf.fr/geocodage/search"


async def _resolve_one(client: httpx.AsyncClient, key: str, query: str):
    try:

        r = await client.get(GEOCODE_URL, params={"q": query, "limit": 1})
        r.raise_for_status()
        features = r.json().get("features") or []
        if not bool(re.findall(r'\b\d{5}\b', query)):
           features = []
        print(features)
        if not features:
            return key, {"error": "no result"}

        props = features[0]["properties"]
        lon, lat = lamber93_to_gps(props["x"], props["y"])

        cover = await asyncio.to_thread(
            get_nearest_operators,
            lon, lat, 30000,   # 2G
            lon, lat,  5000,   # 3G
            lon, lat, 10000    # 4G
        )
        return key, cover

    except Exception as exc:
        return key, {"error": str(exc)}

@api_view(["POST"])
async def adress4GView(request):
    response_data = {}
    if not isinstance(request.data, dict):
        return Response({"error": "Payload must be a json object"}, 
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            tasks = [
                _resolve_one(client, k, request.data[k])
                for k in request.data
            ]
            results = await asyncio.gather(*tasks, return_exceptions=False)

        for key, value in results:
            response_data[key] = value

        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as exc:
        return Response({"error": str(exc)}, 
                        status=status.HTTP_400_BAD_REQUEST)