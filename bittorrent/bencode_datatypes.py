from dataclasses import dataclass



@dataclass
class BencodeInfo:
    pieces: str
    piece_len: int
    len: int
    name: str

@dataclass
class BencodeTorrent:
    announce: str
    info: BencodeInfo

@dataclass
class TorrentFile:
    announce: str
    info_hash: list # Identifies file we want to download
    piece_hashes: list
    piece_len: int
    len: int
    name: str 
