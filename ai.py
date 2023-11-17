import cv2
from PIL import Image

image_path = 'cat.jpg'

image = cv2.imread(image_path)


cat_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalcatface_extended.xml')

cat_face = cat_face_cascade.detectMultiScale(image)

print(cat_face)

glasses = Image.open('glasses.png')
cat =  Image.open(image_path)

cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")

for (x, y, width, height) in cat_face:
    glasses = glasses.resize((width, int(height/3)))
    cat.paste(glasses, (x, int(y+height/4)), glasses)
    cat.save("cat_with_glasses.png")
    cat_with_glasses = cv2.imread("cat_with_glasses.png")
    cv2.imshow("Cat with glasses", cat_with_glasses)
    cv2.rectangle(image, (x, y), (x+width, y+height), (0,0,255), 3)

cv2.imshow("Cat", image)

cv2.waitKey()