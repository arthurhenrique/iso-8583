import struct
from utils import *

class MtiIso:
    mti = ""

    def __init__(self, mti_iso = ""):
        self.mti_iso = mti_iso
    
        
class BitmapIso:
    # List of bitmaps 
    bitmap = []

    def __init__(self, bitmap = []):
        self.bitmap = bitmap
    
    @staticmethod
    def get_bitmap(list_bitmap):
        bits = []
        # Verify if is Null
        if len(list_bitmap) is 0:
            list_bitmap = self.bitmap
        # To each list_bitmap show the bit setted on
        for count in range ( 0, len(list_bitmap) ):
            length = 64 * ( count + 1 )
            for bit in range ( 1, length + 1 ):
                # is_set identifies which Data Elements is set on list_bitmap
                is_set = ( 1 << length - bit ) & list_bitmap[count]
                # find bit
                if ( is_set  != 0 ):
                    bits.append(bit)
        return bits

    @staticmethod
    def has_another_bitmap(list_bitmap):
        is_set = ( 1 << 64 - 1 ) &  list_bitmap
        # if the first bit is 0
        if ( is_set == 0 ):
            return False
        else:
            return True

class DataElementIso:

    list_bitmap = []

    data_element = ""

    bit_value    = []

    BITS_VALUE_TYPE = {}

    # Every BITS_VALUE_TYPE has:
    # BITS_VALUE_TYPE[N] = [ X,Y, Z, W,K]
    # N = bitnumber
    # X = smallStr representation of the bit meanning
    # Y = large str representation
    # Z = type of the bit (B, N, A, AN, ANS, LL, LLL)
    # W = size of the information that N need to has
    # K = type os values a, an, n, ansb, b
    BITS_VALUE_TYPE[  0] = ['','','','','']
    BITS_VALUE_TYPE[  1] = ['BME','Bit map '                                   ,'B'  ,16 ,'b'  ]
    BITS_VALUE_TYPE[  2] = ['2'  ,'Primary account number (PAN)'               ,'LL' ,19 ,'n'  ]
    BITS_VALUE_TYPE[  3] = ['3'  ,'Processing code'                            ,'N'  ,6  ,'n'  ]
    BITS_VALUE_TYPE[  4] = ['4'  ,'Amount, transaction'                        ,'N'  ,12 ,'n'  ]
    BITS_VALUE_TYPE[  5] = ['5'  ,'Amount, settlement'                         ,'N'  ,12 ,'n'  ]
    BITS_VALUE_TYPE[  6] = ['6'  ,'Amount, cardholder billing'                 ,'N'  ,12 ,'n'  ]
    BITS_VALUE_TYPE[  7] = ['7'  ,'Transmission date & time'                   ,'N'  ,10 ,'n'  ]
    BITS_VALUE_TYPE[  8] = ['8'  ,'Amount, cardholder billing fee'             ,'N'  ,8  ,'n'  ]
    BITS_VALUE_TYPE[  9] = ['9'  ,'Conversion rate, settlement'                ,'N'  ,8  ,'n'  ]
    BITS_VALUE_TYPE[ 10] = ['10' ,'Conversion rate, cardholder billing'        ,'N'  ,8  ,'n'  ]
    BITS_VALUE_TYPE[ 11] = ['11' ,'System trace audit number (STAN)'           ,'N'  ,6  ,'n'  ]
    BITS_VALUE_TYPE[ 12] = ['12' ,'Time, local transaction (hhmmss)'           ,'N'  ,6  ,'n'  ]
    BITS_VALUE_TYPE[ 13] = ['13' ,'Date, local transaction (MMDD)'             ,'N'  ,4  ,'n'  ]
    BITS_VALUE_TYPE[ 14] = ['14' ,'Date, expiration'                           ,'N'  ,4  ,'n'  ]
    BITS_VALUE_TYPE[ 15] = ['15' ,'Date, settlement'                           ,'N'  ,4  ,'n'  ]
    BITS_VALUE_TYPE[ 16] = ['16' ,'Date, conversion'                           ,'N'  ,4  ,'n'  ]
    BITS_VALUE_TYPE[ 17] = ['17' ,'Date, capture'                              ,'N'  ,4  ,'n'  ]
    BITS_VALUE_TYPE[ 18] = ['18' ,'Merchant type'                              ,'N'  ,4  ,'n'  ]
    BITS_VALUE_TYPE[ 19] = ['19' ,'Acquiring institution country code'         ,'N'  ,3  ,'n'  ]
    BITS_VALUE_TYPE[ 20] = ['20' ,'PAN extended, country code'                 ,'N'  ,3  ,'n'  ]
    BITS_VALUE_TYPE[ 21] = ['21' ,'Forwarding institution. country code'       ,'ANS',3  ,'n'  ]
    BITS_VALUE_TYPE[ 22] = ['22' ,'Point of service entry mode'                ,'N'  ,3  ,'n'  ]
    BITS_VALUE_TYPE[ 23] = ['23' ,'Application PAN sequence number'            ,'N'  ,3  ,'n'  ]
    BITS_VALUE_TYPE[ 24] = ['24' ,'Function code (ISO 8583:1993)/(NII)'        ,'N'  ,3  ,'n'  ]
    BITS_VALUE_TYPE[ 25] = ['25' ,'Point of service condition code'            ,'N'  ,2  ,'n'  ]
    BITS_VALUE_TYPE[ 26] = ['26' ,'Point of service capture code'              ,'N'  ,2  ,'n'  ]
    BITS_VALUE_TYPE[ 27] = ['27' ,'Authorizing identification response length' ,'N'  ,1  ,'n'  ]
    BITS_VALUE_TYPE[ 28] = ['28' ,'Amount, transaction fee'                    ,'N'  ,8  ,'n'  ]
    BITS_VALUE_TYPE[ 29] = ['29' ,'Amount, settlement fee'                     ,'N'  ,8  ,'n'  ]
    BITS_VALUE_TYPE[ 30] = ['30' ,'Amount, transaction processing fee'         ,'N'  ,8  ,'n'  ]
    BITS_VALUE_TYPE[ 31] = ['31' ,'Amount, settlement processing fee'          ,'N'  ,8  ,'n'  ]
    BITS_VALUE_TYPE[ 32] = ['32' ,'Acquiring institution identification code'  ,'LL' ,11 ,'n'  ]
    BITS_VALUE_TYPE[ 33] = ['33' ,'Forwarding institution identification code' ,'LL' ,11 ,'n'  ]
    BITS_VALUE_TYPE[ 34] = ['34' ,'Primary account number, extended'           ,'LL' ,28 ,'n'  ]
    BITS_VALUE_TYPE[ 35] = ['35' ,'Track 2 data'                               ,'LL' ,37 ,'n'  ]
    BITS_VALUE_TYPE[ 36] = ['36' ,'Track 3 data'                               ,'LLL',104,'n'  ]
    BITS_VALUE_TYPE[ 37] = ['37' ,'Retrieval reference number'                 ,'N'  ,12 ,'an' ]
    BITS_VALUE_TYPE[ 38] = ['38' ,'Authorization identification response'      ,'N'  ,6  ,'an' ]
    BITS_VALUE_TYPE[ 39] = ['39' ,'Response code'                              ,'A'  ,2  ,'an' ]
    BITS_VALUE_TYPE[ 40] = ['40' ,'Service restriction code'                   ,'N'  ,3  ,'an' ]
    BITS_VALUE_TYPE[ 41] = ['41' ,'Card acceptor terminal identification'      ,'AN' ,8  ,'ans']
    BITS_VALUE_TYPE[ 42] = ['42' ,'Card acceptor identification code'          ,'AN' ,15 ,'ans']
    BITS_VALUE_TYPE[ 43] = ['43' ,'Card acceptor name/location '               ,'A'  ,40 ,'asn']
    BITS_VALUE_TYPE[ 44] = ['44' ,'Additional response data'                   ,'LL' ,25 ,'an' ]
    BITS_VALUE_TYPE[ 45] = ['45' ,'Track 1 data'                               ,'LL' ,76 ,'an' ]
    BITS_VALUE_TYPE[ 46] = ['46' ,'Additional data - ISO'                      ,'LLL',999,'an' ]
    BITS_VALUE_TYPE[ 47] = ['47' ,'Additional data - national'                 ,'LLL',999,'an' ]
    BITS_VALUE_TYPE[ 48] = ['48' ,'Additional data - private'                  ,'LLL',999,'an' ]
    BITS_VALUE_TYPE[ 49] = ['49' ,'Currency code, transaction'                 ,'A'  ,3  ,'a'  ]
    BITS_VALUE_TYPE[ 50] = ['50' ,'Currency code, settlement'                  ,'AN' ,3  ,'an' ]
    BITS_VALUE_TYPE[ 51] = ['51' ,'Currency code, cardholder billing'          ,'A'  ,3  ,'a'  ]
    BITS_VALUE_TYPE[ 52] = ['52' ,'Personal identification number data'        ,'B'  ,16 ,'b'  ]
    BITS_VALUE_TYPE[ 53] = ['53' ,'Security related control information'       ,'LL' ,18 ,'n'  ]
    BITS_VALUE_TYPE[ 54] = ['54' ,'Additional amounts'                         ,'LLL',120,'an' ]
    BITS_VALUE_TYPE[ 55] = ['55' ,'ICC Data - EMV having multiple tags'        ,'LLL',999,'ans']
    BITS_VALUE_TYPE[ 56] = ['56' ,'Reserved ISO'                               ,'LLL',999,'ans']
    BITS_VALUE_TYPE[ 57] = ['57' ,'Reserved national'                          ,'LLL',999,'ans']
    BITS_VALUE_TYPE[ 58] = ['58' ,'Reserved national'                          ,'LLL',999,'ans']
    BITS_VALUE_TYPE[ 59] = ['59' ,'Reserved national'                          ,'LLL',999,'ans']
    BITS_VALUE_TYPE[ 60] = ['60' ,'Reserved national'                          ,'LL' ,7  ,'ans']
    BITS_VALUE_TYPE[ 61] = ['61' ,'Reserved private'                           ,'LLL',999,'ans']
    BITS_VALUE_TYPE[ 62] = ['62' ,'Reserved private'                           ,'LLL',999,'ans']
    BITS_VALUE_TYPE[ 63] = ['63' ,'Reserved private'                           ,'LLL',999,'ans']
    BITS_VALUE_TYPE[ 64] = ['64' ,'Message authentication code (MAC)'          ,'B'  ,16 ,'b'  ]
    BITS_VALUE_TYPE[ 65] = ['65' ,'Bitmap, extended'                           ,'B'  ,16 ,'b'  ]
    BITS_VALUE_TYPE[ 66] = ['66' ,'Settlement code'                            ,'N'  ,1  ,'n'  ]
    BITS_VALUE_TYPE[ 67] = ['67' ,'Extended payment code'                      ,'N'  ,2  ,'n'  ]
    BITS_VALUE_TYPE[ 68] = ['68' ,'Receiving institution country code'         ,'N'  ,3  ,'n'  ]
    BITS_VALUE_TYPE[ 69] = ['69' ,'Settlement institution country code'        ,'N'  ,3  ,'n'  ]
    BITS_VALUE_TYPE[ 70] = ['70' ,'Network management information code'        ,'N'  ,3  ,'n'  ]
    BITS_VALUE_TYPE[ 71] = ['71' ,'Message number'                             ,'N'  ,4  ,'n'  ]
    BITS_VALUE_TYPE[ 72] = ['72' ,'Message number, last'                       ,'LLL',999,'ans']
    BITS_VALUE_TYPE[ 73] = ['73' ,'Date, action (YYMMDD)'                      ,'N'  ,6  ,'n'  ]
    BITS_VALUE_TYPE[ 74] = ['74' ,'Credits, number'                            ,'N'  ,10 ,'n'  ]
    BITS_VALUE_TYPE[ 75] = ['75' ,'Credits, reversal number'                   ,'N'  ,10 ,'n'  ]
    BITS_VALUE_TYPE[ 76] = ['76' ,'Debits, number'                             ,'N'  ,10 ,'n'  ]
    BITS_VALUE_TYPE[ 77] = ['77' ,'Debits, reversal number'                    ,'N'  ,10 ,'n'  ]
    BITS_VALUE_TYPE[ 78] = ['78' ,'Transfer number'                            ,'N'  ,10 ,'n'  ]
    BITS_VALUE_TYPE[ 79] = ['79' ,'Transfer, reversal number'                  ,'N'  ,10 ,'n'  ]
    BITS_VALUE_TYPE[ 80] = ['80' ,'Inquiries number'                           ,'N'  ,10 ,'n'  ]
    BITS_VALUE_TYPE[ 81] = ['81' ,'Authorizations, number'                     ,'N'  ,10 ,'n'  ]
    BITS_VALUE_TYPE[ 82] = ['82' ,'Credits, processing fee amount'             ,'N'  ,12 ,'n'  ]
    BITS_VALUE_TYPE[ 83] = ['83' ,'Credits, transaction fee amount'            ,'N'  ,12 ,'n'  ]
    BITS_VALUE_TYPE[ 84] = ['84' ,'Debits, processing fee amount'              ,'N'  ,12 ,'n'  ]
    BITS_VALUE_TYPE[ 85] = ['85' ,'Debits, transaction fee amount'             ,'N'  ,12 ,'n'  ]
    BITS_VALUE_TYPE[ 86] = ['86' ,'Credits, amount'                            ,'N'  ,15 ,'n'  ]
    BITS_VALUE_TYPE[ 87] = ['87' ,'Credits, reversal amount'                   ,'N'  ,15 ,'n'  ]
    BITS_VALUE_TYPE[ 88] = ['88' ,'Debits, amount'                             ,'N'  ,15 ,'n'  ]
    BITS_VALUE_TYPE[ 89] = ['89' ,'Debits, reversal amount'                    ,'N'  ,15 ,'n'  ]
    BITS_VALUE_TYPE[ 90] = ['90' ,'Original data elements'                     ,'N'  ,42 ,'n'  ]
    BITS_VALUE_TYPE[ 91] = ['91' ,'File update code'                           ,'AN' ,1  ,'an' ]
    BITS_VALUE_TYPE[ 92] = ['92' ,'File security code'                         ,'N'  ,2  ,'n'  ]
    BITS_VALUE_TYPE[ 93] = ['93' ,'Response indicator'                         ,'N'  ,5  ,'n'  ]
    BITS_VALUE_TYPE[ 94] = ['94' ,'Service indicator'                          ,'AN' ,7  ,'an' ]
    BITS_VALUE_TYPE[ 95] = ['95' ,'Replacement amounts'                        ,'AN' ,42 ,'an' ]
    BITS_VALUE_TYPE[ 96] = ['96' ,'Message security code'                      ,'AN' ,8  ,'an' ]
    BITS_VALUE_TYPE[ 97] = ['97' ,'Amount, net settlement'                     ,'N'  ,16 ,'n'  ]
    BITS_VALUE_TYPE[ 98] = ['98' ,'Payee'                                      ,'ANS',25 ,'ans']
    BITS_VALUE_TYPE[ 99] = ['99' ,'Settlement institution identification code' ,'LL' ,11 ,'n'  ]
    BITS_VALUE_TYPE[100] = ['100','Receiving institution identification code'  ,'LL' ,11 ,'n'  ]
    BITS_VALUE_TYPE[101] = ['101','File name'                                  ,'ANS',17 ,'ans']
    BITS_VALUE_TYPE[102] = ['102','Account identification 1'                   ,'LL' ,28 ,'ans']
    BITS_VALUE_TYPE[103] = ['103','Account identification 2'                   ,'LL' ,28 ,'ans']
    BITS_VALUE_TYPE[104] = ['104','Transaction description'                    ,'LLL',100,'ans']
    BITS_VALUE_TYPE[105] = ['105','Reserved for ISO use'                       ,'LLL',999,'ans']
    BITS_VALUE_TYPE[106] = ['106','Reserved for ISO use'                       ,'LLL',999,'ans']
    BITS_VALUE_TYPE[107] = ['107','Reserved for ISO use'                       ,'LLL',999,'ans']
    BITS_VALUE_TYPE[108] = ['108','Reserved for ISO use'                       ,'LLL',999,'ans']
    BITS_VALUE_TYPE[109] = ['109','Reserved for ISO use'                       ,'LLL',999,'ans']
    BITS_VALUE_TYPE[110] = ['110','Reserved for ISO use'                       ,'LLL',999,'ans']
    BITS_VALUE_TYPE[111] = ['111','Reserved for ISO use'                       ,'LLL',999,'ans']
    BITS_VALUE_TYPE[112] = ['112','Reserved for national use'                  ,'LLL',999,'ans']
    BITS_VALUE_TYPE[113] = ['113','Reserved for national use'                  ,'LL' ,11 ,'n'  ]
    BITS_VALUE_TYPE[114] = ['114','Reserved for national use'                  ,'LLL',999,'ans']
    BITS_VALUE_TYPE[115] = ['115','Reserved for national use'                  ,'LLL',999,'ans']
    BITS_VALUE_TYPE[116] = ['116','Reserved for national use'                  ,'LLL',999,'ans']
    BITS_VALUE_TYPE[117] = ['117','Reserved for national use'                  ,'LLL',999,'ans']
    BITS_VALUE_TYPE[118] = ['118','Reserved for national use'                  ,'LLL',999,'ans']
    BITS_VALUE_TYPE[119] = ['119','Reserved for national use'                  ,'LLL',999,'ans']
    BITS_VALUE_TYPE[120] = ['120','Reserved for private use'                   ,'LLL',999,'ans']
    BITS_VALUE_TYPE[121] = ['121','Reserved for private use'                   ,'LLL',999,'ans']
    BITS_VALUE_TYPE[122] = ['122','Reserved for private use'                   ,'LLL',999,'ans']
    BITS_VALUE_TYPE[123] = ['123','Reserved for private use'                   ,'LLL',999,'ans']
    BITS_VALUE_TYPE[124] = ['124','Reserved for private use'                   ,'LLL',255,'ans']
    BITS_VALUE_TYPE[125] = ['125','Reserved for private use'                   ,'LL' ,50 ,'ans']
    BITS_VALUE_TYPE[126] = ['126','Reserved for private use'                   ,'LL' ,6  ,'ans']
    BITS_VALUE_TYPE[127] = ['127','Reserved for private use'                   ,'LLL',999,'ans']
    BITS_VALUE_TYPE[128] = ['128','Message authentication code'                ,'B'  ,16 ,'b'  ]
    
    def __init__(self,bitmap=[],  data_element = ""):
        self.list_bitmap  = bitmap
        self.data_element = data_element
    
    def get_length(self, ini, bit):
        type_de = self.BITS_VALUE_TYPE[bit][2]
        if  type_de is 'LL':
            return  int(self.data_element[ini:ini + 2], 10) + 2
        elif type_de is 'LLL':
            return  int(self.data_element[ini:ini + 3], 10) + 3
        else:
            return  self.BITS_VALUE_TYPE[bit][3]

    def parse_data_element(self):
        ini    = 0
        end    = 0
        length = 0
        bits_active = BitmapIso.get_bitmap(self.list_bitmap)
        list_bit_value = []
        for count in range(0,len(bits_active)):
            bit    = bits_active[count]
            ini    = ini + length
            length = self.get_length(ini,bit)
            end    = ini + length
            list_bit_value.append([bit, self.data_element[ini:end]])
        return list_bit_value
