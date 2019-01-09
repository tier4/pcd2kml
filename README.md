# pcd2kml  

Convert polygon written in point cloud file (.pcd) to kml file.



##Install  

`pip install pcd2kml`

you also need to install [pyproj](https://github.com/jswhit/pyproj)

##Usage  


```
import pcd2kml
pcd2kml.create_kml_polygon("input.pcd", "output.kml", ref=3)
```
