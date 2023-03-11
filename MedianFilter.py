import cv2

img = cv2.imread('tasya.jpeg')
filtered = cv2.medianBlur(img, 3)
cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
