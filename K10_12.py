import struct


def f31(binary: bytes) -> dict:
    def struct_a(offset: int) -> dict:
        a1 = list(struct.unpack('> 2H', binary[offset: offset + 4]))
        offset += 4

        [length1] = struct.unpack('> I', binary[offset: offset + 4])
        offset += 4
        [link_str] = struct.unpack('> I', binary[offset: offset + 4])
        a2 = str([struct.unpack('>' + str(length1) + 's', binary[link_str: link_str + length1])])[4:-4]
        offset += 4

        [a3] = struct.unpack('> f', binary[offset: offset + 4])
        offset += 4
        [a4] = struct.unpack('> i', binary[offset: offset + 4])
        offset += 4
        a5 = list(struct.unpack('> 4Q', binary[offset: offset + 32]))
        offset += 32
        [a6] = struct.unpack('> i', binary[offset: offset + 4])
        offset += 4
        [a7] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2
        a8 = struct_d(offset)
        offset += 1 + 8 + 28 + 8 + 2 + 2
        return {
            'A1': [struct_b(i) for i in a1],
            'A2': a2,
            'A3': a3,
            'A4': a4,
            'A5': a5,
            'A6': a6,
            'A7': struct_c(a7),
            'A8': a8
        }

    def struct_b(offset: int) -> dict:
        [b1] = struct.unpack('> h', binary[offset: offset + 2])
        offset += 2
        [b2] = struct.unpack('> f', binary[offset: offset + 4])
        offset += 4

        [length1] = struct.unpack('> I', binary[offset: offset + 4])
        offset += 4
        [link_str] = struct.unpack('> I', binary[offset: offset + 4])
        b3 = str([struct.unpack('>' + str(length1) + 's', binary[link_str: link_str + length1])])[4:-4]
        offset += 4

        return {
            'B1': b1,
            'B2': b2,
            'B3': b3
        }

    def struct_c(offset: int) -> dict:
        [c1] = struct.unpack('> b', binary[offset: offset + 1])
        offset += 1
        [c2] = struct.unpack('> f', binary[offset: offset + 4])
        offset += 4
        [c3] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2
        [c4] = struct.unpack('> Q', binary[offset: offset + 8])
        offset += 8
        [c5] = struct.unpack('> h', binary[offset: offset + 2])
        offset += 2
        [c6] = struct.unpack('> b', binary[offset: offset + 1])
        offset += 1
        [c7] = struct.unpack('> h', binary[offset: offset + 2])
        offset += 2
        [c8] = struct.unpack('> f', binary[offset: offset + 4])
        offset += 4

        return {
            'C1': c1,
            'C2': c2,
            'C3': c3,
            'C4': c4,
            'C5': c5,
            'C6': c6,
            'C7': c7,
            'C8': c8
        }

    def struct_d(offset: int) -> dict:
        [d1] = struct.unpack('> b', binary[offset: offset + 1])
        offset += 1
        [d2] = struct.unpack('> Q', binary[offset: offset + 8])
        offset += 8
        d3 = list(struct.unpack('> 7i', binary[offset: offset + 28]))
        offset += 28
        [d4] = struct.unpack('> q', binary[offset: offset + 8])
        offset += 8
        [d5] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2
        [d6] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2

        return {
            'D1': d1,
            'D2': d2,
            'D3': d3,
            'D4': d4,
            'D5': d5,
            'D6': d6
        }

    return struct_a(3)
