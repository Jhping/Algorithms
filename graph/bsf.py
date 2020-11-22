#!usr/bin/python
#-*-coding:utf8-*-
import re
import unittest
import math

coordination_source = """
{name:'兰州', geoCoord:[103.73, 36.03]},
{name:'嘉峪关', geoCoord:[98.17, 39.47]},
{name:'西宁', geoCoord:[101.74, 36.56]},
{name:'成都', geoCoord:[104.06, 30.67]},
{name:'石家庄', geoCoord:[114.48, 38.03]},
{name:'拉萨', geoCoord:[102.73, 25.04]},
{name:'贵阳', geoCoord:[106.71, 26.57]},
{name:'武汉', geoCoord:[114.31, 30.52]},
{name:'郑州', geoCoord:[113.65, 34.76]},
{name:'济南', geoCoord:[117, 36.65]},
{name:'南京', geoCoord:[118.78, 32.04]},
{name:'合肥', geoCoord:[117.27, 31.86]},
{name:'杭州', geoCoord:[120.19, 30.26]},
{name:'南昌', geoCoord:[115.89, 28.68]},
{name:'福州', geoCoord:[119.3, 26.08]},
{name:'广州', geoCoord:[113.23, 23.16]},
{name:'长沙', geoCoord:[113, 28.21]},
//{name:'海口', geoCoord:[110.35, 20.02]},
{name:'沈阳', geoCoord:[123.38, 41.8]},
{name:'长春', geoCoord:[125.35, 43.88]},
{name:'哈尔滨', geoCoord:[126.63, 45.75]},
{name:'太原', geoCoord:[112.53, 37.87]},
{name:'西安', geoCoord:[108.95, 34.27]},
//{name:'台湾', geoCoord:[121.30, 25.03]},
{name:'北京', geoCoord:[116.46, 39.92]},
{name:'上海', geoCoord:[121.48, 31.22]},
{name:'重庆', geoCoord:[106.54, 29.59]},
{name:'天津', geoCoord:[117.2, 39.13]},
{name:'呼和浩特', geoCoord:[111.65, 40.82]},
{name:'南宁', geoCoord:[108.33, 22.84]},
//{name:'西藏', geoCoord:[91.11, 29.97]},
{name:'银川', geoCoord:[106.27, 38.47]},
{name:'乌鲁木齐', geoCoord:[87.68, 43.77]},
{name:'香港', geoCoord:[114.17, 22.28]},
{name:'澳门', geoCoord:[113.54, 22.19]}
"""

def get_city_info(coordination_source):

    city_location = {}
    for line in coordination_source.split("\n"):
        if line.startswith("//"):continue
        if line.strip()=="":continue
        city = re.findall("name:'(\w+)'",line)[0]
        coordination = re.findall("geoCoord:\[(\d+.\d+),\s(\d+.\d+)\]",line)[0]
        city_location[city] = (float(coordination[0]),float(coordination[1]))
    #print(len(city_location))
    return city_location

city_info = get_city_info(coordination_source)

def geo_distance(origin, destination):
    lat_ori,lng_ori= origin
    lat_des, lng_des = destination
    radius = 6371  # km
    dlng = math.radians(lng_des-lng_ori)
    dlat = math.radians(lat_des - lat_ori)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat_ori)) * math.cos(math.radians(lat_des)) *
         math.sin(dlng / 2) * math.sin(dlng / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d

def get_twocitys_distance(city1,city2):
    return geo_distance(city_info[city1],city_info[city2])

threshold = 700   # defined the threshold
from collections import defaultdict


def build_connection(city_info):
    cities_connection = defaultdict(list)
    cities = list(city_info.keys())
    for c1 in cities:
        for c2 in cities:
            if c1 == c2: continue

            if get_twocitys_distance(c1, c2) < threshold:
                cities_connection[c1].append(c2)
    return cities_connection


cities_connection = build_connection(city_info)
#print(cities_connection)
# BFS
def print_pathes(pathes):
    print(pathes)

def search_1(graph,start,destination):
    searched_citys = set()
    if destination == start:
        return [start]

    dest_path = []
    searching_pathes = [[start]]
    while searching_pathes:
        print("\n\n")
        print_pathes(searching_pathes)
        searching_path = searching_pathes.pop(0)
        print(searching_path)
        searching_city = searching_path[-1]
        print(searching_city)
        # 已经检查过的城市不再检查
        if searching_city in searched_citys: continue
        for neibor in graph[searching_city]:
            print(neibor)
            #邻居已存在路径中不在添加该邻居到路径中
            if neibor in searching_path:continue
            if destination == neibor:
                dest_path = searching_path + [neibor]
                print(dest_path)
                return dest_path
            else:
                new_path = searching_path + [neibor]
                searching_pathes.append(new_path)
        searched_citys.add(searching_city)

    return dest_path

# Optimal search using variation of BFS
def search_2(graph,start,destination,search_strategy):
    searched_cites = set()
    searching_pathes = [[start]]

    while searching_pathes:
        searching_path = searching_pathes.pop(0)

class TestBsf(unittest.TestCase):
    def setUp(self):
        print("setup:\n")

    def tearDown(self):
        print("teardown:\n")

    def test_get_city_info(self):
        self.assertEqual(\
        type(get_city_info(coordination_source)),\
        dict,\
        msg="get_city_info: return type error")

        self.assertEqual(len(get_city_info(coordination_source)),\
                         32,\
                         msg="city num error")

    def test_geo_distance(self):
        self.assertEqual(city_info["杭州"], (120.19, 30.26))
        self.assertEqual(city_info["上海"], (121.48, 31.22))
        self.assertEqual(get_twocitys_distance("杭州","上海"), 153.5185697155768)
    def test_build_connection(self):
        self.assertEqual(build_connection(city_info)["西宁"], ['兰州', '嘉峪关', '成都', '拉萨', '贵阳', '重庆', '银川'])

    def test_search_1(self):
        self.assertEqual(search_1(cities_connection,"上海", "香港"),['上海', '合肥', '香港'])
if __name__ == "__main__":
    unittest.main()