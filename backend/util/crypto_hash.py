import hashlib
import json

# def stringify(data):
#     return json.dumps(data)

def crypto_hash(*args):
    """
    Return a sha-256 hash of the given arguments
    Secure Hash Algorithm in 256 bits(fixed size)
    if even one character is changed a completely new has will be generated
    only possible to crack through guess & check
    """
    stringified_args = sorted(map(lambda data: json.dumps(data) , args))
    """
    sorted makes sure we get the same has when we have the same inputs but in diff order
    """
    # print(f'args: {stringified_args}')
    joined_data = ''.join(stringified_args)
    # print(f'joined_data: {joined_data}')


    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()
"""
data must be turned into a byte string before encoded through the sha256 method
encode is specific to String type
hex digest gets the unique string output of the resulting hash object
"""

def main():
    print(f"crypto_hash('one', 2, [3]): {crypto_hash('one', 2, [3])}")
    print(f"crypto_hash(2, 'one', [3]): {crypto_hash(2, 'one', [3])}")

if __name__ == '__main__':
    main()