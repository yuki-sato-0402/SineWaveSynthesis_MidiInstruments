#!/bin/zsh

python_files=("DetectFreq.py" "Ordering1.py" "Ordering2.py")

cpp_files=("Interpolation.cpp" "FileMergers.cpp")

#python
for py_file in "${python_files[@]}"; do
  python3 "$py_file"
done

#C++
for cpp_file in "${cpp_files[@]}"; do
  # コンパイル
  g++ -o output_executable "$cpp_file"

  # コンパイルが成功したかチェック
  if [ $? -eq 0 ]; then
    # 実行
    ./output_executable
  else
    echo "コンパイルエラーが発生しました。"
    break
  fi
done
