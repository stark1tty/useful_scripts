# useful_scripts
A small repo for sharing useful scripts I've mocked up. :)

---

## Table of Contents
- [Everyday Scripts](#everyday-scripts)
- [Misc](#misc)
- [Plants](#Plants)
    - [Plant Identification Script](#Plant-Identification-Script)
- [RSS Feeds](#RSS-feeds)


---

## Everyday Scripts
- [bullets-to-csv.py](https://github.com/stark1tty/useful_scripts/blob/main/everyday-scripts/bullets-to-csv.py) - Script to turn bullet points from a .md to a .csv. Used for note-taking.
- [webp2jpg](https://github.com/stark1tty/useful_scripts/blob/main/Misc/webp2jpg.py) - Converts folder of webp images to jpgs by renaming the extensions. I did it for the memes.

## Misc
- Just a pile of things I need to share. Don't mind the mess.

## Plants
🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿

### Plant Identification Script 
#### Keywords
#image_classification #ai #plants #ecology #plantnet #python

**23/12/13 Update**: Moving this to its own repo [here]((https://github.com/stark1tty/Plant-Image-Batch-ID)

#### Language
- Python (3.10)

##### Requirements/Packages
- os
- csv
- requests
- time

```python
pip install os csv requests time
```

#### Location
- [Plants/Identify-Plant-Images-from-Directory.ipnyb](https://github.com/stark1tty/useful_scripts/blob/main/Plants/Identify-Plant-Images-from-Directory.ipnyb)

#### Description
This script processes a directory of image files using the PlantNet API for plant identification. It saves the results to a CSV file with the specified format. The API can be found free at: https://plantnet.org/

Script is modified from an example on their github: https://github.com/plantnet

##### Tips
- I use an extension called Kutools to insert images in Excel. :)
- https://plugins.qgis.org/plugins/ImportPhotos/ for locational information on images.
- https://exiftool.org/ for more camera data and locational information.
- Filter results with confidence intervals of >0.1 to get rid of the bulk of bad matches.

## RSS feeds
- Just a folder of exports from my local FreshRSS to share. Lots of PopSci because I love it.
