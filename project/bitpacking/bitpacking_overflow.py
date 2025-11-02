from .bitpacking_v1 import BitPackingV1

class BitPackingOverflow(BitPackingV1):
    def __init__(self, bits_per_value, overflow_limit):
        super().__init__(bits_per_value)
        self.overflow_limit = overflow_limit 
        self.overflow = []

    def compress(self, arr):
        base_encoded = []
        self.overflow.clear()
        index_in_overflow = 0

        for val in arr:
            if val < (1 << (self.overflow_limit - 1)):

                base_encoded.append((0, val))
            else:

                base_encoded.append((1, index_in_overflow))
                self.overflow.append(val)
                index_in_overflow += 1

        packed = []
        bits_in_int = 32
        mask = (1 << self.k) - 1
        current = 0
        bit_shift = 0

        for flag, val in base_encoded:
            combined = (flag << (self.k - 1)) | (val & (mask >> 1))
            current |= combined << bit_shift
            bit_shift += self.k

            if bit_shift >= bits_in_int:
                packed.append(current)
                bit_shift -= bits_in_int
                current = (combined >> (self.k - bit_shift)) if bit_shift > 0 else 0

        if bit_shift > 0:
            packed.append(current)

        self.data = packed
        self.original_size = len(arr)
        return packed

    def decompress(self):
        mask = (1 << self.k) - 1
        bits_in_int = 32
        result = []
        for i in range(self.original_size):
            idx = (i * self.k) // bits_in_int
            shift = (i * self.k) % bits_in_int
            combined = (self.data[idx] >> shift) & mask
            flag = (combined >> (self.k - 1)) & 1
            value_bits = combined & ((1 << (self.k - 1)) - 1)
            if flag == 0:
                result.append(value_bits)
            else:
                if value_bits < len(self.overflow):
                    result.append(self.overflow[value_bits])
                else:
                    result.append(0)
        return result
