"""MessageIso is a message type in ISO format ( string ), 
that contains 3 basics structs( MTI, Bitmap and Data Elements )"""
class MessageIso:

    # Property `message_iso` is a message type in ISO format ( string ), 
    # that contains 3 basics structs( MTI, Bitmap and Data Elements )
    message_iso = ""

    # Property `list_bitmap` List of bitmap
    list_bitmap = []

    def __init__(self, message_iso = ""):
        self.message_iso = message_iso
    
    def set_message_iso(self, message_iso):
        self.message_iso = message_iso

    def get_message_iso(self):
        return self.message_iso

    def set_list_bitmap(self, bitmap):
        self.list_bitmap.append(bitmap)

    def get_list_bitmap(self):
        return self.list_bitmap

    def parse_mti(self, ini):
        end = 4
        return self.message_iso[ini:end]
    """
    call parse_bitmap while has another bitmap
    """
    def parse_bitmap(self, ini):
        end = ini + 16
        bitmap = int(self.message_iso[ini:end], 16)
        self.set_list_bitmap(hex(bitmap)[2:])
        if Bitmap.has_another_bitmap(bitmap):
            ini = ini + 16
            end = end + 16
            self.parse_bitmap(ini)
        return self.list_bitmap

    def parse_data_elements(self):
        pass
        return self.message_iso[20:-1]

class MtiIso:

    mti_iso = ""
    """docstring for MtiIso"""
    def __init__(self, mti_iso = ""):
        self.mti_iso = mti_iso
    
    def set_message_iso(self, mti_iso):
        self.mti_iso = mti_iso

    def get_message_iso(self):
        return self.mti_iso

class Bitmap:
    
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

    @staticmethod
    def has_another_bitmap(bitmap):
        is_set = ( 1 << 64 - 1 ) &  bitmap
        # if the first bit is 0
        if ( is_set == 0 ):
            return False
        else:
            return True

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
                # find bit
                if ( is_set  != 0 ):
                    data_elements.append(bit)
        return data_elements

class DataElementIso:
    data_element = ""
    """docstring for MtiIso"""
    def __init__(self, data_element = ""):
        self.data_element = data_element
    
    def set_message_iso(self, data_element):
        self.data_element = data_element

    def get_message_iso(self):
        return self.data_element
        
        
if __name__ == '__main__':
    #Area of Class Tests
    """
    <INFO> - >> MSG ISO8583 
    02003238640128C182000020000000000010550403102449904108102449040399514840501100000007225376363180000126563000=21010000150010030000403000288WAMPHML100000000000005421499002440013000300300250004000100260015POSSE200130522A00320002040040000300100510003003006200020100740016526194CE486DA110007500370048219000020040002=0000000002004000200780001200790003002012600012014500012022800048000484032DF7A01019F360202f6DF61041F76AE73
    <INFO> - >> PARSE ISO8583 
    <Message Type Indicator> [0200]
    <Primary Bitmap        > [3238640128C18200]
    <Data Element 003      > [002000] -> [Processing code]
    <Data Element 004      > [000000001055] -> [Amount, transaction]
    <Data Element 007      > [0403102449] -> [Transmission date & time]
    <Data Element 011      > [904108] -> [Systems trace audit number]
    <Data Element 012      > [102449] -> [Time, Local transaction (hhmmss)]
    <Data Element 013      > [0403] -> [Date, Local transaction (MMDD)]
    <Data Element 018      > [9951] -> [Merchant type]
    <Data Element 019      > [484] -> [Acquiring institution country code]
    <Data Element 022      > [050] -> [Point of service entry mode]
    <Data Element 032      > [11] [00000007225] -> [Acquiring institution identification code]
    <Data Element 035      > [37] [6363180000126563000=21010000150010030] -> [Track 2 data]
    <Data Element 037      > [000403000288] -> [Retrieval reference number]
    <Data Element 041      > [WAMPHML1] -> [Card acceptor terminal identification]
    <Data Element 042      > [000000000000054] -> [Card acceptor identification code]
    <Data Element 048      > [214] [99002440013000300300250004000100260015POSSE200130522A00320002040040000300100510003003006200020100740016526194CE486DA110007500370048219000020040002=0000000002004000200780001200790003002012600012014500012022800048000] -> [Additional data - Private]
    <Data Element 049      > [484] -> [Currency code, transaction]
    <Data Element 055      > [032] [DF7A01019F360202f6DF61041F76AE73] -> [Reserved ISO]
    """
    #MessageIso() Tests
    msg = "02003238640128C182000020000000000010550403102449904108102449040399514840501100000007225376363180000126563000=21010000150010030000403000288WAMPHML100000000000005421499002440013000300300250004000100260015POSSE200130522A00320002040040000300100510003003006200020100740016526194CE486DA110007500370048219000020040002=0000000002004000200780001200790003002012600012014500012022800048000484032DF7A01019F360202f6DF61041F76AE73"
    test_msg = MessageIso(msg)
    print("MTI")
    print(test_msg.parse_mti(0))
    print()
    print("BITMAP")
    print(test_msg.parse_bitmap(4))
    print()
    print("DATA ELEMENTS")
    print(test_msg.parse_data_elements())

    #MtiIso() Tests

    #Bitmap() Tests
    test_bitmap = Bitmap()
    bitmap = "8000100001000000"
    bitmap = "3238640128C18200"
    bitmap = "A20000010400020080000000100000104000040000000000"
    bitmap = "3238640128C18200"
    test_bitmap.set_bitmap(bitmap)
    print(test_bitmap.get_data_elements())
    
    
    #DataElementIso() Tests
