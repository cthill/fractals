import math
from PIL import Image, ImageDraw

points = [[(0.0,1.0), (1.0, 1.0), (0.5, 1 - 0.5 * math.sqrt(3))]]

def midpoint(a, b):
    return ((a[0] + b[0])/2, (a[1] + b[1])/2)

def iterate(points):
    out = []

    for p in points:
        p01 = midpoint(p[0],p[1])
        p02 = midpoint(p[0],p[2])
        p12 = midpoint(p[1],p[2])

        out.append([p[0], p01, p02])
        out.append([p[1], p01, p12])
        out.append([p[2], p02, p12])

    return out

def drawPointList(l, frame, name, color):
    # draw set
    draw = ImageDraw.Draw(frame)
    padding = 16

    aspectRatio = 0.86602540595

    # set the draw scale
    drawScale = frame.size[0] * aspectRatio

    # since the frame is square and the aspect ratio is less than 1,
    # we need to add some x offset to center the fractal
    xOffset = (frame.size[0] - drawScale) / 2

    # account for padding
    drawScale -= padding * 2

    def drawLine(a, b):
        x1 = padding + drawScale * a[0]
        x2 = padding + drawScale * b[0]
        y1 = padding + drawScale * a[1]
        y2 = padding + drawScale * b[1]
        draw.line([x1 + xOffset, y1, x2 + xOffset, y2], fill=color, width = 1)

    for i in range(0, len(l) - 1):
        drawLine(l[i], l[i+1])

    #special case last point
    drawLine(l[-1], l[0])

    frame.save(name)

def blank(w, h):
    img = Image.new('RGB', (w,h))
    img.paste((255, 255, 255), [0,0, img.size[0], img.size[1]])
    return img

iterations = 7
lastFrame = blank(1024, 1024)
for i in range(iterations):
    for pl in points:
        drawPointList(pl, lastFrame, 'img/frame%s.png' % i, (255, 0,0))
    points = iterate(points)
