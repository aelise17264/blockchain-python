from backend.util.hex_to_binary import hex_to_binary

def test_htb():
    og_number = 789
    hex_number = hex(og_number)[2:]
    binary_number = hex_to_binary(hex_number)

    assert int(binary_number, 2) == og_number