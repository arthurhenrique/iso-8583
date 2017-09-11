# encoding: utf-8

from parser_iso8583 import *

if __name__ == '__main__':
    
    parse = ParserMessageIso(msg)
    print_iso("<Message Original>"      , msg)
    print_iso("<Message Type Indicator>", parse.get_mti())
    print_iso("<Bitmap>"                , parse.get_bitmap())
    print_iso("<Bits Active>"           , BitmapIso.get_bitmap(parse.bitmap))

    list_de = parse.get_data_element() #list_parse = [55, 48] parse.get_data_element(list_parse)
    
    print("<Data Elements>")
    for bit in range(0,len(list_de)):
        print("\t<Data Element {:03d}> [{}] -> {}\t".format(list_de[bit][0],list_de[bit][1], DataElementIso.BITS_VALUE_TYPE[list_de[bit][0]][1]))
