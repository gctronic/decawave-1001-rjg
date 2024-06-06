from .tlv_message import TlvMessage


class DwmPositionSetRequest(TlvMessage):
    def __init__(self, x, y, z):
        value = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        value[0] = x&0xFF
        value[1] = (x>>8)&0xff
        value[2] = (x>>16)&0xff
        value[3] = (x>>24)&0xff
        value[4] = y&0xFF
        value[5] = (y>>8)&0xff
        value[6] = (y>>16)&0xff
        value[7] = (y>>24)&0xff
        value[8] = z&0xFF
        value[9] = (z>>8)&0xff
        value[10] = (z>>16)&0xff
        value[11] = (z>>24)&0xff
        value[12] = 100
        #print(bytes([0x01, 0x0D]+value))
        super().__init__(bytes([0x01, 0x0D] + value))
