import cv2
import numpy as np
img1 = cv2.imread('lemur.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('flag.png', cv2.IMREAD_COLOR)

h , w, c = img1.shape
h2, w2, c2 = img2.shape
xor_img = cv2.bitwise_xor(img1, img2)
cv2.imwrite('xor_image.png', xor_img)
# print(h, w, c)
# print(h2, w2, c2)

# cv2.imshow('Lemur', img1)
# cv2.imshow('Flag', img2)
# cv2.waitKey(0)