package com.generator.Generator;

public class MiddleSquareWeylSequenceRNG implements RandomNumberGenerator {
    private long seed;
    private final long weylSequence = 0xb5ad4eceda1ce2a9L;
    private long counter = 45346;

    public long nextRandom(){
        seed *= seed; // Square the seed
        seed += (weylSequence * counter++); // Add the Weyl sequence step
        seed = (seed >> 16) & 0xFFFFFFFFL; // Extract the middle digits and ensure positive result
        return seed;
    }

    public String generate(int length,long s){
        seed = s;
        StringBuilder bitSequence = new StringBuilder(length);
        while (bitSequence.length() < length) {
            long randomNumber = nextRandom();
            for (int i = 0; i < 32 && bitSequence.length() < length; i++) { // Extracting 32 bits from each number
                bitSequence.append((randomNumber >> i) & 1);
            }
        }
        return bitSequence.toString();
    }
}
