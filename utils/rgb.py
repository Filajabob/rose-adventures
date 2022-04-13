def init(_enable_colors):
    global enable_colors
    enable_colors = bool(_enable_colors)

def rgb(r, g, b):
    if enable_colors:
        return f"\033[38;2;{r};{g};{b}m"