br = "\n----------------------------------------------------------------------------\n"

def log_iso(obj):
    obj_t = str(type(obj)).split('.')[1].replace('\'>','')
    print("{} class {} - test".format(br,obj_t))

def print_iso(str_obs, value):
    print("<",str_obs,">\n\t", value)

def get_hex(obj):
    #in case of list
    if "list" in str(type(obj)):
        l_obj = []
        for x in range(0,len(obj)):
            l_obj.append(format(obj[x], '02X'))
        return l_obj
    #in case of number real or integer
    if "float" or "int" or "double" in str(type(obj)):
        return format(obj, '02X')