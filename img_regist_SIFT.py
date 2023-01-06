# image registration
# register all images into the fist image

import cv2
from matplotlib import pyplot as plt
import numpy as np

#TODO crop image with ROI
# create mask of bedrock.
# learn how to mask image, process only over the bedrock.

fn1 = './2021-04-01_13-03-04.jpg'
fn2 = './2021-04-01_14-01-45.jpg'

# reference image
#img 1
img = cv2.imread(fn1)
bgr_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img1 = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)

# float image
#img 2
img = cv2.imread(fn2)
bgr_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)

del img, bgr_img

# Initiate SIFT detector
sift = cv2.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)
# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
# cv.drawMatchesKnn expects list of lists as matches.
img3 =cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img3),plt.show()

#transform image with the matched information
# image warping
# choose appropriate keypoint
ref_matched_kpts = np.float32()

# calculate homography

# project float image

# write image

