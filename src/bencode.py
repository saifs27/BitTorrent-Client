
INTEGER_START = b'i'
LIST_START = b'l'
DICT_START  = b'd'
END = b'e'
STRING_START = b'0123456789'
STRING_SEP = b':'



class Decoder():
    def __init__(self, data: str):
        self.data = data
        self.ptr = 0
    
    def decode(self):
        c: str = self.data[self.ptr]
        if c == INTEGER_START:
            return self.decode_int()
        if c == LIST_START:
            return self.decode_list()
        if c == DICT_START():
            return self.decode_dict()
        if c in STRING_START:
            return self.decode_string()
        if c == END:
            return None

    def decode_list(self):
        res = []
        i = 1
        while self.data[self.ptr + i] != END:
            if self.data[self.ptr + i] == INTEGER_START:
                res.append(self.decode_int())
            if self.data[self.ptr + i] == STRING_START:
                ...
            
    
    def decode_dict(self):
        res = {}

    def decode_int(self):
        res = ""
        i = 1
        while self.data[self.ptr + i] != END:  
            res += self.data[self.ptr + i]
            i += 1
        self.ptr += i
        return int(res)

    def decode_string(self):
        res = ""
        i = 2
        while self.data[self.ptr + i] != END:
            res += self.data[self.ptr+i]
            i += 1
        self.ptr += i

        return res
        
        



class Encoder():
    def __init__(self):
        ...
    