#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int main () {
  for(int sine = 0; sine < 15; sine++){
   double data[18][9][2];
   int dataSize = 0;
   cout << sine  << endl;
   for(int file = 0; file <= 17; file++){
     ifstream inputFile;
     string inputFilePath;
     if(file < 9){
      inputFilePath = "./S"+ to_string(sine + 1) +"/ordered/S"+ to_string(sine + 1) +"Pi"+ to_string(file)  +".txt";
     // cout << "P" << sine + 1<<  endl;
     }else{
      inputFilePath = "./S"+ to_string(sine + 1) +"/ordered/S"+ to_string(sine + 1) +"Vi"+ to_string(file - 9)  +".txt";
    //  cout << "V" << sine + 1<< endl;
     }

     inputFile.open(inputFilePath);
        if (!inputFile.is_open()) {
            cout << "入力ファイルを開けませんでした。" << endl;
            return 1;
        }

        // 出力ファイルを開く

      string line;
      dataSize = 0;
      while(getline(inputFile, line)){
        stringstream ss(line);
        string cell;
      //  vector<string> cells;
        int j = 0;

        // カンマ区切りの各要素を取得
        while (ss >> cell){
            // 要素に+1をして出力ファイルに書き込む
            double value = stod(cell);
            data[file][dataSize][j] = value;
            j ++;
        }
      //cout << j  << endl;
   //   cout << data[file][dataSize][0] << " " << data[file][dataSize][1] <<  " " << dataSize<<endl;
        dataSize ++;
      }
    //  cout << file << endl;
    //  cout << "next" << endl;
      inputFile.close();
    }

    
    double interpDataP[9][88][2];
    double interpDataV[9][128][2];//補間されたデータ用
    
    for(int h = 0; h <= 17; h++){
      int count = 0;
      ofstream outputFile;

      string outputFilePath;
      if(h < 9){
        outputFilePath = "./S"+ to_string(sine + 1) +"/interpolated/S"+ to_string(sine + 1) +"Pi"+ to_string(h) +"interP.txt";
      }else{
        outputFilePath = "./S"+ to_string(sine + 1) +"/interpolated/S"+ to_string(sine + 1) +"Vi"+ to_string(h - 9) +"interP.txt";
      }

      outputFile.open(outputFilePath);
      if (!outputFile.is_open()) {
          cout << "出力ファイルを開けませんでした。" << endl;
          return 1;
      }
      double diffData;
      for(int i = 0; i < dataSize - 1; i++){
        if(h < 9){//Vの場合、
            for(int k = 0; k < 11; k++){
                for(int j = 0; j < 2; j++){
                  diffData = (data[h][i + 1][j] - data[h][i][j]) / 11; //配列の隣同士の差分
                    if(j == 0){
                      interpDataP[h][k + i * 11][j] = data[h][i][j] + diffData * k;
                    }else{
                      interpDataP[h][k + i * 11][j] = data[h][i][j] + diffData * k;
                    }
                 }
                // cout << interpData[h][k + i * 11][0] << " "  << interpData[h][k + i * 11][1] << endl;
                 outputFile << interpDataP[h][k + i * 11][0] << " "  << interpDataP[h][k + i * 11][1] <<" " <<endl;
                 cout << count << endl;
                 count ++;
            }

         
        }else{//Pの場合、
           for(int k = 0; k < 16; k++){
                for(int j = 0; j < 2; j++){
                  diffData = (data[h][i + 1][j] - data[h][i][j]) / 16; //配列の隣同士の差分
                    if(j == 0){
                      interpDataV[h][k + i * 16][j] = data[h][i][j] + diffData * k;
                    }else{
                      interpDataV[h][k + i * 16][j] = data[h][i][j] + diffData * k;
                    }
                 }
                // cout << interpData[h][k + i * 16][0] << " "  << interpData[h][k + i * 16][1] << endl;
                 outputFile << interpDataV[h][k + i * 16][0] << " "  << interpDataV[h][k + i * 16][1] <<" " << endl;
                 cout << count << endl;
                 count ++;
           }
        }
          //  cout << dataSize << endl;
      //   cout << "next" << endl;
      }


   //   cout << "nextfile" << endl;
      // 行の末尾のカンマを削除して改行を書き込む
      //outputFile.seekp(-2, ios_base::end);
      outputFile << endl;
      // ファイルを閉じる
      outputFile.close();
   }
      // outputFile.close();
      cout << "nextSINE" << endl;
 }
 return 0;
}
