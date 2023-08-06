def to_str(bytes_or_str): # str == unicode
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

a = b'\x45\x44\x50\x52\x45\x53\x53\x4f' # b'EDPRESSO'

print( to_str(a))
print( to_bytes(a))