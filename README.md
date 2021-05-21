# Sketch-Generation-with-Drawing-Process-Guided-by-Vector-Flow-and-Grayscale

以下のサイトを参考に画像を鉛筆画風に変換するアプリをEelで作成

http://cedro3.com/ai/sketch/  

https://github.com/TZYSJTU/Sketch-Generation-with-Drawing-Process-Guided-by-Vector-Flow-and-Grayscale

## Installation Procedure

Operation check: Windows 10 environment

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

create folder **sketch_app\source\html\mp4**

start apps

```
cd source
python views.py
```

## Operation Procedure

1. Specify the image files (jpg, png) in the sketch_`app\source\input` folder from the screen.
2. Click the Execute button to start the image conversion process.
3. The completed image files will be stored in the following folder.
  
   `sketch_app\source\html\img` ：input, output files
   `sketch_app\source\html\mp4` : Video of the conversion process



### Demo

![Eelアプリ](https://github.com/sinjorjob/sketch_app/blob/master/image/EEL_APPS_DEMO.gif)


