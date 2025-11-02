from .base import BitPacking

class BitPackingV2(BitPacking):
    def compress(self, arr):
        packed = []
        mask = (1 << self.k) - 1
        current_val = 0
        used_bits = 0
        bits_in_int = 32

        for val in arr:
            if self.k <= (bits_in_int - used_bits):
                current_val |= (val & mask) << used_bits
                used_bits += self.k
                if used_bits == bits_in_int:
                    packed.append(current_val)
                    current_val = 0
                    used_bits = 0
            else:
                remaining = bits_in_int - used_bits
                current_val |= (val & ((1 << remaining) - 1)) << used_bits
                packed.append(current_val)
                current_val = val >> remaining
                used_bits = self.k - remaining

        if used_bits > 0:
            packed.append(current_val)

        self.data = packed
        self.original_size = len(arr)
        return packed

    def decompress(self):
        mask = (1 << self.k) - 1
        bits_in_int = 32
        result = []

        bit_pos = 0
        int_index = 0

        for _ in range(self.original_size):
            if int_index >= len(self.data):
                break
            val = (self.data[int_index] >> bit_pos) & mask
            bit_pos += self.k
            if bit_pos >= bits_in_int:
                bit_pos -= bits_in_int
                int_index += 1
                if int_index < len(self.data):
                    val |= (self.data[int_index] & ((1 << bit_pos) - 1)) << (self.k - bit_pos)
            result.append(val)
        return result

    def get(self, i):

        return self.decompress()[i]
