from bitpacking.bitpacking_v1 import BitPackingV1
from bitpacking.bitpacking_v2 import BitPackingV2
from bitpacking.bitpacking_overflow import BitPackingOverflow

def make_bitpacker(mode, bits, overflow_limit=None):
    if mode == "simple":
        return BitPackingV1(bits)
    elif mode == "overlap":
        return BitPackingV2(bits)
    elif mode == "overflow":
        if overflow_limit is None:
            raise ValueError("Need overflow_limit for overflow mode")
        return BitPackingOverflow(bits, overflow_limit)
    else:
        raise ValueError("Unknown mode: " + mode)
