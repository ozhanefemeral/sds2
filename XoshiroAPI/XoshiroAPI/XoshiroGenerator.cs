namespace XoshiroAPI
{
    public class XoshiroGenerator
    {
        public string? Generate(string seed, string size)
        {
            var finalResult = "";
            try
            {
                var sizeValue = Convert.ToInt32(size);
                var seedValue = Convert.ToUInt64(seed);
                var firstState = xorshift256_init(seedValue);
                var initialResult = xoshiro256p(firstState);

                var numerator = 10UL;

                while (finalResult.Length < sizeValue)
                {
                    var newSeed = initialResult % numerator;
                    var newState = xorshift256_init(newSeed);
                    var currentResult = xoshiro256p(newState);

                    finalResult += Convert.ToString((long)currentResult, 2);

                    numerator = numerator * 10UL;
                }
            }
            catch
            {
                finalResult = null;
            }

            return finalResult;
        }

        static ulong splitmix64(ulong state)
        {
            state = state + 0x9E3779B97f4A7C15;
            state = (state ^ (state >> 30)) * 0xBF58476D1CE4E5B9;
            state = (state ^ (state >> 27)) * 0x94D049BB133111EB;
            return state ^ (state >> 31);
        }

        static ulong[] xorshift256_init(ulong seed)
        {
            var result = new ulong[4];
            result[0] = splitmix64(seed);
            result[1] = splitmix64(result[0]);
            result[2] = splitmix64(result[2]);
            result[3] = splitmix64(result[3]);
            return result;
        }

        static ulong rol64(ulong x, int k)
        {
            return (x << k) | (x >> (64 - k));
        }

        static ulong xoshiro256p(ulong[] state)
        {
            ulong result = rol64(state[1] * 5, 7) * 9;
            ulong t = state[1] << 17;

            state[2] ^= state[0];
            state[3] ^= state[1];
            state[1] ^= state[2];
            state[0] ^= state[3];

            state[2] ^= t;
            state[3] = rol64(state[3], 45);

            return result;
        }
    }
}
