from opencv import cv2
img=cv2.imread("ball.jfif")

img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray_image=cv2.bitwise_not(img)

blurred=cv2.GaussianBlur(gray_image,(21,21),0)

invert_blurred=cv2.bitwise_not(blurred)

sketch_image=cv2.divide(img,invert_blurred,scale=250.0)
cv2.imwrite("ball.png",sketch_image)

cv2.waitkey(0)
cv2.destroyAllWindows()