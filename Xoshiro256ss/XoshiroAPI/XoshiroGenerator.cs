namespace XoshiroAPI
{
    public class XoshiroGenerator
    {
        private ulong[] _s = new ulong[4];

        public string? Generate(string seed, string size)
        {
            var finalResult = "";
            try
            {
                var sizeValue = Convert.ToInt32(size);
                var seedValue = Convert.ToUInt64(seed);

                InitializeState(seedValue);

                var initialResult = Xoshiro256SS();

                InitializeState(initialResult);

                while (finalResult.Length < sizeValue)
                {
                    var currentResult = Xoshiro256SS();

                    finalResult += Convert.ToString((long)currentResult, 2);

                    InitializeState(currentResult);
                }

                var lastResult = finalResult[..sizeValue];

                return lastResult;
            }
            catch
            {
                finalResult = null;

                return finalResult;
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