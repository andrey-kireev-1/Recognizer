# Image&Video Weapon Recognizer by [Yolov5](https://github.com/ultralytics/yolov5)
First, you can run my example code, and then train your own model and use it in the program.
## Weapon Recognizer
###### Program consist of yolov5 model, user interface form on Qt and recognize script.
To run Recognizer clone repo:
```
git clone https://github.com/andrey-kireev-1/Recognizer.git
```
Install python requirements:
```
pip install -r requirements.txt
```
Open and run *app.py*. Here you can select recognition accuracy and files (images: .jpg, .png; videos: .avi, .mp4).

![menu](https://user-images.githubusercontent.com/71035387/171960871-8ab1f746-5bad-4f83-a5f8-058b3002d839.png)

After selecting a file, object recognition will start. 4 categories of weapons can be recognized: pistol, machine gun, knife, hand grenade. For example, the input and output image could be like this:

![example](https://user-images.githubusercontent.com/71035387/171962072-b1fe5c6e-ea10-4582-93f1-7752bc3820c2.png)

And video:

![image](https://user-images.githubusercontent.com/71035387/171964385-877c6aad-d741-44ed-8680-f5f4dc0264f1.png)


Download different photos and videos with weapons and try to recognize them. Enjoy :)

## How to create your own model to recognize:
Collect a set of images with your object. Label your images (for example, with: [Make Sense](https://www.makesense.ai/)). 

Divide the collected and labeled set of images into 3 folders: **train, valid, test**. *(Further, I recommend using Google Colab, but you can also work locally.)* Create a folder in Google Drive, put the folders train, valid, test and dataset.yaml file there (replace the folder paths according to your Google Drive). 

Next: Upload on Google Drive *train_model.ipynb*, open it in Google Colab, change folders paths and run this file. The model will start training.

![train](https://user-images.githubusercontent.com/71035387/171963769-e03ccc93-4fa3-49de-812b-405e5ced0f25.png)

After completing the training of the model, download the file *best.pt* from the path /content/yolov5/runs/train/exp/weights/best.pt. Close Google Colab. Place your *best.pt* file into your cloning repo local folder. Now your program will recognize your own object.
____
###### Kireev 2022
