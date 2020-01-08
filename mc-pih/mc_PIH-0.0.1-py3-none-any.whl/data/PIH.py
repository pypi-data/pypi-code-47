from cv2 import imread, imwrite


def txt2Img(photoDir, message, outputFile):
    photo_data = imread(photoDir)

    if outputFile.split('.')[-1].lower() != 'png':
        print()
        raise Exception('输出文件类型只能是png，否则将导致压缩丢失')

    def to_bin(inf):
        maxLen = 0
        new = ''
        for i in inf:
            treated = str(bin(ord(i))).replace('0b', '')
            if maxLen < len(treated):
                maxLen = len(treated)
            new += treated + ' '
        return [new[:-1], maxLen]

    def int_to_bin(inf):
        con = str(bin(int(str(inf), 10))).replace('0b', '')
        return con

    # 分析编码信息的总长度
    totalLen = int_to_bin(len(message))
    # 最大长度达到1000000+
    totalLenPointer = int_to_bin(len(totalLen))
    # 将格式转换为5
    totalLenPointer = str(pow(10, 5 - len(totalLenPointer)))[1:] + totalLenPointer

    # 将编码信息转换成二进制形式
    BinaryInf_temp = to_bin(message)
    maxLen = BinaryInf_temp[1]
    BinaryInf = BinaryInf_temp[0].split(' ')
    del BinaryInf_temp  # release memory

    # 将所有项目转移到具有最大元素的项目
    for index, nowInf in enumerate(BinaryInf):
        BinaryInf[index] = str(pow(10, maxLen - len(nowInf)))[1:] + nowInf

    # 最大ASCII长度：31
    # 使用5个长度作为通用
    lenPerInf = int_to_bin(maxLen)
    lenPerInf = str(pow(10, 5 - len(lenPerInf)))[1:] + lenPerInf

    # 撰写项目
    composedInf = lenPerInf + totalLenPointer + totalLen + ''.join(BinaryInf)

    h, w = photo_data.shape[:2]

    flag = True

    # 检查大小限制
    if h * w < len(composedInf):
        raise Exception('图片无法存储文本！')

    # 写入照片
    for x in range(h):
        for y in range(w):
            nowAt = x * h + y
            if nowAt == len(composedInf):
                flag = False
                break
            # even as flat, odd as 1
            photo_data[x, y, 0] += photo_data[x, y, 0] % 2 - int(composedInf[nowAt])
        if not flag:
            break

    imwrite(outputFile, photo_data)


def img2Txt(photoDir):
    photo_data = imread(photoDir)

    if photoDir.split('.')[-1].lower() != 'png':
        raise Exception('如果输入文件类型不是png，则会发生错误')

    def to_string(inf):
        return chr(int(inf, 2))

    def bin_to_int(inf):
        place = inf.find('1')
        if place == -1:
            return 0
        else:
            # print(inf[place:])
            return int(inf[place:], 2)

    h, w = photo_data.shape[:2]
    composeData = ''
    # 在程序中不调用警告
    totalLenPointer = dataLen = lenPerInf = 1
    flag = False

    for x in range(h):
        for y in range(w):
            nowAt = x * h + y
            # 对于无数据索引
            if nowAt < 10:
                composeData += str(photo_data[x, y, 0] % 2)
                if nowAt == 9:
                    lenPerInf = bin_to_int(composeData[:5])
                    totalLenPointer = bin_to_int(composeData[5:])

            # 对于dataLen参数
            elif nowAt == 10 + totalLenPointer:
                dataLen = bin_to_int(composeData[10:])
                # 清空数据容器以准备包含二进制数据
                composeData = ''
                
                
                composeData += str(photo_data[x, y, 0] % 2)

            else:
                if nowAt == dataLen * lenPerInf + totalLenPointer + 10:
                    flag = True
                    break
                composeData += str(photo_data[x, y, 0] % 2)
        if flag:
            break

    message = ''

    # 传回字符串
    for i in range(0, len(composeData), lenPerInf):
        message += to_string(composeData[i:i + lenPerInf])

    return message

