# encoding: utf-8

import sys
sys.path.append('./Pyso8583')
from parser_iso8583 import *

if __name__ == '__main__':

    msg = "02003238640128C18200002000000000160121090612024700745112022409069951484050110000000722537636318*************=2108*******01003000006502937900002970000000000002020222******************************************************************************************************************************************************************************************************************************4843129F2701809F3602018E9F2608B12C8EC8650ACC949F10050000000188950500800010009B02E8009F01060000000072259F41030000345F360102DF7A0101DF7B03000000DF7C0400000000DF68050000000000DF6104205AD928DF63080000000040200001DF6206000000060566DF6003005763DF7201009F080202059A031709069F21031202248104000271795F20064D4E493032379F45020000"

    parse = ParserMessageIso(msg)

    print_iso("<Message Original>"      , parse.get_message_iso())
    print_iso("<Message Type Indicator>", parse.get_mti())
    print_iso("<Bitmap>"                , parse.get_bitmap())
    print_iso("<Bits Active>"           , BitmapIso.get_bitmap(parse.bitmap))
    
    list_de = parse.get_data_element()
    
    print("<Data Elements>")
    for count in range(0, len(list_de)):
        print("\t<Data Element {:03d}> [{}] -> {}\t".format(list_de[count][0],list_de[count][1], DataElementIso.BITS_VALUE_TYPE[list_de[count][0]][1]))
