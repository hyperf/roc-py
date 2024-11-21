from roc.packet import Packet
import struct


class Packer:
    def pack(self, packet: Packet):
        return struct.pack("I", packet.len()).decode() + struct.pack("I", packet.id).decode() + packet.body

    def unpack(self, raw: str):
        id = struct.unpack("I", raw[4:8].encode())[0]
        body = raw[8:]
        return Packet(int(id), body)
