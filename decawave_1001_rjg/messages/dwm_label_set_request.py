from .tlv_message import TlvMessage


class DwmLabelSetRequest(TlvMessage):
    def __init__(self, label):
        value = bytes(label, 'utf-8')
        super().__init__(bytes([0x1d, len(value)]) + value)
