# Create by Ahmadreza Anaami
import cv2;

img = cv2.imread("RES/2.jpg" , 0)
cv2.namedWindow("img")
def nothing(args):
    pass
cv2.createTrackbar("Thresh" , "img" ,0 ,500 , nothing)

while True:
    _img =  img.copy()
    Thresh = cv2.getTrackbarPos("Thresh" , "img")
    canny = cv2.Canny(img , 0 , Thresh)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(_img, contours, -1, (0, 255, 0), 2 )
    
    cv2.imshow("img", _img)
    cv2.waitKey(1)

