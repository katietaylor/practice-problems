matrix = [['r', 'r', 'b', 'b', 'g'],
          ['r', 'r', 'b', 'g', 'g'],
          ['g', 'g', 'g', 'g', 'w'],
          ['g', 'w', 'g', 'g', 'b']]


def get_color(y, x):
    color = matrix[y][x]
    if color is None:
        return None
    else:
        return color


def color_fill(y, x, new_color, start_color=None):

    if start_color is None:
        start_color = get_color(y, x)

    if x < 0 or x > 4 or y < 0 or y > 3:
        return

    if start_color != get_color(y, x):
        return

    else:
        matrix[y][x] = new_color

    color_fill(y, x + 1, new_color, start_color)
    color_fill(y, x - 1, new_color, start_color)
    color_fill(y + 1, x, new_color, start_color)
    color_fill(y - 1, x, new_color, start_color)
