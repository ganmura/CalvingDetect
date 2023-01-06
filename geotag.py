# add geolocation into EXIF file

from GPSPhoto import gpsphoto

# load image
image_path = '/home/user/Nextcloud/calving_mechanism/sfm/test_img/2021-04-01_13-03-04.jpg'
img = gpsphoto.GPSPhoto(image_path)

# coordinate to be added
# this is for camera 2
x, y, z = -73.0008552918434, -49.5343764023182, 553.646411272728
dx, dy, dz = 1.45E-07, 1.47E-07, 0.01652554737507

# image size reduced??
info = gpsphoto.GPSInfo((x,y), alt=int(z))
img.modGPSData(info, 'C2.jpg')
