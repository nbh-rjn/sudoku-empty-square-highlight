import cv2
import numpy as np

# read img and do the usual converting so we can process further
image = cv2.imread('soduku.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

# perform closing to get rid of the numbers so we are left with just the squares
kernel = np.ones((20, 20), np.uint8)
filled_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

# place red squares on original
result_image = cv2.cvtColor(filled_image, cv2.COLOR_GRAY2BGR)
for i in range(filled_image.shape[0]):
    for j in range(filled_image.shape[1]):
        if (filled_image[i, j] == [0, 0, 0]).all():
            image[i, j] = [0, 0, 255]
cv2.imshow('result_image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
