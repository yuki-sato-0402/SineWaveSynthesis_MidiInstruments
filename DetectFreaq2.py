import librosa
import numpy as np
import os
import json
import matplotlib.pyplot as plt

#array1に代入する値（ファイルV1,インデックス0）と他の処理を別にする。
n_fft = 1024  # フレームサイズ
hop_length = 512  # フレームのシフトサイズ

#ファイル読み込みV----------------------------------------------------------------------------
def DefineFileV(FileNum):
    file_number = FileNum + 1
    file_name = f'SoundSources/GuitarV{file_number}.wav'
    print(file_name)
    y, sr = librosa.load(file_name, sr=None)  # sr=Noneはサンプリングレートを維持
    return y, sr
#ファイル読み込みP----------------------------------------------------------------------------
def DefineFileP(FileNum):
    file_number = FileNum - 8
    file_name = f'SoundSources/GuitarP{file_number}.wav'
    print(file_name)
    y, sr = librosa.load(file_name, sr=None)  # sr=Noneはサンプリングレートを維持
    return y, sr
#FFT処理----------------------------------------------------------------------------
def DoingFFT(timeindex,y ,sr):
    # 指定された時間範囲（例：2秒から5秒）を切り出す
    start_time = 0.50 + timeindex / 10  # 開始時間（秒）
    start_sample = int(start_time * sr)
    y_cut = y[start_sample:start_sample + n_fft]
    # STFTを計算
    stft = librosa.stft(y_cut, n_fft=n_fft, hop_length=hop_length)

    # 周波数スペクトルを計算
    magnitude_spectrum = np.abs(stft)

    #周波数
    freq_axis = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    
    #振幅
    log_absolute = np.mean(magnitude_spectrum, axis=1)
    my_dict = dict(zip(freq_axis, log_absolute))
    return my_dict

#DictArrayのkeyを初期化する。----------------------------------------------------------------------------
dict_top15 = None
dict1 = {}
array1 = []
Alldict = []
y1, sr1 = DefineFileV(0)
sorted_dict = sorted(DoingFFT(0, y1, sr1).items(), key=lambda x: x[1], reverse=True)
dict_top15 = sorted_dict[:15]
    
for key, value in dict_top15:
    array1.append(key)
    dict1[key] = value
    print(f"周波数: {key}, 振幅値: {value}")
DictArray = [
    dict1,
    {array1[0]: 'value1', array1[1]: 'value2', array1[2]: 'value1', array1[3]: 'value2', array1[4]: 'value1', array1[5]: 'value5', array1[6]: 'value1', array1[7]: 'value1', array1[8]: 'value1', array1[9]: 'value1', array1[10]: 'value1', array1[11]: 'value1', array1[12]: 'value1', array1[13]: 'value1', array1[14]: 'value1'},
    {array1[0]: 'value1', array1[1]: 'value2', array1[2]: 'value1', array1[3]: 'value2', array1[4]: 'value1', array1[5]: 'value5', array1[6]: 'value1', array1[7]: 'value1', array1[8]: 'value1', array1[9]: 'value1', array1[10]: 'value1', array1[11]: 'value1', array1[12]: 'value1', array1[13]: 'value1', array1[14]: 'value1'},
    {array1[0]: 'value1', array1[1]: 'value2', array1[2]: 'value1', array1[3]: 'value2', array1[4]: 'value1', array1[5]: 'value5', array1[6]: 'value1', array1[7]: 'value1', array1[8]: 'value1', array1[9]: 'value1', array1[10]: 'value1', array1[11]: 'value1', array1[12]: 'value1', array1[13]: 'value1', array1[14]: 'value1'},
    {array1[0]: 'value1', array1[1]: 'value2', array1[2]: 'value1', array1[3]: 'value2', array1[4]: 'value1', array1[5]: 'value5', array1[6]: 'value1', array1[7]: 'value1', array1[8]: 'value1', array1[9]: 'value1', array1[10]: 'value1', array1[11]: 'value1', array1[12]: 'value1', array1[13]: 'value1', array1[14]: 'value1'},
    {array1[0]: 'value1', array1[1]: 'value2', array1[2]: 'value1', array1[3]: 'value2', array1[4]: 'value1', array1[5]: 'value5', array1[6]: 'value1', array1[7]: 'value1', array1[8]: 'value1', array1[9]: 'value1', array1[10]: 'value1', array1[11]: 'value1', array1[12]: 'value1', array1[13]: 'value1', array1[14]: 'value1'},
    {array1[0]: 'value1', array1[1]: 'value2', array1[2]: 'value1', array1[3]: 'value2', array1[4]: 'value1', array1[5]: 'value5', array1[6]: 'value1', array1[7]: 'value1', array1[8]: 'value1', array1[9]: 'value1', array1[10]: 'value1', array1[11]: 'value1', array1[12]: 'value1', array1[13]: 'value1', array1[14]: 'value1'},
    {array1[0]: 'value1', array1[1]: 'value2', array1[2]: 'value1', array1[3]: 'value2', array1[4]: 'value1', array1[5]: 'value5', array1[6]: 'value1', array1[7]: 'value1', array1[8]: 'value1', array1[9]: 'value1', array1[10]: 'value1', array1[11]: 'value1', array1[12]: 'value1', array1[13]: 'value1', array1[14]: 'value1'},
    {array1[0]: 'value1', array1[1]: 'value2', array1[2]: 'value1', array1[3]: 'value2', array1[4]: 'value1', array1[5]: 'value5', array1[6]: 'value1', array1[7]: 'value1', array1[8]: 'value1', array1[9]: 'value1', array1[10]: 'value1', array1[11]: 'value1', array1[12]: 'value1', array1[13]: 'value1', array1[14]: 'value1'},
    ]

#DictArrayに値を代入する。----------------------------------------------------------------------------
for FileNum in range(18):
    print(FileNum)
    # 音声データの読み込みまたは録音
    if FileNum < 9:
        y2, sr2 = DefineFileV(FileNum)
    else:
        y2, sr2 = DefineFileP(FileNum)
    
    for timeindex in range(9):
        thisdict = DoingFFT(timeindex,y2 ,sr2)
        
        for i in range(len(array1)):  
            if array1[i] in thisdict :
                value = thisdict.get(array1[i])
                DictArray[timeindex][array1[i]] = value 
                   
    Alldict.insert(FileNum, DictArray)
    # スペクトルをプロット
    # plt.figure(figsize=(10, 6))
    # plt.plot(freq_axis, log_absolute , linewidth=2)
    # plt.title(f'Spectrum{timeindex}')
    # plt.xlabel('Frequency (Hz)')
    # plt.ylabel('Magnitude')
    # plt.grid()
    #plt.show()
    output_directory = "pythonTxt/"
    if FileNum < 9:
        file_name = "Velocity" + str(FileNum + 1) + ".txt"
    else:
        file_name = "Pitch" + str(FileNum - 8) + ".txt"
        
    output_file = os.path.join(output_directory, file_name)
    with open(output_file, 'a') as file:
        i = 1
        file.write("[")
        for my_dict2 in DictArray:
            float_dict = {}
            for key, value in my_dict2.items():
                try:
                    # 各値を浮動小数点数に変換
                    float_value = float(value)
                    rounded_value = str(round(float_value, 3))
                    rounded_key = round(key, 3)
                    # 新しい辞書にキーと浮動小数点数値を格納
                    float_dict[rounded_key] = rounded_value
                except ValueError:
                    # 数値に変換できない場合、エラーをキャッチ
                    print(f"Value '{value}' for key '{rounded_key}' is not a valid number.")

            dict_str = json.dumps(float_dict)
            file.write(dict_str)
            if (1 <= i and i  <= 8):
                file.write(",")
                file.write("\n")
          #  print(my_dict2)
          # print(i)
            i += 1
        file.write("]")