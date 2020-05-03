#include <vector>

using namespace std;

// prototyping
vector<int> twoNumberSum(vector<int> array, int);

int main(){

}


vector<int> twoNumberSum(vector<int> array, int targetSum){
    for(int  i = 0; i < array.size(); i++){
        for(int j = i; j < array.size(); j++){
            cout << "j: " << j << "i: " << i << "\n";
            
        }
    }
}