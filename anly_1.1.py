#coding:utf-8連続ではない
# 1分足を5分足にまとめる。

import csv   #csvモジュールをインポートする
import os

# 入力ファイルの読込
r = open('INPUT/AUDJPY_20150501.csv', 'rb')

# 配列に格納
dataReader = csv.reader(r)
next(dataReader)    # ヘッダーだけ消す
header = ['date','O','H','L','C']

# 出力ファイルの設定
w = open('OUTPUT/AUDJPY_20150501.csv','wb')
writer = csv.writer(w, lineterminator='\n')
writer.writerow(header)
for row in dataReader:
    writer.writerow(row)
    print row[0] , row[2]
    # ↑ここ！(๑╹ω╹๑ )
    
r.close()
w.close()
