import eel
import desktop
from draw import *
from PIL import Image
import glob
import sys
import os

app_name="html"
end_point="index.html"
size=(700,600)


@eel.expose
def drawing(file_name):
    """
    引数：画面で指定したファイル名
    戻り値: 正常終了時はなし。
    　　　　file_nameがinputフォルダに存在しなかった場合はエラーメッセージ(message)
      　　　をindex.htmlへ返す。
    """
  file_name = file_name.split("\\")[-1]
  cwd = os.getcwd()
  input_file = os.path.join(cwd, "input", file_name)
  
  if os.path.isfile(input_file):
      print("変換処理を開始します。")
      n = 10  # グレースケール量子化次数
      period = 5  # 線（ストローク）幅 
      # drawing
      draw(file_name, n, period)
      print("変換処理が正常終了しました。")
  else:
      message = "ファイルが存在しません。"
      print(message)
      return message


  



@eel.expose
def test():

    print("test-ok")
    return "exit"

desktop.start(app_name,end_point,size)

