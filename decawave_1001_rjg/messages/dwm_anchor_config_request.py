from .tlv_message import TlvMessage


class DwmAnchorConfigRequest(TlvMessage):
    def __init__(self, initiator: bool, ble_en: bool):
        value = 0x02 # Active mode
        if initiator:
            value = value | 0x80
        if ble_en:
            value = value | 0x08
        super().__init__(bytes([0x07, 2, value, 0x00]))
