import cv2

#What we are going to do
# Read image(RGB) -> Converting into HSV --> Getting Mask

def do_nothing(x):
    pass

cv2.namedWindow('Track Bars',cv2.WINDOW_NORMAL)
cv2.createTrackbar('min_blue','Track Bars', 0, 255, do_nothing)
cv2.createTrackbar('min_red', 'Track Bars', 0, 255, do_nothing)
cv2.createTrackbar('min_green','Track Bars', 0, 255, do_nothing)

cv2.createTrackbar('max_blue','Track Bars', 0, 255, do_nothing)
cv2.createTrackbar('max_red', 'Track Bars', 0, 255, do_nothing)
cv2.createTrackbar('max_green','Track Bars', 0, 255, do_nothing)


img = cv2.imread('D:\ObjectDetection\Actitvity 1\objects-to-detect.jpg')
img_resize = cv2.resize(img,(600,400))

cv2.namedWindow('OrginalImage',cv2.WINDOW_NORMAL)
cv2.imshow('OrginalImage', img_resize)


hsv_img = cv2.cvtColor(img_resize,cv2.COLOR_BGR2HSV)
cv2.namedWindow('HSVImage',cv2.WINDOW_NORMAL)
cv2.imshow('HSVImage', hsv_img)

while True:
    if cv2.waitKey(0):
        break

while True:
    min_blue = cv2.getTrackbarPos('min_blue', 'Track Bars')
    min_green = cv2.getTrackbarPos('min_green', 'Track Bars')
    min_red = cv2.getTrackbarPos('min_red','Track Bars')

    max_blue = cv2.getTrackbarPos('max_blue', 'Track Bars')
    max_green = cv2.getTrackbarPos('max_green', 'Track Bars')
    max_red = cv2.getTrackbarPos('max_red', 'Track Bars')

    mask = cv2.inRange(hsv_img,(min_blue,min_green,min_red),(max_blue,max_green,max_red))

    cv2.namedWindow('MaskImage',cv2.WINDOW_NORMAL)
    cv2.imshow('MaskImage',mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

#Perfect Result
# min_blue, min_green, min_red = 21, 222, 70
# max_blue, max_green, max_red = 176, 255, 255

print('min_blue', 'min_green', 'min_red = {0}, {1}, {2}'.format(min_blue,min_green,min_red))
print('max_blue', 'max_green', 'max_red = {0}, {1}, {2}'.format(max_blue,max_green,max_red))

