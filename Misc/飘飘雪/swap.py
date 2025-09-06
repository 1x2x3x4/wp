def swap(hex_data):  
    result = b''  
    for temp in hex_data:  
                 
        # 互换高四位和第四位  
        swapped = ((temp & 0xF0) >> 4) | ((temp & 0x0F) << 4)
        ret = swapped.to_bytes(1, byteorder="big")
        #print(ret)
        # 将结果重新转换为16进制字符串  
        result+=ret
    return result  

# 读取文件的16进制内容  
with open('./key', 'rb') as file:  
    hex_data = file.read()  

swapped_hex_data = swap(hex_data)  
print(swapped_hex_data)

# 可选：将结果写回文件  
with open('data_swapped.hex', 'wb') as file:  
    file.write(swapped_hex_data)
