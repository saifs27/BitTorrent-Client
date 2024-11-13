INTEGER_START = 'i'
LIST_START = 'l'
DICT_START  = 'd'
END = 'e'
STRING_START = '0123456789'
STRING_SEP = ':'

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
        if c == DICT_START:
            return self.decode_dict()
        if c in STRING_START:
            return self.decode_string()
        if c == END:
            return None
        raise ValueError("Cannot parse type")

    def decode_list(self):
        res = []
        self.ptr += 1
        while self.data[self.ptr] != END:
            i = self.decode()
            res.append(i)
        return res
             
    def decode_dict(self):
        res = {}
        self.ptr += 1
        while self.data[self.ptr] != END:
            key = self.decode()
            value = self.decode()
            res[key] = value
        return res
    
    def decode_int(self):
        res = ""
        self.ptr += 1
        while self.data[self.ptr] != END:  
            res += self.data[self.ptr]
            self.ptr += 1
        self.ptr += 1
        return int(res)

    def decode_string(self):
        res = ""
        str_size = ""
        while self.data[self.ptr] != STRING_SEP :
            str_size += self.data[self.ptr]
            self.ptr += 1
        str_size = int(str_size)
        self.ptr += 1

        for _ in range(str_size):
            res += self.data[self.ptr]
            self.ptr += 1


        return res



class Encoder():
    def __init__(self, data):
        self.data = data
        self.ptr = 0

    def encode(self):
        return self._encode(self.data)
        
    def encode_int(self, integer: int):
        return "i" + str(integer)  + "e"
    
    def encode_string(self, string: str):
        string_size = len(string)
        return f"{string_size}:{string}"
    
    def encode_list(self, list: list):
        list_items="l"
        for i in list:
            list_items += self._encode(i)    
        return f"{list_items}e"
    
    def encode_dict(self, dictionary: dict):
        dict_items = "d"

        for key, value in dictionary.items():
            dict_items += self._encode(key)
            dict_items += self._encode(value)
            
        return f"{dict_items}e"
     
    def _encode(self, i):
            if isinstance(i, int):
                return self.encode_int(i)
            if isinstance(i, str):
                return self.encode_string(i)
            if isinstance(i, list):
                return self.encode_list(i)
            if isinstance(i, dict):
                return self.encode_dict(i)
            raise TypeError("Unsupported type. Must be int, string, list, or dictionary")

            
 
