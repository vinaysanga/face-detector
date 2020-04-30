from cv2 import cv2, data
import math, sys, numpy
import os

def proc(imagePath):
	#Getting the image path from the system arguments
	fileName = imagePath.split('/')[-1]

	#Converting the image to grayscale for better luminiscence detection
	image = cv2.imread(imagePath)
	image2 = numpy.copy(image)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	print(f'#### Image size: {image.shape[1]}x{image.shape[0]}')

	#Adding the haar cascade for detecting the faces
	faceCascade = cv2.CascadeClassifier(
		data.haarcascades + "haarcascade_frontalface_default.xml")
	faces = faceCascade.detectMultiScale(
		gray, scaleFactor = 1.1,
		minNeighbors = 3, minSize=(image.shape[0]//15,image.shape[0]//15)
	)

	print(f'#### Found {len(faces)} faces.')

	#For marking the rectangles on found faces and cropping the faces
	count = 1
	folder_path = os.path.join(os.getcwd(),fileName.split('.')[0])
	os.mkdir(folder_path)
	os.chdir(folder_path)
	for (x, y, w, h) in faces:
		face_pixels = image[y:y + h, x:x + w] 
		print(f'x={x}; y={y}; w={w}; h={h}')
		if cv2.imwrite(f'face_{count}.JPG', face_pixels) :
			print(f'#### Saved face {count} / {len(faces)} locally. Size: {w}x{h}')
		cv2.rectangle(image2, (x, y), (x+w, y+h), (0,255,255), math.ceil(image.shape[0]/360))
		count += 1

	if cv2.imwrite(f'facedetect_{fileName}', image2):
		print("#### Image faces_detected.jpg written to filesystem..")

	os.chdir('..')		

if __name__ =='__main__':
	for i in range(1, len(sys.argv)):
		proc(sys.argv[i])	
