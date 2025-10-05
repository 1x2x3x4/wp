import apng

apng_file = "misc40.png"
apng_data = apng.APNG.open(apng_file)

ascii_chars = ""
for i, (_, control) in enumerate(apng_data.frames):
    if 32 <= control.delay <= 127:  # 只取可见ASCII字符范围
        ascii_char = chr(control.delay)
        ascii_chars += ascii_char
        print(f"Frame {i+1} delay: {control.delay} ({ascii_char})")  # 循环里打印

print("拼接的ASCII字符:", ascii_chars)
