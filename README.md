# face-detector

This is a Python script for detecting the faces present in an image. It is just a wrapper over the haar classifier from OpenCV library.
The script will detect the faces, crop them up and save them in a folder having name matching the image-name.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites
These packages must be present in order for the script to work
```
numpy 1.18.1
opencv-python 4.2.0.34
```

### Installing
Follow the steps below:

Step 1: Clone or download the repository.
```
git clone https://github.com/vinaysanga/face-detector.git
cd face-detector
```
Step 2: Install the requirements.txt with pip.
```
pip install -r requirements.txt
```
Step 3: Specify the absolute file path of the image(s) as follows:

For single images -
```
python3 facedetect.py /path/to/the/file
``` 
e.g.
```
python3 facedetect.py /home/vinay/Desktop/TestImgs/Img1.jpg
```

OR

For all images --
```
python3 facedetect.py /path/*.jpg
```
e.g.
```
python3 facedetect.py /home/vinay/Desktop/TestImgs/*.jpg
```

**Detected faces(cropped) and a marked image(original image with faces marked with rectangle) will be saved in folders named as image name(e.g. Img1) in 'face-detect' folder.**

## Some extras:
* If the detector is detecting too many false faces then try to increase ``` minNeighbors=3``` to ```minNeighbors=4 or 5``` in facedetect.py.
* Alternatively, you can also increase ```scaleFactor=1.1`` upto ```scaleFactor=1.3``` in the facedetect.py file.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
