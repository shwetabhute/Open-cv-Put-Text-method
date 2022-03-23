import cv2
path = 'numpy.jpg'
image = cv2.imread(path)
window_name = 'Image'
font = cv2.FONT_HERSHEY_SIMPLEX
org = (70, 60)
fontScale = 1
color = (255, 0, 0)
thickness = 1
image = cv2.putText(image, 'Tutorial', org,font, fontScale, color, thickness, cv2.LINE_AA)
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
