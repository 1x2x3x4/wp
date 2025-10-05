import struct
import zlib

def read_png_chunks(file_path):
    chunks = []
    with open(file_path, 'rb') as f:
        # Check PNG signature
        signature = f.read(8)
        if signature != b'\x89PNG\r\n\x1a\n':
            raise ValueError("Not a valid PNG file")

        while True:
            # Read chunk length
            length_data = f.read(4)
            if len(length_data) == 0:
                break
            length = struct.unpack('>I', length_data)[0]

            # Read chunk type
            chunk_type = f.read(4).decode('ascii')

            # Read chunk data
            chunk_data = f.read(length)

            # Read CRC
            stored_crc_data = f.read(4)
            stored_crc = struct.unpack('>I', stored_crc_data)[0]

            # Add chunk to list
            chunks.append((chunk_type, chunk_data, stored_crc))
            
    return chunks

def calculate_crc(chunk_type, chunk_data):
    crc = zlib.crc32(chunk_type.encode('ascii'))
    crc = zlib.crc32(chunk_data, crc)
    return crc & 0xffffffff

def check_crc(file_path):
    s=''
    chunks = read_png_chunks(file_path)
    for chunk_type, chunk_data, stored_crc in chunks:
        if chunk_type == 'IDAT':
            calculated_crc = calculate_crc(chunk_type, chunk_data)
            if calculated_crc == stored_crc:
                #print(1, end='')
                s="".join([s, '1'])
            else:
                #print(0, end='')
                s="".join([s, '0'])
    return s
    
# 使用示例
txt=check_crc('misc44.png')
print(txt)
# 每8位一个数字
data = []
index = 0
while index < len(txt):
    if txt[index] != '\n':
        data.append(int(txt[index:index+8], 2))
        index += 8
    else:
        index += 1
print(data)
# 数字列表转为字符
ascii_chars = [chr(num) for num in data]
ascii_string = ''.join(ascii_chars)
print(ascii_string)
