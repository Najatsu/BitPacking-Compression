from bitpacking.factory import make_bitpacker
import random

if __name__ == "__main__":
    arr = [1, 2, 3, 1024, 4, 5, 2048]
    bp = make_bitpacker("overflow", 12, overflow_limit=8)
    c = bp.compress(arr)
    print("Compressed:", c)
    print("Overflow zone:", bp.overflow)
    print("Decompressed:", bp.decompress())

    big = [random.randint(0, 4095) for _ in range(5000)]
    bp2 = make_bitpacker("overlap", 12)
    t = bp2.measure(bp2.compress, big)
    print(f"Compression time (5000 ints): {t:.5f}s")
