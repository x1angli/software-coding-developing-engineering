import struct

class EncodingFactory:

    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.base = len(alphabet)

    def encode(self, data):
        n = int.from_bytes(data, byteorder='big') # Since byteorder is "big", the most significant byte is at the beginning of the byte array
        result = ''
        while n > 0:
            n, r = divmod(n, self.base)
            result = self.alphabet[r] + result
        return result

    def decode(self, s):
        n = 0
        while len(s) > 0:
            n = n * len(self.alphabet) + self.alphabet.find(s[0])
            s = s[1:]
        return n.to_bytes((n.bit_length() + 7) // 8 , 'big') or b'\0'



class MyBase64:

    def __init__(self, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'):
        self.alphabet = alphabet
        self.base = 64

    def encode(self, data):
        # add a right zero pad to make this string a multiple of 3 characters
        padding = ''
        paddinglen = -len(data) % 3
        for i in range(paddinglen):
            padding += '='
            data += b'\0'

        result = ''
        for i in range(0, len(data), 3):

            # we add newlines after every 76 output characters, according to the MIME specs
            resultlen = len(result)
            if resultlen > 0 and ((resultlen // 3 * 4) % 76 == 0):
                resultlen += '\n'

            n = int.from_bytes(data[i: i+3], byteorder='big', signed=False)
            (n1, n2, n3, n4)  = (n >> 18) & 63, (n >> 12) & 63, (n >> 6) & 63, n & 63
            result += (self.alphabet[n1] + self.alphabet[n2] + self.alphabet[n3] + self.alphabet[n4])

        if (paddinglen > 0):
            result[-paddinglen:] = padding
        result += '\n'

        return result.encode('ascii')


# base63 is used to generate a propretary serial number. It only supports alphanumeric chars plus dash "-"
base63 = EncodingFactory('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-')

base36 = EncodingFactory('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')


def test():
    input = b'43afa433a'
    print(MyBase64().encode(input))
    import base64
    print(base64.encodebytes(input))

    encoded = base63.encode(b'data to be encoded')
    print(encoded)
    decoded = base63.decode(encoded)
    print(decoded)
    
if __name__ == '__main__':
    test()
    
