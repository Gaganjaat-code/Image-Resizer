import cv2

#configurable parameters
source = "download.jpeg"
destination = 'newimage.png'
scale_percent = 50

src = cv2.imread(source,cv2.IMREAD_UNCHANGED)
#cv2.imshow("tittle",scr)

# percentage by which the image is resized

# Calculate the 50 percentage of original dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# resizem image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination,output)
#cv2.waitKeyt(0)