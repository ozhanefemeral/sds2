using System.Text;

namespace XoshiroAPI
{
    public class XoshiroGenerator
    {
        private ulong[] _s = new ulong[4];

        public string? Generate(string seed, string size)
        {
            var finalResult = new StringBuilder();
            try
            {
                var sizeValue = Convert.ToInt32(size);
                var seedValue = Convert.ToUInt64(seed);

                InitializeState(seedValue);

                while (finalResult.Length < sizeValue)
                {
                    var currentResult = Xoshiro256SS();

                    var binaryResult = Convert.ToString((long)currentResult, 2);

                    finalResult.Append(binaryResult);
                }

                return finalResult.ToString()[..sizeValue].ToString();
            }
            catch
            {
                return null;
            }
        }

        private static ulong Rol64(ulong x, int k)
        {
            return (x << k) | (x >> (64 - k));
        }

        private ulong Xoshiro256SS()
        {
            var result = Rol64(_s[1] * 5, 7) * 9;
            var t = _s[1] << 17;

            _s[2] ^= _s[0];
            _s[3] ^= _s[1];
            _s[1] ^= _s[2];
            _s[0] ^= _s[3];

            _s[2] ^= t;
            _s[3] = Rol64(_s[3], 45);

            return result;
        }

        private void InitializeState(ulong seed)
        {
            _s[0] = Splitmix64(seed);
            _s[1] = Splitmix64(_s[0]);
            _s[2] = Splitmix64(_s[1]);
            _s[3] = Splitmix64(_s[2]);
        }

        private static ulong Splitmix64(ulong seed)
        {
            seed += 0x9E3779B97f4A7C15;
            seed = (seed ^ (seed >> 30)) * 0xBF58476D1CE4E5B9;
            seed = (seed ^ (seed >> 27)) * 0x94D049BB133111EB;

            return seed ^ (seed >> 31);
        }
    }
}