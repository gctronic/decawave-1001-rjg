from .tlv_message import TlvMessage


class DwmPanIdSetRequest(TlvMessage):
    def __init__(self, id):
        value = [id&0xff, (id>>8)&0xff]
        super().__init__(bytes([0x2e, 2] + value))
