#include <vector>
#include <iostream>

using namespace std;


vector<int> twoNumberSum(vector<int> array, int targetSum){
    vector<int> sum_array;
    for(int  i = 0; i < array.size(); i++){
        for(int j = i+1; j < array.size(); j++){
            if(arra[i] + array[j] == targetsum){
                sum_array.push_back(array[i]);
                sum_array.push_back(array[j]);
            }
        }
    }
    return sum_array;
}