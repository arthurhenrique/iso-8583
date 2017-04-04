from struct_iso8583 import BitmapIso

class ParserMessageIso:
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

    def get_parsed_mti(self, ini = 0):
        end = 4
        return self.message_iso[ini:end]
    
    def get_parsed_bitmap(self, ini = 4):
        end = ini + 16
        bitmap = int(self.message_iso[ini:end], 16)
        self.list_bitmap.append(bitmap)
        if BitmapIso.has_another_bitmap(bitmap):
            ini = ini + 16
            end = end + 16
            self.get_bitmap(ini)
        return self.list_bitmap

    def get_parsed_data_elements(self):
        return self.message_iso[len(self.list_bitmap):-1]