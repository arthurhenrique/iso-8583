#class Tag:


#class Length:


#class Value:

BIT_5 = 5
BIT_0 = 0

s = "DF7A01019F360202f7DF61041F76AE73"
s = "DF61041F76AE73"

def has_another_byte(tag_byte):
    sum_bits = 0
    for bit in range(BIT_0,BIT_5):
        if tag_byte & 1 << bit:
            sum_bits = sum_bits + 1 
    # has another byte?
    if sum_bits == 5:
        return True
    else:
        return False

len_byte = 2
tag_byte = int(s[:len_byte],16)
if has_another_byte(tag_byte):
    len_byte = 4
    tag_byte = int(s[:len_byte],16)

tag    = hex(tag_byte)
ini = len_byte
end = len_byte + 2
length = int(s[ini:end],16)
ini = end
end = end + length * 2
value  = str(s[ini:end])

print(tag)
print(length)
print(value)