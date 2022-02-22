""" 
需求
1，显示一个窗口。
2，我们要做到的功能有鼠标点击屏幕生成小球。
3，生成的小球大小随机，颜色随机，向随机方向移动，速度也随机。
4，大的球碰到小球时可以吃掉小球，吃掉后会变大。
5，球碰到边界会弹回去。
"""
import pygame


def main():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')
    screen.fill((224, 224, 224))
    pygame.display.flip()
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
