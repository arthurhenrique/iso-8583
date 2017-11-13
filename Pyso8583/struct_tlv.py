
str_emv = "3129F2701809F3602018E9F2608B12C8EC8650ACC949F10050000000188950500800010009B02E8009F01060000000072259F41030000345F360102DF7A0101DF7B03000000DF7C0400000000DF68050000000000DF6104205AD928DF63080000000040200001DF6206000000060566DF6003005763DF7201009F080202059A031709069F21031202248104000271795F20064D4E493032379F45020000"

str_emv = str_emv[3:]

ini = 0;
end = 2

c = len(str_emv)

while end < c :
    #Tag
    if has_another_byte(int(str_emv[ini:end], 16)):
        end = end + 2
    tag = str_emv[ini:end]
    ini = end
    end = end + 2

    #Length
    len = int(str_emv[ini:end],16) * 2
    ini = end
    end = len + end

    #Value
    val = str_emv[ini:end]
    ini = end
    end = end + 2

    #Print
    print("tag: "   , tag)
    print("length: ", len)
    print("value:"  , val)
    print("----------------")
