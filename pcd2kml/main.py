#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pcd2kml.ConcaveHull as ConcaveHull
import os, sys
import csv
import pcl
from pyproj import Proj, transform
import simplekml
from scipy.spatial import ConvexHull
import numpy as np


def translate_xy_to_lnglat(x, y, EPSG_code):
    in_proj = Proj(init=EPSG_code)
    out_proj = Proj(init='EPSG:6668')
    return transform(in_proj, out_proj, x, y)

# def get_EPSG_code(ref_number):
#     if 1 <= int(ref_number) <= 19:
#         return "EPSG:" + str(6668 + int(ref_number))
#     else:
#         return None

def create_kml_polygon(src_file, dst_file, EPSG_code):
    points = pcl.load(src_file)
    kml = simplekml.Kml()
    outerBoundaryList, pointsList = [], []
    for i in range(points.size):
        pointsList.append(points[i])
    hull = ConvexHull(pointsList)
    for i in range(len(hull.vertices)):
        lnglat = translate_xy_to_lnglat(x=points[hull.vertices[i]][0], y=points[hull.vertices[i]][1], EPSG_code="EPSG:"+str(EPSG_code))
        outerBoundaryList.append(lnglat)
    outerBoundaryList = np.array(outerBoundaryList)
    hull = ConcaveHull.concaveHull(outerBoundaryList, 3)
    for i in range(len(hull)):
        hull[i] = hull[i].tolist()
    hull = np.array(hull)
    kml.newpolygon(name="this_polygon", outerboundaryis=hull)
    kml.save(dst_file)

def get_polygon(src_file, EPSG_code):
    points = pcl.load(src_file)
    kml = simplekml.Kml()
    outerBoundaryList, pointsList = [], []
    for i in range(points.size):
        pointsList.append(points[i])
    hull = ConvexHull(pointsList)
    for i in range(len(hull.vertices)):
        lnglat = translate_xy_to_lnglat(x=points[hull.vertices[i]][0], y=points[hull.vertices[i]][1], EPSG_code="EPSG:"+str(EPSG_code))
        outerBoundaryList.append({"lng":lnglat[0], "lat":lnglat[1]})
    return outerBoundaryList