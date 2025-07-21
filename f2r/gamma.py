from enum import Enum
from dataclasses import dataclass, field
from typing import List
import socket
import os
import struct

class _FrameType(Enum):
    BUZZER_PERFORM = 3
    POWER_MANAGER_SET_CONFIG = 66

socket_path = "/var/run/gamma1000d/service.socket"

@dataclass
class _Frame:
    type: _FrameType = field(init=False)  # Prevent from being set in constructor


class GammaClient:
    def __init__(self):
        try:
            self.client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            # Connect to the server
            self.client.connect(socket_path)
        except FileNotFoundError:
             raise NameError('Failed to connect, check if gamma1000d service is running')
        except ConnectionRefusedError:
             raise NameError('Failed to connect, check if gamma1000d service is running')
             
    def __del__(self):
        if self.client is None:
            self.client.close()

    def send(self, data):
        self.client.sendall( data )

    def receive(self, ammount = 1):
        return self.client.recv( ammount )

@dataclass    
class PowerManagerConfig(_Frame):
    active: bool
    lowBrightnessTime: int
    standbyTime: int
    shutdownTime: int
    def __post_init__(self):
        self.type = _FrameType.POWER_MANAGER_SET_CONFIG

    def serialize(self) -> bytes:
        return struct.pack("<BBBBB", self.type.value, self.active, self.lowBrightnessTime, self.standbyTime, self.shutdownTime)

    def perform(self, client):
        client.send( self.serialize() )
        # Wait for the reply
        # 0 - for success
        return struct.unpack("<b", client.receive(1) )[0]


class BuzzerOp:
    CANCEL = 1
    PERFORM = 2
    PAUSE = 3
    LOOP = 4

@dataclass
class BuzzerSample:
    op: BuzzerOp
    amplitude: int = 0
    duration: int = 0
    def serialize(self) -> bytes:
        return struct.pack("<BHH", self.op, self.amplitude, self.duration)

@dataclass
class Buzzer(_Frame):
    samples: List[BuzzerSample] = field(default_factory=list)
    def __post_init__(self):
        self.type = _FrameType.BUZZER_PERFORM
    
    def serialize(self) -> bytes:
        result = struct.pack("<B", self.type.value)
        result += struct.pack("<B", len(self.samples))  # uint32 sample count
        for sample in self.samples:
            result += sample.serialize()
        return result    

    @staticmethod
    def cancel(client):
        a = Buzzer( samples = [BuzzerSample(op=BuzzerOp.CANCEL)] )
        client.send( a.serialize() )
        # Wait for the reply
        # 0 - for success
        return struct.unpack("<b", client.receive(1) )[0]


    def perform(self, client):
        client.send( self.serialize() )
        # Wait for the reply
        # 0 - for success
        return struct.unpack("<b", client.receive(1) )[0]



