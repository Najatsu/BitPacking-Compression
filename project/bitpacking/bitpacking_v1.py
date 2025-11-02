from .base import BitPacking

class BitPackingV1(BitPacking):
    def compress(self, arr):
        packed = []
        bits_in_int = 32
        mask = (1 << self.k) - 1
        current_val = 0
        shift = 0

        for num in arr:
            current_val |= (num & mask) << shift
            shift += self.k

            if shift >= bits_in_int:
                packed.append(current_val)
                shift -= bits_in_int
                current_val = (num >> (self.k - shift)) if shift > 0 else 0

        if shift > 0:
            packed.append(current_val)

        self.data = packed
        self.original_size = len(arr)
        return packed

    def decompress(self):
        result = []
        mask = (1 << self.k) - 1
        bits_in_int = 32

        for i in range(self.original_size):
            index = (i * self.k) // bits_in_int
            offset = (i * self.k) % bits_in_int
            val = (self.data[index] >> offset) & mask
            result.append(val)
        return result

    def get(self, i):
        bits_in_int = 32
        mask = (1 << self.k) - 1
        idx = (i * self.k) // bits_in_int
        offset = (i * self.k) % bits_in_int
        return (self.data[idx] >> offset) & mask
