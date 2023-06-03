# useful_scripts
A small repo for sharing useful scripts I've mocked up. :)

---

## Table of Contents
- [Plants](#Plants)
    - [Plant Identification Script](#Plant-Identification-Script)

---

## Plants
🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿

### Plant Identification Script 
#### Keywords
#image_classification #ai #plants #ecology #plantnet

#### Location
Plants/Identify-Plant-Images-from-Directory.ipnyb

#### Description
This script processes a directory of image files using the PlantNet API for plant identification. It saves the results to a CSV file with the specified format. The API can be found free at: https://plantnet.org/

Script is modified from an example on their github: https://github.com/plantnet

##### Tips
- I use an extension called Kutools to insert images in Excel. :)
- https://plugins.qgis.org/plugins/ImportPhotos/ for locational information on images.
- https://exiftool.org/ for more camera data and locational information.
- Filter results with confidence intervals of >0.1 to get rid of the bulk of bad matches.
