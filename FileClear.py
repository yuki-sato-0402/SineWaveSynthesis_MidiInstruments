
for Velocity in range(9):
    #リストの中から辞書型を順番に取得。(一つのインデックスを取得)
         
     # ファイルを書き込みモードで開く
    for Sine in range(15):
    # ファイル名を設定 (例: output1.txt, output2.txt, ...)
        file_name = f'S{Sine+1}/S{Sine+1}V{Velocity+1}.txt'
        #ファイルを書き込みモードで開く
        with open(file_name, 'w') as file:
            # 辞書のキーと値をファイルに書き込む
            file.write("")          
          