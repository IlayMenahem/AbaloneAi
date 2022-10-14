#include <map>
#include <iostream>
#include <cassert>
#include <string>
#include <stdlib.h>

#ifndef NUM_OF_SPACES
#define NUM_OF_SPACES = 61
#endif
//add struct (called tuple) of n integers (like a tuple).
//add struct of n tuples (like a tuple).

struct staticArray{
    int arr[];
};

struct static2DArray{
    int arr[][];
};

class board{
    private:
        char spaces[NUM_OF_SPACES];
        std::map<staticArray, static2DArray> possibleMoves3;
        std::map<staticArray, static2DArray> possibleMoves2;
        std::map<staticArray, static2DArray> possibleMoves1;
        
    public:
        /**
         * @brief Construct a new board object
         */
        board(){
            possibleMoves3[{1,2,3}] = {{0,0,0},{0,0,0},{0,0,0},{0,0,0},{0,0,0},{0,0,0}};
        }

        /**
         * @brief changes to c at index index
         * 
         * @param index 
         * @param c 
         */
        void change(int index, char c){
            spaces[index] = c;
        }

        /**
         * @brief 
         * 
         * @param indices 
         * @return true 
         */
        bool legal_tuple(int indices[]){
            
        }
}
