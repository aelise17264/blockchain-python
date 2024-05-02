from backend.util.crypto_hash import crypto_hash

HEX_TO_BINARY_CONVERSION_TABLE = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111'
}

def hex_to_binary(hex_string):
    binary_string = ''
    
    for char in hex_string:
        binary_string += HEX_TO_BINARY_CONVERSION_TABLE[char]
    
    return binary_string

def main():
    number = 451
    hex_number = hex(number)[2:]
    # to get a slice of the hex number leaving off the 0x
    print(f'hex_number: {hex_number}')

    binary_number = hex_to_binary(hex_number)
    print(f'binary number: {binary_number}')

    og_num = int(binary_number, 2)
    # the 2 specifies that the input is a binary string
    print(f'original number: {og_num}')

    hex_to_binary_crypto_hash = hex_to_binary(crypto_hash('test-data'))
    print(f'hex to binary crypto hash: {hex_to_binary_crypto_hash}')

if __name__ == '__main__':
    main()