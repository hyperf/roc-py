from roc.packet import Packet
import struct


class Packer:
    def pack(self, packet: Packet):
        return struct.pack("I", packet.len()).hex() + struct.pack("I", packet.id).hex() + packet.body

    def unpack(self, raw: str):
        id = struct.unpack("I", bytes.fromhex(raw[4:8]))[0]
        body = raw[8]
        return Packet(int(id), body)
