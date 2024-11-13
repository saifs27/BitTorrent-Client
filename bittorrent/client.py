import asyncio
from dataclasses import dataclass

class Client:
    connection: int
    choked: bool
    bitfield: int
    peer: int    