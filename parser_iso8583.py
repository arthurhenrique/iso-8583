from struct_iso8583 import BitmapIso
from utils import *
"""
Class `ParserMessageIso` that parse the message from format ISO-8583
"""
class ParserMessageIso:
    # Property `message_iso` is a message type in ISO format ( string ), 
    # that contains 3 basics structs( MTI, Bitmap and Data Elements )
    message_iso = ""

    # Property `mti` contains message type Indicator
    mti = ""

    # Property `bitmap` List of bitmap
    bitmap = []

    # Property `data_element` data elements
    data_element = ""

    # Constructor ParserMessageIso
    def __init__(self, message_iso = ""):
        self.message_iso = message_iso
        self.set_mti()
        self.set_bitmap()
        self.set_data_element()
    
    # Set original Message in ISO-8583 format
    def set_message_iso(self, message_iso = ""):
        self.message_iso = message_iso

    # Get the original Message in ISO-8583 format
    def get_message_iso(self):
        return self.message_iso

    # Set Message Type Indicator, with initial position in 0
    def set_mti(self, ini = 0):
        end = 4
        self.mti = self.message_iso[ini:end]

    # Get Message Type Indicator properties
    def get_mti(self):
        return self.mti

    # Set a list of Bitmap, starting in position 4 in string. Recursive function
    def set_bitmap(self, ini = 4):
        end = ini + 16
        bitmap = int(self.message_iso[ini:end], 16)
        # Add to the list of bitmaps while the primary bit is 1
        self.bitmap.append(bitmap)
        if BitmapIso.has_another_bitmap(bitmap):
            ini = ini + 16
            end = end + 16
            self.set_bitmap(ini)

    # Get Bitmap property
    def get_bitmap(self):
        return self.bitmap

    # Set all the data elements in orinal format
    def set_data_element(self):
        ini = 0
        ini = ini + len(self.mti)
        ini = ini + len(self.bitmap) * 16
        end = -1
        self.data_element = self.message_iso[ini:end]

    # Get all the data element in original format
    def get_data_element(self):
        return self.data_element
