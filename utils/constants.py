from .rgb import rgb, init

print_colors = input("Enable colors? (Y/n) ").strip() == 'Y'
init(print_colors)

class Constants:
    WHITE = rgb(255, 255, 255)

    RED = rgb(255, 0, 0)
    GREEN = rgb(0, 255, 0)
    BLUE = rgb(0, 0, 255)

    CYAN = rgb(0, 255, 255)
    PURPLE = rgb(255, 0, 255)