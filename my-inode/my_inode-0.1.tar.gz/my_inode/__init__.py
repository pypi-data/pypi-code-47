B_size = 2
P_size = 1
F_offset = 5
d_blocks = 12
i1_block = 13
i2_block = 14
i3_block = 15


def i_calc(bs, ps, fo):
    point_per_block = float(bs/ps)
    indirect1 = point_per_block
    indirect2 = point_per_block**2
    indirect3 = point_per_block**3
    i1_end = (i1_block*point_per_block)+indirect1
    i2_end = i1_end+(indirect2*point_per_block)
    i3_end = i2_end+(indirect3*point_per_block)
    if fo < point_per_block*d_blocks:
        return (int(((fo)/point_per_block))+1,)

    elif fo < i1_end:
        rem = fo - ((i1_block-1)*point_per_block)
        #print int(rem/point_per_block)
        return (i1_block, (int(rem/point_per_block))+1)

    elif fo < i2_end:
        rem = fo - i1_end
        rem2 = rem / point_per_block
        #print int(rem2%point_per_block)
        #print int(rem/indirect2)
        return (i2_block, int(rem/indirect2)+1, int(rem2%point_per_block)+1)

    elif fo < i3_end:
        rem = fo - i2_end
        rem2 = rem / point_per_block
        rem3 = rem / indirect2
        #print int(rem3%point_per_block)
        #print int(rem2%point_per_block)
        #print int(rem/indirect3)
        return (i3_block, int(rem/indirect3)+1, int(rem3%point_per_block)+1, int(rem2%point_per_block)+1)


if __name__ == "__main__":
    print i_calc(B_size, P_size, F_offset)