from parser_iso8583 import *
from struct_iso8583 import *
from utils import *

if __name__ == '__main__':
    
    #Area of Class Tests
    #MessageIso() Tests
    msg           = "02003238640128C182000020000000000010550403102449904108102449040399514840501100000007225376363180000126563000=21010000150010030000403000288WAMPHML100000000000005421499002440013000300300250004000100260015POSSE200130522A00320002040040000300100510003003006200020100740016526194CE486DA110007500370048219000020040002=0000000002004000200780001200790003002012600012014500012022800048000484032DF7A01019F360202f6DF61041F76AE73"
    obj_msg       = ParserMessageIso(msg)
    log_iso(obj_msg)

    # get values
    mti = obj_msg.get_mti()
    list_bitmap = obj_msg.get_bitmap()
    data_element = obj_msg.get_data_element()

    # Show Message in ISO format 
    print_iso("Message Original", msg)
    print_iso("Message Type Identifier", mti)
    print_iso("Bitmaps", get_hex(list_bitmap))
    print_iso("Data Element", data_element)

    #MtiIso() Tests
    obj_mti = MtiIso()
    log_iso(obj_mti)
    obj_mti.mti = mti
    print_iso("Message Type Identifier", obj_mti.mti)

    #BitmapIso() Tests
    obj_bitmap = BitmapIso()
    log_iso(obj_bitmap)
    obj_bitmap.bitmap = list_bitmap
    print_iso("Bitmap",obj_bitmap.get_bitmap_parsed())

    #DataElementIso() Tests
    obj_de = DataElementIso()
    log_iso(obj_de)
    obj_de.data_element = data_element
    print_iso("Actives Data Element",obj_de.data_element)

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
