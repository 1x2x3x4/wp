import base64
#在执行过程需要将路径移至当前文件夹中

with open('./base.txt', 'r') as f:  #读取base.txt文件
    contents = f.read()  # 读取文件内容
    i = 0  # 初始化计数器
    while True:
        try:
            i += 1
            contents = base64.b64decode(contents)  # 尝试进行Base64解码
            print(f"第{i}次解码成功")
        except Exception as e:
            print(f"解码失败，解码次数: {i}")
            print(f"解码后的内容：{contents}")
            break  # 解码失败时退出循环
