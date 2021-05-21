import pandas as pd
import re
import datetime
import os
import sys

RECEIPT_FOLDER = "./receipt"

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code   #商品コード
        self.item_name=item_name   #商品名
        self.price=price           #商品の値段
    

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]   #注文コード
        self.item_count_list=[]   #オーダー数を追加
        self.item_master=item_master   # item_masterにはItemクラスがリスト形式で格納される。


    def add_item_order(self,item_code, order_count):
        """注文数分オーダーを追加(商品コードと注文数を蓄積する)"""
        self.item_order_list.append(item_code)
        self.item_count_list.append(order_count)


    def get_item_info(self, item_master):
        """オーダー画面に表示する注文可能な製品情報を取得"""
        self.item_name = []   #製品名
        self.item_code = []   #製品コード
        self.item_price = []   #製品価格
        for item in item_master:
            self.item_name.append(item.item_name)
            self.item_code.append(item.item_code)
            self.item_price.append(item.price)
        return self.item_name, self.item_code, self.item_price


    def view_item_list(self):
        """オーダーされたすべての製品情報を取得"""
        self.order_list = []  #最終的なオーダー情報
        self.total_all_items_amount=0   #全商品の合計金額
        self.total_item_amount = 0  #商品毎の合計金額

        for order_item, count in zip(self.item_order_list, self.item_count_list):   #注文コードと注文数を1レコードずつ取り出す
            for item in self.item_master:    #商品情報が格納されているitem_masterから1つずつ商品クラス情報を取り出し
                if order_item == item.item_code:    #オーダーされた商品コードと同じ商品コードのクラスかどうかをチェックし
                    #オーダーの合計金額を計算
                    self.total_item_amount = int(item.price) * int(count)   #商品全体の合計金額
                    self.total_all_items_amount += int(item.price) * int(count)   #商品毎の合計金額
                    print(f"商品名：{item.item_name}, 価格：{item.price}, 注文数：{count},合計金額：{self.total_item_amount}円") #一致していたらその商品の名前、価格を表示
                    #self.write_receipt(f"商品名：{item.item_name}, 価格：{item.price}, 注文数：{count},合計金額：{self.total_item_amount}円")
                    #self.order_list.append(f"商品名：{item.item_name}, 価格：{item.price}, 注文数：{count},合計金額：{self.total_item_amount}円")  #オーダ情報を追記
                    self.order_list.append("商品名：{}　,価格： {:,d}円,　注文数：{},　合計金額：{:,d}円".format(item.item_name, item.price, count, self.total_item_amount ))  #オーダ情報を追記
                    break
        
        return self.order_list, "{:,d}".format(self.total_all_items_amount)   #オーダ情報と合計金額を返す


    def input_order(self, item_code, item_count, order, item_master):
        """注文を受け付ける"""

        #処理結果の格納先辞書を生成
        message = dict_message()
        #商品コードの入力値チェック（数字3桁）
        print("item_code=", item_code, type(item_code))
        if not is_only_num( item_code, r'([0-9]{3})'):
            message["type"] = "error"
            message["message"] ="3桁数字の商品コードを入力してください。"
            print(message)
            return message

        #商品コードの存在チェック
        if not is_item_code_valid(item_code, item_master):
            message["type"] = "error"
            message["message"] ="商品コードが存在しません。\n存在する商品コードを入力してください。"
            return message

        #注文数が整数かチェック
        if not is_only_num(item_count, r'([0-9]+)'):
            message["type"] = "error"
            message["message"] ="注文数は整数値を入力してください。"
            return message
        #注文数が1以上の整数かチェック
        elif not int(item_count) >= 1:
            message["type"] = "error"
            message["message"] ="注文数は1以上の整数値を入力してください。"
            return message

        #注文情報をオーダーに追加     
        order.add_item_order(item_code,item_count)    
        message["type"] = "success"
        message["message"] =""  #正常終了時は特にメッセージを利用しないため空を設定
        return message


    def input_deposit_and_change_calc(self, payment):
        """お客様からのお預かり金額を入力しお釣りを計算"""
        message = dict_message()
        self.deposit=payment  #支払金額を取得
        #支払い金額が整数かチェック
        if not is_only_num(self.deposit, r'([0-9]+)'):    
            message["type"] = "error"
            message["message"] ="支払金額は整数値を入力してください。"
            return message

        #支払い金額が1以上かチェック
        elif not int(self.deposit) >= 1:
            message["type"] = "error"
            message["message"] ="支払金額は1以上の整数値を入力してください。"
            return message
        
        self.change_money=int(self.deposit) - self.total_all_items_amount #おつりの計算

        if self.change_money >= 0:
            message["type"] = "success"
            message["message"] = "購入処理が完了しました！ <br> お預り金：{:,d}円<br> おつり：{:,d}円".format(int(self.deposit), int(self.change_money))
            return message
        else:
            message["type"] = "error"
            message["message"] ="お金が不足しています。\n 再度金額を入力してください。"
            return message


    def chk_order_status(self):
        """オーダーリストに商品が追加されているかチェック"""
        message = dict_message()
        if not self.item_order_list:
            message["type"] = "error"
            message["message"] = "商品が選択されていません。\n 先に購入する商品を選んでください。"
            return message

        if self.change_money >= 0:
            message["type"] = "success"
            message["message"] = "購入処理が完了しました！ <br> お預り金：{:,d}円<br> おつり：{:,d}円".format(int(self.deposit), int(self.change_money))
            return message

        else:
            message["type"] = "error"
            message["message"] ="お金が不足しています。\n 再度金額を入力してください。"
            return message
  

def add_item_master(csv_path):
    """
    csvのitem_master.csvを読み込んで製品マスター情報を生成
    """
    item_master=[]   #商品マスタの格納先リスト
    
    try:
        # pandasは文字列を格納するのに、objectというdtypeを用いる
        # item_codeが001->1のようになってしまうのでこれを回避
        item_master_df=pd.read_csv(csv_path,dtype={"item_code":object})
        #DataFrameを1行ずつ抽出しItemクラスを使って商品マスタのインスタンスを生成
        for index, row in item_master_df.iterrows():
            item_master.append(Item(row["item_code"], row["item_name"], row["price"]))
        print("{}件の商品データを登録しました。".format(index+1))
        print("------- マスタ登録が完了しました。 ---------")
        return item_master                    
    except Exception as e:
        print("マスタ登録処理が異常終了しました。")
        print(f"エラー内容:{e}")
        sys.exit()



#入力値の数値判定関数
def is_only_num(input, regex):
    return True if re.fullmatch(regex, input) else False


#商品マスターに存在する商品コードかどうかをチェックする関数
def is_item_code_valid(item_code, item_master):
    decision_flag  = False
    for item in item_master:  #商品マスターに入力した商品コードが存在するかチェック
        if item_code == item.item_code:
            decision_flag  = True
    return decision_flag

def dict_message():
    #処理結果を格納する空の辞書型データを返す。
    message = {"type":"", "message":""}
    return message
