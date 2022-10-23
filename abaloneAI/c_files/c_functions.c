#include <iostream>

int row_length(int row){
        if (row < 5)
            return row + 5;
        else
            return 13 - row;
}