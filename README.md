# Sketch-Generation-with-Drawing-Process-Guided-by-Vector-Flow-and-Grayscale with Eel

Create an application in Eel that converts an image to a pencil drawing style by referring to the following site.

http://cedro3.com/ai/sketch/  

https://github.com/TZYSJTU/Sketch-Generation-with-Drawing-Process-Guided-by-Vector-Flow-and-Grayscale

## Environment

 Windows 10 environment

## Installation Procedure



Start the command prompt in administrator mode.
execute following commands.

```
git clone https://github.com/sinjorjob/sketch_app.git
cd sketch_app
mkdir venv
cd venv
python -m venv env
env\scripts\activate
cd ..
pip install -r requirements.txt
pip3 install torch==1.8.1+cpu torchvision==0.9.1+cpu torchaudio===0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
```

create folder `sketch_app\source\html\mp4`

start apps

```
cd source
python views.py
```

## Operation Procedure

1. Specify the image files (jpg, png) in the `sketch_app\source\input` folder from the screen.
2. Click the Execute button to start the image conversion process.
3. The completed image files will be stored in the following folder.
  
   `sketch_app\source\html\img` ：input, output files  
   `sketch_app\source\html\mp4` : Video of the conversion process  

**Caution**

**If you specify an image file that does not exist in the app\source\input folder, an error will occur.  
Since the program is designed to run in a CPU environment, it will take longer to process high quality images.  
The conversion process for the sample files in the /source/input folder took about 15 minutes on a CORE i7 4 Core 16GB memory environment.**

### Demo

![Eelアプリ](https://github.com/sinjorjob/sketch_app/blob/master/image/EEL_APPS_DEMO.gif)


