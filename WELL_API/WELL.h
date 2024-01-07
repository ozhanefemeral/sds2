#include <math.h>    //pow
#include <stdio.h>   //stderr
#include <stdbool.h> //bool
#include <time.h>    //rand
#include <stdlib.h>  //rand

unsigned int Mtrx0(unsigned int value){ return 0; }

unsigned int Mtrx1(unsigned int value){ return value; }

unsigned int Mtrx2(unsigned int value, int t){
    if (t>=0)   return value >> t;
    else        return value << (-t);
}

unsigned int Mtrx3(unsigned int value, int t){
    if (t>=0) return value ^ (value >> t);
    else      return value ^ (value << (-t));
}

unsigned int Mtrx4(unsigned int value, unsigned int a, unsigned int w){
    //  x^(w-1)==1
    if (w-1==0 || value==1) return (value >> 1) ^ a;
    else                    return (value >> 1);
}

unsigned int Mtrx5(unsigned int value, int t, unsigned int b){
    if (t>=0) return value ^ ( (value << t) & b );
    else      return value ^ ( (value >> (-t)) & b );
}

// -------------------------------------------------------------------------------------------

unsigned int MaskP(unsigned int p, unsigned int w){
    return ((unsigned int)(pow(2,w)-1) ^ (unsigned int)(pow(2,p)-1));
}

unsigned int RevMaskP(unsigned int p, unsigned int w){
    return (unsigned int)(pow(2,p)-1);
}

unsigned int RotP(unsigned int p, unsigned int w, unsigned int value1, unsigned int value2){
    return ( value1 & RevMaskP(p,w) )|( value2 & MaskP(p,w) ); 
}

// -------------------------------------------------------------------------------------------

unsigned int * initSTATE(   unsigned short r, 
                            unsigned short w, 
                            unsigned int * seed, 
                            int seedSize, 
                            unsigned int * stateIndex ){

    * stateIndex = 0;

    srand(time(NULL));

    unsigned int * newState = (unsigned int*)malloc( r*sizeof(unsigned int) );

    if(seed==NULL || seedSize==0){
        for (int i=0;i<r;i++){
            newState[i] = rand();
        }
    }
    else if(seedSize!=r){
        fprintf(stderr, "(!) sizes of seed and state vector are different\n",seedSize,r);
        exit(EXIT_FAILURE);
    }
    else{
        for (int i=0;i<r;i++){
            newState[i] = seed[i];
        }
    }

    return newState;
}

unsigned int WELL512a(  unsigned short r, unsigned short w, unsigned short p, 
                        unsigned int * state, unsigned int * stateIndex, 
                        unsigned short m1, unsigned short m2, unsigned short m3 ){
    
    unsigned int z0,z1,z2,z3,z4;
    unsigned int v0     = state[ (*stateIndex)               ];
    unsigned int vm1    = state[ (*stateIndex + m1) % r      ];
    unsigned int vm2    = state[ (*stateIndex + m2) % r      ];
    unsigned int vm3    = state[ (*stateIndex + m3) % r      ];
    unsigned int vlast  = state[ (*stateIndex + r - 1) % r   ];
    unsigned int vlast2 = state[ (*stateIndex + r - 2) % r   ];

    z0 = RotP(p,w,vlast2,vlast);
    z1 = Mtrx3(v0,-16) ^ Mtrx3(vm1,-15);
    z2 = Mtrx3(vm2,11) ^ Mtrx0(vm3);
    z3 = z1 ^ z2;
    z4 = Mtrx3(z0,-2) ^ Mtrx3(z1,-18) ^ Mtrx3(z2,-28) ^ Mtrx5(z3,-5,0xda442d24);

    *stateIndex = (*stateIndex + r - 1) % r;

    state[(*stateIndex + r - 1 )%r] = vlast2 & MaskP(p,w);
    state[(*stateIndex + 1)%r ] = z3;
    state[(*stateIndex)] = z4;

    return state[*stateIndex];    
}


void logDev(unsigned short r, unsigned int * state, unsigned int * stateIndex){
    printf("S[");
    for(int i=0;i<r;i++){
        printf(" %10u ",state[(*stateIndex+i)%r]);
    }
    printf("]\tidx: %d\n",*stateIndex);
}