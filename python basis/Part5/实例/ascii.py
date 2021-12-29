from PIL import Image
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type=int, default=459)
parser.add_argument('--height', type=int, default=570)

args = parser.parse_args()

IMG = args.file

WIDTH = args.width

HEIGHT = args.height

OUTPUT = args.output

ascii_char = list(
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0+1)/length

    return ascii_char[int(gray/unit)]


if __name__ == '__main__':

    # 打开并调整图片的宽和高
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    # 初始化输出的字符串
    txt = ""

    # 遍历图片中的每一行
    for i in range(HEIGHT):
        # 遍历该行中的每一列
        for j in range(WIDTH):
            # 将 (j,i) 坐标的 RGB 像素转为字符后添加到 txt 字符串
            txt += get_char(*im.getpixel((j, i)))
        # 遍历完一行后需要增加换行符
        txt += '\n'
    # 输出到屏幕
    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)
