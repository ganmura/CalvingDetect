# image registration
# register all images into the fist image

import cv2
from matplotlib import pyplot as plt

#crop image with ROI
# create mask of bedrock.

fn1 = './2021-04-01_13-03-04.jpg'
fn2 = './2021-04-01_14-01-45.jpg'
#img 1
img = cv2.imread(fn1)


bgr_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img1 = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)

#img 2
img = cv2.imread(fn2)
bgr_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img2 = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)

del img, bgr_img

# Create SURF object. You can specify params here or later.
# Here I set Hessian Threshold to 400
# SURF is not open yet?
sift = cv2.xfeatures2d.SIFT_create(400)
kp, des = sift.detectAndCompute(gray_img1,None)

# this class only works for SURF
# sift.setHessianThreshold(50000)
img2 = cv2.drawKeypoints(gray_img1,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()

# SURF

# MSAC
