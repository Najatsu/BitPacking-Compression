import time

class BitPacking:
    def __init__(self, bits_per_value):
        self.k = bits_per_value
        self.data = []
        self.original_size = 0

    def compress(self, arr):
        raise NotImplementedError

    def decompress(self):
        raise NotImplementedError

    def get(self, i):
        raise NotImplementedError

    def measure(self, func, *args):
        start = time.perf_counter()
        func(*args)
        return time.perf_counter() - start
