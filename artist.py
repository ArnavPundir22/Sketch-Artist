import cv2

image = cv2.imread("car.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted = 255 - gray
blur = cv2.GaussianBlur(inverted, (15, 15), 0)
inverted_blur = 255 - blur

sketch = cv2.divide(gray, inverted_blur, scale=240.0)
resize = cv2.resize(sketch, (500, 800))

cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch", resize)

key = cv2.waitKey(0) & 0xFF   # wait for a key press

if key == ord("s"):
    name = input("Enter the File name with extension: ")
    cv2.imwrite(name, resize)
    print(f"Pencil sketch saved as {name}")

elif key == ord("q"):
    print("Quit without saving.")

cv2.destroyAllWindows()
