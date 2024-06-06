from .tlv_message import TlvMessage


class DwmTagConfigRequest(TlvMessage):
    def __init__(self, ble_en: bool):
        value = 0x42 # Location engine enabled and active mode
        if ble_en:
            value = value | 0x08
        super().__init__(bytes([0x05, 2, value, 0x00]))
