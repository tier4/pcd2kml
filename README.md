# pcd2kml  

Get convex hull of point cloud file and make polygon in kml file.


## Install  

`pip install pcd2kml`

you also need to install [pyproj](https://github.com/jswhit/pyproj) and [pcl (Point Cloud Library)](http://www.pointclouds.org/downloads/)

## Usage  


```
import pcd2kml
pcd2kml.create_kml_polygon("input.pcd", "output.kml", ref=3) #EPSG = ref code + 6668 in Japan
```

You can see the output in Google earth.  
The output is white polygon.

![kml polygon](https://user-images.githubusercontent.com/23014935/51017159-5bce7900-15b6-11e9-93c9-60b7dd2f3dbe.png)