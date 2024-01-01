
import os

def delete_txt_files(directory_path):
   try:
        # ルートディレクトリ内のサブディレクトリを取得
        subdirectories = [d for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]
        
        files1 = os.listdir(directory_path)
        
        for file in files1:
                if file.endswith(".txt"):
                    file_path = os.path.join(directory_path, file)
                    os.remove(file_path)
                    print(f"削除: {file_path}")

        # 各サブディレクトリ内の.txtファイルを削除
        for subdir in subdirectories:
            subdir_path = os.path.join(directory_path, subdir)
            files2 = os.listdir(subdir_path)
            
            for file in files2:
                if file.endswith(".txt"):
                    file_path = os.path.join(subdir_path, file)
                    os.remove(file_path)
                    print(f"削除: {file_path}")

        print("すべての.txtファイルを削除しました。")

   except Exception as e:
        print(f"エラーが発生しました: {e}")

# ディレクトリのパスを指定
target_directories = ["./pythonTxt", "./S1", "./S2", "./S3", "./S4", "./S5", "./S6", "./S7", "./S8", 
"./S9", "./S10", "./S11", "./S12", "./S13", "./S14", "./S15", "Joined"]

# 関数を呼び出し
for directory in target_directories:
    delete_txt_files(directory)