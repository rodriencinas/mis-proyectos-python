import cv2
import glob
import os

images = glob.glob("data/sample_images/*.jpg")

os.makedirs("data/resized_images", exist_ok=True)

#print(type(images))
#print(images)

for image in images:
    img = cv2.imread(image, 0)
    cv2.imshow("Real size img", img)
    cv2.waitKey(1500)
    resized_img = cv2.resize(img, (100,100))
    cv2.imshow("Resized img", resized_img)
    cv2.waitKey(1500)
    
    filename = os.path.basename(image)
    cv2.imwrite(f"data/resized_images/resized_{filename}", resized_img)
    
    cv2.destroyAllWindows()