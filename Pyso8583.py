class Pyso8583:
    
    # Property that has DE's actives
    bitmap = []

    def __init__(self, bitmap = []):
        self.bitmap = bitmap

    # Set an string value to property bitmap
    def set_bitmap(self, str_bitmap):
        parsed = self.parse_bitmap(str_bitmap)
        self.bitmap = parsed

    # Returns list[] type 
    def get_bitmap(self):
        return self.bitmap
    
    # Parse and verify if is a bitmap valid
    def parse_bitmap(self,str_bitmap):
        max_bitmaps  = len(str_bitmap) / 16
        list_bitmaps = []
        ini = 0
        end = 16
        # parse and add to a list
        for count in range(0, int(max_bitmaps)):
            list_bitmaps.append(int( str_bitmap[ini:end], 16 ))
            ini = ini + 16
            end = end + 16
        # is bitmap a number or bit valid ?
        if not (self.is_bitmap_valid(list_bitmaps, str_bitmap)):
            return 
        else: 
            return list_bitmaps

    # Returns Boolean type if bitmap is a bitmap valid
    def is_bitmap_valid(self, list_bitmaps, str_bitmap):
        flag_bool = True
        # Verifies if is 16 divisible chars
        if ( len(str_bitmap) % 16 != 0 ):
            print("[ERROR] Error in parsing - bitmap not valid")
            return False
        # Verifies to each bitmap if first bit is '1'
        for count in range(0, len(list_bitmaps) - 1):
            is_set = ( 1 << 64 - 1 ) &  list_bitmaps[count]
            # if the first bit is 0, got an error 
            if ( is_set == 0 ):
                print("[ERROR] Error in set bitmap [", count, " isn't '1'", bin(list_bitmaps[count]), ( 1 << 64 - 1) &  list_bitmaps[count] != 0)
                flag_bool = False
        if flag_bool:
            return True
        else:
            return False

    # Shows the Data Elements Acives in bitmap
    def get_data_elements(self):
        data_elements = []
        list_bitmaps  = self.bitmap
        # Verify if is Null
        if list_bitmaps is None:
            print("[ERROR] Error generate DE - list_bitmaps null or not exists")
            return False
        # To each bitmap show the bit setted on
        for count in range ( 0, len(list_bitmaps) ):
            length = 64 * ( count + 1 )
            for bit in range ( 1, length + 1 ):
                # is_set identifies which Data Elements is set on bitmap
                is_set = ( 1 << length - bit ) & list_bitmaps[count]
                if ( is_set  != 0 ):
                    data_elements.append(bit)
        return data_elements


if __name__ == '__main__':
    iso = Pyso8583()
    bitmap = "8000100001000000C000040000000000C200040000000000"
    iso.set_bitmap(bitmap)
    print(iso.get_data_elements())
