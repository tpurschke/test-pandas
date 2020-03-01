#!/usr/bin/python
import pandas as pd
import yaml
#import sys


def find_zones_without_valid_areas(zonelist, arealist):
    zones_without_area = []
    for area in zonelist.area:
        a = str(area)
        assert isinstance(area, object)
        #        sys.stdout.write('area: ' + area + "\n")
        if area not in arealist.id.values:
            #            print(area)
            #            print('broken ref')
            zones_without_area.append(area)
    return zones_without_area


def find_duplicate_area_ids(area_list):
    area_ids = area_list.id.values
    area_ids.sort()
    doubles = []
    old = None
    for i, elem in enumerate(area_ids):
        if i != 0:
            if elem == old:
                doubles.append(elem)
                old = None
                continue
        old = elem
    return doubles

# TODO: implement checks:
# no duplicate area ids
# no duplicate area ids
# no duplicate area names
# no duplicate zone ids


with open('zones.yaml', 'r') as f:
    zone_list = pd.json_normalize(yaml.safe_load(f)['zones'])

with open('areas.yaml', 'r') as f:
    area_list = pd.json_normalize(yaml.safe_load(f)['areas'])

dangling_zones = find_zones_without_valid_areas(zone_list, area_list)
if len(dangling_zones) > 0:
    print('ERROR: found zones without area')
    print(dangling_zones)

duplicate_areas = find_duplicate_area_ids(area_list)
if len(duplicate_areas) > 0:
    print('ERROR: found duplicate area ids')
    print(duplicate_areas)

# check_area_refs(area_dataMap['areas'], zone_dataMap['zones'])
