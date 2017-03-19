# Get Data Elements on 
def get_DE(bitmaps):
    if bitmaps is None:
        print("[ERROR] Error generate DE - bitmaps null or not exists")
        return
    data_elements = []
    for count in range ( 0, len(bitmaps) ):
        length = 64 * ( count + 1 )
        for bit in range ( 1, length + 1 ):
            # is_set identifies which Data Elements is set on bitmap
            is_set = ( 1 << length - bit ) & bitmaps[count]
            if ( is_set  != 0 ):
                data_elements.append(bit)
    return data_elements

# Parse and verify if is a bitmap valid
def parse_bitmaps(str_bitmap):
    list_bitmaps = []
    ini = 0
    end = 16
    # verifies if is 16 divisible chars
    if ( len(str_bitmap) % 16 == 0 ):
        div = len(str_bitmap) / 16
    else:
        print("[ERROR] Error in parsing - bitmap not valid")
        return
    # parse and add to a list
    for count in range( 0, int(div) ):
        list_bitmaps.append(int( str_bitmap[ini:end], 16 ))
        ini = ini + 16
        end = end + 16
    # verifies if which bitmap has `1` on first bit
    for count in range( 0, len(list_bitmaps) ):
        if ( ( 1 << 64 - 1) &  list_bitmaps[count] == 0 ):
            print("[ERROR] Error in set bitmap ", count, " isn't '1'", bin(list_bitmaps[count]),( 1 << 64 - 1) &  list_bitmaps[count] != 0)
    return list_bitmaps

# main
bitmap = "800001001C0000408000110000000020800001001C000040"
parsed = parse_bitmaps(bitmap)
get_DE(parsed)
