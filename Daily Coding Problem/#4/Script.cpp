// Example program
#include <iostream>

using namespace std;

int missing(int* arr, int len) {
    int arrtmp;

    // Find minimum positive integer
    unsigned int /*min = 4294967295, max = 0,*/ posnums = 0;
    for (int i = 0; i < len; i++) {
        arrtmp = arr[i];
        if (arrtmp > 0) {
            posnums++;/*
            if (arrtmp < min)
                min = arrtmp;
            if (arrtmp > max)
                max = arrtmp;*/
        }
    }
    int i = 0
    while ()
}

int main()
{
    int arr[12] = {-2,4,7,4,7,8,3,6,-5,0,0};

    missing(arr, 12);
}
