# encoding: utf-8
import struct

BIT_5 = 5
BIT_0 = 0


class ParserTlv():

    tag      = 0
    length   = 0
    value    = 0
    list_tlv = []

    ARRAY = {}

    ARRAY[0  ] = ['9F01', 'Acquirer Identifier'                                                   ]
    ARRAY[1  ] = ['9F02', 'Amount, Authorised (Numeric)'                                          ]
    ARRAY[2  ] = ['9F03', 'Amount, Other (Numeric)'                                               ]
    ARRAY[3  ] = ['9F04', 'Amount, Other (Binary)'                                                ]
    ARRAY[4  ] = ['9F05', 'Application Discretionary Data'                                        ]
    ARRAY[5  ] = ['9F06', 'Application Identifier (AID) - terminal'                               ]
    ARRAY[6  ] = ['9F07', 'Application Usage Control'                                             ]
    ARRAY[7  ] = ['9F08', 'Application Version Number'                                            ]
    ARRAY[8  ] = ['9F09', 'Application Version Number'                                            ]
    ARRAY[9  ] = ['9F0B', 'Cardholder Name Extended'                                              ]
    ARRAY[10 ] = ['BF0C', 'FCI Issuer Discretionary Data'                                         ]
    ARRAY[11 ] = ['9F0D', 'Issuer Action Code - Default'                                          ]
    ARRAY[12 ] = ['9F0E', 'Issuer Action Code - Denial'                                           ]
    ARRAY[13 ] = ['9F0F', 'Issuer Action Code - Online'                                           ]
    ARRAY[14 ] = ['9F10', 'Issuer Application Data'                                               ]
    ARRAY[15 ] = ['9F11', 'Issuer Code Table Index'                                               ]
    ARRAY[16 ] = ['9F12', 'Application Preferred Name'                                            ]
    ARRAY[17 ] = ['9F13', 'Last Online Application Transaction Counter (ATC) Register'            ]
    ARRAY[18 ] = ['9F14', 'Lower Consecutive Offline Limit'                                       ]
    ARRAY[19 ] = ['9F15', 'Merchant Category Code'                                                ]
    ARRAY[20 ] = ['9F16', 'Merchant Identifier'                                                   ]
    ARRAY[21 ] = ['9F17', 'Personal Identification Number (PIN) Try Counter'                      ]
    ARRAY[22 ] = ['9F18', 'Issuer Script Identifier'                                              ]
    ARRAY[23 ] = ['9F1A', 'Terminal Country Code'                                                 ]
    ARRAY[24 ] = ['9F1B', 'Terminal Floor Limit'                                                  ]
    ARRAY[25 ] = ['9F1C', 'Terminal Identification'                                               ]
    ARRAY[26 ] = ['9F1D', 'Terminal Risk Management Data'                                         ]
    ARRAY[27 ] = ['9F1E', 'Interface Device (IFD) Serial Number'                                  ]
    ARRAY[28 ] = ['9F1F', 'Track 1 Discretionary Data'                                            ]
    ARRAY[29 ] = ['5F20', 'Cardholder Name'                                                       ]
    ARRAY[30 ] = ['9F21', 'Transaction Time'                                                      ]
    ARRAY[31 ] = ['9F22', 'Certification Authority Public Key Index'                              ]
    ARRAY[32 ] = ['9F23', 'Upper Consecutive Offline Limit'                                       ]
    ARRAY[33 ] = ['5F24', 'Application Expiration Date'                                           ]
    ARRAY[34 ] = ['5F25', 'Application Effective Date'                                            ]
    ARRAY[35 ] = ['9F26', 'Application Cryptogram'                                                ]
    ARRAY[36 ] = ['9F27', 'Cryptogram Information Data'                                           ]
    ARRAY[37 ] = ['5F28', 'Issuer Country Code'                                                   ]
    ARRAY[38 ] = ['5F2A', 'Transaction Currency Code'                                             ]
    ARRAY[39 ] = ['5F2D', 'Language Preference'                                                   ]
    ARRAY[40 ] = ['9F2E', 'Integrated Circuit Card (ICC) PIN Encipherment Public Key Exponent'    ]
    ARRAY[41 ] = ['9F2F', 'Integrated Circuit Card (ICC) PIN Encipherment Public Key Remainder'   ]
    ARRAY[42 ] = ['5F30', 'Service Code'                                                          ]
    ARRAY[43 ] = ['9F32', 'Issuer Public Key Exponent'                                            ]
    ARRAY[44 ] = ['9F33', 'Terminal Capabilities'                                                 ]
    ARRAY[45 ] = ['5F34', 'Application Primary Account Number (PAN)'                              ]
    ARRAY[46 ] = ['9F35', 'Terminal Type'                                                         ]
    ARRAY[47 ] = ['5F36', 'Transaction Currency Exponent'                                         ]
    ARRAY[48 ] = ['9F37', 'Unpredictable Number'                                                  ]
    ARRAY[49 ] = ['9F38', 'Processing Options Data Object List (PDOL)'                            ]
    ARRAY[50 ] = ['9F34', 'Cardholder Verification Method (CVM) Results'                          ]
    ARRAY[51 ] = ['9F3A', 'Amount, Reference Currency'                                            ]
    ARRAY[52 ] = ['9F3B', 'Application Reference Currency'                                        ]
    ARRAY[53 ] = ['9F3C', 'Transaction Reference Currency Code'                                   ]
    ARRAY[54 ] = ['9F3D', 'Transaction Reference Currency Exponent'                               ]
    ARRAY[55 ] = ['9F40', 'Additional Terminal Capabilities'                                      ]
    ARRAY[56 ] = ['9F41', 'Transaction Sequence Counter'                                          ]
    ARRAY[57 ] = ['42'  , 'Identification Number (IIN)'                                           ]
    ARRAY[58 ] = ['9F43', 'Application Reference Currency Exponent'                               ]
    ARRAY[59 ] = ['9F44', 'Application Currency Exponent'                                         ]
    ARRAY[60 ] = ['9F2D', 'Integrated Circuit Card (ICC) PIN Encipherment Public Key Certificate' ]
    ARRAY[61 ] = ['9F46', 'Integrated Circuit Card (ICC) Public Key Certificate'                  ]
    ARRAY[62 ] = ['9F47', 'Integrated Circuit Card (ICC) Public Key Exponent'                     ]
    ARRAY[63 ] = ['9F48', 'Integrated Circuit Card (ICC) Public Key Remainder'                    ]
    ARRAY[64 ] = ['9F49', 'Dynamic Data Authentication Data Object List (DDOL)'                   ]
    ARRAY[65 ] = ['9F4A', 'Static Data Authentication Tag List'                                   ]
    ARRAY[66 ] = ['9F4B', 'Signed Dynamic Application Data'                                       ]
    ARRAY[67 ] = ['9F4C', 'ICC Dynamic Number'                                                    ]
    ARRAY[68 ] = ['9F4D', 'Log Entry'                                                             ]
    ARRAY[69 ] = ['9F4E', 'Merchant Name and Location'                                            ]
    ARRAY[70 ] = ['4F'  , 'Identifier (AID)'                                                      ]  
    ARRAY[71 ] = ['50'  , 'Label'                                                                 ]
    ARRAY[72 ] = ['9F51', 'Application Currency Code'                                             ]
    ARRAY[73 ] = ['9F52', 'Card Verification Results (CVR)'                                       ]
    ARRAY[74 ] = ['5F53', 'International Bank Account Number (IBAN)'                              ]
    ARRAY[75 ] = ['5F54', 'Bank Identifier Code (BIC)'                                            ]
    ARRAY[76 ] = ['5F55', 'Issuer Country Code (alpha2 format)'                                   ]
    ARRAY[77 ] = ['5F56', 'Issuer Country Code (alpha3 format)'                                   ]
    ARRAY[78 ] = ['57'  , '2 Equivalent Data'                                                     ]
    ARRAY[79 ] = ['9F58', 'Lower Consecutive Offline Limit (Card Check)'                          ]
    ARRAY[80 ] = ['9F59', 'Upper Consecutive Offline Limit (Card Check)'                          ]
    ARRAY[81 ] = ['5A'  , 'Primary Account Number (PAN)'                                          ]
    ARRAY[82 ] = ['9F5C', 'Cumulative Total Transaction Amount Upper Limit'                       ]
    ARRAY[83 ] = ['9F72', 'Consecutive Transaction Limit (International - Country)'               ]
    ARRAY[84 ] = ['61'  , 'Template'                                                              ]
    ARRAY[85 ] = ['9F65', 'Track 2 Bit Map for CVC3'                                              ]
    ARRAY[86 ] = ['9F66', 'Track 2 Bit Map for UN and ATC'                                        ]
    ARRAY[87 ] = ['9F68', 'Mag Stripe CVM List'                                                   ]
    ARRAY[88 ] = ['9F69', 'Unpredictable Number Data Object List (UDOL)'                          ]
    ARRAY[89 ] = ['9F6B', 'Track 2 Data'                                                          ]
    ARRAY[90 ] = ['9F6C', 'Mag Stripe Application Version Number (Card)'                          ]
    ARRAY[91 ] = ['9F6E', 'Unknown Tag'                                                           ]
    ARRAY[92 ] = ['6F'  , 'Control Information (FCI) Template'                                    ]
    ARRAY[93 ] = ['70'  , 'Proprietary Template'                                                  ]
    ARRAY[94 ] = ['71'  , 'Script Template 1'                                                     ]
    ARRAY[95 ] = ['72'  , 'Script Template 2'                                                     ]
    ARRAY[96 ] = ['73'  , 'Discretionary Template'                                                ]
    ARRAY[97 ] = ['9F74', 'VLP Issuer Authorization Code'                                         ]
    ARRAY[98 ] = ['9F75', 'Cumulative Total Transaction Amount Limit - Dual Currency'             ]
    ARRAY[99 ] = ['9F76', 'Secondary Application Currency Code'                                   ]
    ARRAY[100] = ['77'  , 'Message Template Format 2'                                             ]
    ARRAY[101] = ['9F7D', 'Unknown Tag'                                                           ]
    ARRAY[102] = ['9F7F', 'Card Production Life Cycle (CPLC) History File Identifiers'            ]
    ARRAY[103] = ['80'  , 'Message Template Format 1'                                             ]
    ARRAY[104] = ['81'  , ' Authorised (Binary)'                                                  ]
    ARRAY[105] = ['82'  , 'Interchange Profile'                                                   ]
    ARRAY[106] = ['83'  , 'Template'                                                              ]
    ARRAY[107] = ['84'  , 'File (DF) Name'                                                        ]
    ARRAY[108] = ['86'  , 'Script Command'                                                        ]
    ARRAY[109] = ['87'  , 'Priority Indicator'                                                    ]
    ARRAY[110] = ['88'  , 'File Identifier (SFI)'                                                 ]
    ARRAY[111] = ['89'  , 'Code'                                                                  ]
    ARRAY[112] = ['8A'  , 'Response Code'                                                         ]
    ARRAY[113] = ['8C'  , 'Risk Management Data Object List 1 (CDOL1)'                            ]
    ARRAY[114] = ['8D'  , 'Risk Management Data Object List 2 (CDOL2)'                            ]  
    ARRAY[115] = ['8E'  , 'Verification Method (CVM) List'                                        ]
    ARRAY[116] = ['8F'  , 'Authority Public Key Index'                                            ]
    ARRAY[117] = ['90'  , 'Public Key Certificate'                                                ]
    ARRAY[118] = ['91'  , 'Authentication Data'                                                   ]
    ARRAY[119] = ['92'  , 'Public Key Remainder'                                                  ]
    ARRAY[120] = ['93'  , 'Static Application Data'                                               ]
    ARRAY[121] = ['94'  , 'File Locator (AFL)'                                                    ]
    ARRAY[122] = ['95'  , 'Verification Results'                                                  ]
    ARRAY[123] = ['97'  , 'Certificate Data Object List (TDOL)'                                   ]
    ARRAY[124] = ['98'  , 'Certificate (TC) Hash Value'                                           ]
    ARRAY[125] = ['99'  , 'Personal Identification Number (PIN) Data'                             ]
    ARRAY[126] = ['9A'  , 'Date'                                                                  ]
    ARRAY[127] = ['9B'  , 'Status Information'                                                    ]
    ARRAY[128] = ['9C'  , 'Type'                                                                  ]
    ARRAY[129] = ['9D'  , 'Definition File (DDF) Name'                                            ]
    ARRAY[130] = ['9F45', 'Data Authentication Code'                                              ]
    ARRAY[131] = ['A5'  , 'Control Information (FCI) Proprietary Template'                        ]
    ARRAY[132] = ['9F57', 'Issuer Country Code'                                                   ]
    ARRAY[133] = ['9F39', 'Point-of-Service (POS) Entry Mode'                                     ]
    ARRAY[134] = ['9F73', 'Currency Conversion Factor'                                            ]
    ARRAY[135] = ['9F42', 'Application Currency Code'                                             ]
    ARRAY[136] = ['9F56', 'Issuer Authentication Indicator'                                       ]
    ARRAY[137] = ['9F20', 'Track 2 Discretionary Data'                                            ]
    ARRAY[138] = ['DF01', 'Reference PIN'                                                         ]
    ARRAY[139] = ['9F36', 'Application Transaction Counter (ATC)'                                 ]
    ARRAY[140] = ['9F4F', 'Log Format'                                                            ]
    ARRAY[141] = ['5F50', 'Issuer URL'                                                            ]
    ARRAY[142] = ['9F5A', 'Issuer URL2'                                                           ]
    ARRAY[143] = ['9F53', 'Consecutive Transaction Limit (International)'                         ]
    ARRAY[144] = ['9F54', 'Cumulative Total Transaction Amount Limit'                             ]
    ARRAY[145] = ['9F55', 'Geographic Indicator'                                                  ]

    def __init__(self):
        pass

    def get_description_emv(self, tag):
        for i in range(0,len(self.ARRAY)):
            if (self.ARRAY[i][0] == tag):
                return self.ARRAY[i][1]

    def has_another_byte(self, tag_byte):
        sum_bits = 0
        for bit in range(BIT_0,BIT_5):
            if tag_byte & 1 << bit:
                sum_bits = sum_bits + 1 
        # has another byte?
        if sum_bits == 5:
            return True
        else:
            return False

    def parse_tlv(self, str_emv):
        ini = 0;
        end = 2
        c = len(str_emv)
        while end < c :
            #Tag
            if self.has_another_byte(int(str_emv[ini:end], 16)):
                end = end + 2
            tag = str_emv[ini:end]
            ini = end
            end = end + 2
            #length
            length = int(str_emv[ini:end],16) * 2
            ini = end
            end = length + end
            #Value
            val = str_emv[ini:end]
            ini = end
            end = end + 2
            #Print TLV
            des = self.get_description_emv(tag)
            print("\t\t<Tag: 0x{:04X}> [{}] -> {}".format(int(tag,16), val, des))