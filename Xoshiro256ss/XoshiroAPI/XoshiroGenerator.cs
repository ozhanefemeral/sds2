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
            for (var i = 0; i < _s.Length; i++)
            {
                _s[i] = (ulong)DateTime.Now.Ticks % seed;
            }
        }
    }
}