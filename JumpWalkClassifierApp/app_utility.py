# Layout
DEFAULT_HEIGHT = 480
DEFAULT_WIDTH = 1440
DEFAULT_PADDING = 25

# Font
DEFAULT_FONT = ('Arial', 16)

# Colors
PRIMARY = '#000000'
SECONDARY = '#606060'
POSITIVE = '#557F51'
DEFAULT_BACKGROUND = '#E4E2E2'
POSITIVE_BACKGROUND = '#EEF9EC'

# Create a rounded rectangle on the given canvas
def rounded_rectangle(canvas, pad_x, pad_y, width, height, radius, **kwargs):
    points = [pad_x + radius, pad_y,
              pad_x + radius, pad_y,
              width - radius, pad_y,
              width - radius, pad_y,
              width, pad_y,
              width, pad_y + radius,
              width, pad_y + radius,
              width, height - radius,
              width, height - radius,
              width, height,
              width - radius, height,
              width - radius, height,
              pad_x + radius, height,
              pad_x + radius, height,
              pad_x, height,
              pad_x, height - radius,
              pad_x, height - radius,
              pad_x, pad_y + radius,
              pad_x, pad_y + radius,
              pad_x, pad_y]
    return canvas.create_polygon(points, **kwargs, smooth=True)