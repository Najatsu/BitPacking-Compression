import os, sys
import random
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from bitpacking.factory import make_bitpacker

def measure_time(func, *args):
    start = time.perf_counter()
    result = func(*args)
    return time.perf_counter() - start, result

def benchmark():
    sizes = [1000, 5000, 10000, 50000]
    bits = 12
    overflow_limit = 8

    for n in sizes:
        print(f"\nBenchmark for array of size {n}")
        arr = [random.randint(0, 4095) for _ in range(n)]

        for mode in ["simple", "overlap", "overflow"]:
            if mode == "overflow":
                bp = make_bitpacker(mode, bits, overflow_limit)
            else:
                bp = make_bitpacker(mode, bits)

            t_comp, compressed = measure_time(bp.compress, arr)
            t_decomp, decompressed = measure_time(bp.decompress)
            t_get, val = measure_time(bp.get, n // 2)

            orig_bits = n * 32
            comp_bits = len(compressed) * 32
            ratio = comp_bits / orig_bits

            print(f"\nMode: {mode}")
            print(f"  Compress time:        {t_comp*1000:.2f} ms")
            print(f"  Decompress time:      {t_decomp*1000:.2f} ms")
            print(f"  Get time:             {t_get*1e6:.2f} µs")
            print(f"  Compression ratio:    {ratio:.3f}")

if __name__ == "__main__":
    benchmark()
