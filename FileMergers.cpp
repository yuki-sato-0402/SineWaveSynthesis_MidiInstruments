#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;



int main () {
  string dataP[15][9][88][2];
  string dataV[15][9][128][2];
  for(int sine1 = 0; sine1 < 15; sine1++){
    
    for(int h = 0; h <= 17; h++){
     ifstream inputFile;

     string inputFilePath;
     if(h < 9){
      inputFilePath = "./S"+ to_string(sine1 + 1) +"/interpolated/S"+ to_string(sine1 + 1) +"Pi"+ to_string(h) +"interP.txt";
     }else{
      inputFilePath = "./S"+ to_string(sine1 + 1) +"/interpolated/S"+ to_string(sine1 + 1) +"Vi"+ to_string(h - 9) +"interP.txt";
     }

     inputFile.open(inputFilePath);

        if (!inputFile.is_open()) {
            cout << "入力ファイルを開けませんでした。" << endl;
            return 1;
        }
        string line;
        int index = 0;
            while(getline(inputFile, line)){
            stringstream ss(line);
            string cell;
            int j = 0;
            // カンマ区切りの各要素を取得
            while (ss >> cell) {
              // 要素に+1をして出力ファイルに書き込む
              if(h < 9){
                dataP[sine1][h][index][j] = cell;
              }else{
                dataV[sine1][h - 9][index][j] = cell;
              }
                cout << cell << " ";
                j ++;
            }
            index ++;
      }
      inputFile.close();
    }
     cout << endl;
  }
 
///////////////////////////////////////////////
  
for(int sine2 = 0; sine2 < 15; sine2++){

  //int sine2 = 1;
  ofstream outputFile;
  string pitch = "p";
  string outputFilePath1;
  outputFilePath1 = "./Joined/S"+ pitch +to_string(sine2 + 1) +"joined.txt";
   
   outputFile.open(outputFilePath1);
  for(int v = 0; v <= 8; v++){  
     
    if (!outputFile.is_open()) {
        cout << "出力ファイルを開けませんでした。" << endl;
        return 1;
    }

      outputFile << v <<  "," << " ";
     
      for(int i = 0; i < 88; i++){
          //   cout << data[sine][v][i][0] << " "  << data[sine][v][i][1]  << " ";
             outputFile << dataP[sine2][v][i][0] << " "  << dataP[sine2][v][i][1] << " ";
       }
       outputFile << ";" << endl;
       
  }

  cout << sine2 << endl; 

 outputFile.close();
}
/////////////////////////////////////////

for(int sine2 = 0; sine2 < 15; sine2++){
  ofstream outputFile;
  string velocity = "v";
  string outputFilePath2;
  outputFilePath2 = "./Joined/S"+ velocity +to_string(sine2 + 1) +"joined.txt";
 
  outputFile.open(outputFilePath2);

  for(int v = 0; v <= 8; v++){  
  
    if (!outputFile.is_open()) {
        cout << "出力ファイルを開けませんでした。" << endl;
        return 1;
    }
 
     outputFile << v <<  "," << " ";
    
      for(int i = 0; i < 128; i++){
      //       cout << data[sine][v][i][0] << " "  << data[sine][v][i][1]  << " ";
        outputFile << dataV[sine2][v][i][0] << " "  << dataV[sine2][v][i][1] << " ";
       }
       outputFile << ";" << endl;
    //   cout << "next" << endl; 
  }

  outputFile.close();

  }
return 0;
}
