#include "WELL.h"
#include <stdio.h> //printf

unsigned int * STATE;
unsigned int   sIdx;
unsigned short W  = 32;
unsigned short R  = 16;
unsigned short P  = 0;
unsigned short M1 = 13;
unsigned short M2 = 9;
unsigned short M3 = 5;
unsigned int   GENERATE_SIZE = 1;
unsigned int * SEED;

int main(int argc, char const *argv[]){

    // ARGUMENTS
    // argv[1]:                 GENERATE SIZE, how many numbers to generate
    // argv[2] .. argv[argc-2]: SEED, argc nubers to place in seed 

    if(argc-1 == 0){ GENERATE_SIZE = 1; }
    else if(argc-1 == 1){ GENERATE_SIZE = atoi(argv[1]); }
    else if(argc-1 >= R && argc-1 <= R+1){

        if(argc-1 == R+1){ GENERATE_SIZE = atoi(argv[1]); }
        
        SEED = (unsigned int*)malloc( R*sizeof(unsigned int) );
        for(int i=0; i<R; i++){
            SEED[i] = atoi(argv[i + argc - R]);
        }   
    }
    else{
        fprintf(stderr, "(!) wrong num of args, expecter %d or %d, got %d\n",R,R+1,argc-1);
        fprintf(stderr, "(!) try: <generate size> <seed value1> <seed value2> .. <seed value%d>",R);
        exit(EXIT_FAILURE);
    }

    STATE = initSTATE(R,W,SEED,R, &sIdx);
    // printf("INIT ");logDev(R,STATE,&sIdx);
    for(int i=0;i<GENERATE_SIZE;i++){ unsigned int num = WELL512a(R,W,P,STATE,&sIdx,M1,M2,M3); 
        printf("%u\n",num);
        // printf("%3d. ",i+1);logDev(R,STATE,&sIdx);
    }

    free(STATE);
    STATE = NULL;
    free(SEED);
    SEED = NULL;

    return 0;
}