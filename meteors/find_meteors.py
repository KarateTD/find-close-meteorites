import math
import requests

def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat2) / 2) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

def get_dist(meteor):
    return meteor.get('distance', math.inf)
#Include main block to create packages later
if __name__ == '__main__':
    my_loc = my_loc = (38.8799697,-77.1067698)

    meteor_resp = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
    meteor_data = meteor_resp.json()

    for meteor in meteor_data:
        if not ('reclat' in meteor and 'retlong' in meteor): continue
        meteor['distance'] = calc_dist(float(meteor['reclat']),
                                       float(meteor['recdlong']),
                                       my_loc[0],
                                       my_loc[1])

    meteor_data.sort(key=get_dist)

    print(meteor_data[0:10])
