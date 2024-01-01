import json

# テキストファイルの数
num_files = 18

# 辞書型のリストを格納するリスト
dict_list = []

for i in range(1, num_files + 1):
    if i <= 9:
        filename = f"pythonTxt/Velocity{i}.txt"
    else :
        filename = f"pythonTxt/Pitch{i - 9}.txt"
        
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            file_contents = file.read()
            # JSONデータを辞書型のリストにパース
            data = json.loads(file_contents)
            dict_list.append(data)
    except FileNotFoundError:
        print(f"{filename} が見つかりませんでした。")
    except json.JSONDecodeError:
        print(f"{filename} は有効なJSONデータを含んでいません。")
        
    #print(dict_list,"\n")
#ファイルの辞書型を含むリストを順番に取得。
FileNum = 1
for items1 in dict_list:
    #リストの中から辞書型を順番に取得。(一つのインデックスを取得)
    Index = 0
    for items2 in items1:
         
     # ファイルを書き込みモードで開く
        Sine = 0
        for key, value in items2.items():
        # ファイル名を設定 (例: output1.txt, output2.txt, ...)
            if FileNum <= 9:
                file_name = f'S{Sine+1}/S{Sine+1}V{FileNum}.txt'
            else:
                file_name = f'S{Sine+1}/S{Sine+1}P{FileNum - 9}.txt'
                                                                                                                    
            #ファイルを書き込みモードで開く
            with open(file_name, 'a') as file:
                # 辞書のキーと値をファイルに書き込む
                print(key,value,file_name)
                file.write(f'{Index}, {key} {value};\n') 
            Sine += 1            
        Index += 1                
            # print(dict1)       
  # print(FileNum) 
    print(items1)      
    FileNum += 1

