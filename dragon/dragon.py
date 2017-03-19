import math
from PIL import Image, ImageDraw

points = [(0.0, 0.0), (0.5, 0.5), (1.0, 0.0)]

cw = True
def iterate(l):
    finalList = []
    global cw

    for i in range(len(l) - 1):
        a = l[i]
        b = l[i+1]
        finalList.append(a)

        length = math.sqrt(abs(a[0] - b[0])**2 + abs(a[1] - b[1])**2)
        height = 0.5 * length
        midpoint = ((a[0] + b[0])/2, + (a[1] + b[1])/2)
        x = b[0] - a[0]
        y = a[1] - b[1]

        # fix angle calculations
        if x != 0.0:
            angle = math.atan(y/x)
        else:
            if y > 0:
                angle = math.pi/2
            else:
                angle = -math.pi/2

        if x < 0:
            angle -= math.pi

        # for twisted effect
        #angle += .05 * angle

        if cw:
            p = (midpoint[0] + height * math.sin(angle), midpoint[1] + height * math.cos(angle))
        else:
            p = (midpoint[0] - height * math.sin(angle), midpoint[1] - height * math.cos(angle))


        finalList.append(p)

        # reverse direction for next segment
        cw = not cw

    # add last point
    finalList.append(l[-1])

    return finalList


def drawPointList(l, frame, name, color):
    # draw set
    draw = ImageDraw.Draw(frame)
    padding = 0

    # set the draw scale
    drawScale = frame.size[0] / 1.6

    yOffset = frame.size[0]/3
    xOffset = 1*frame.size[0]/4

    # account for padding
    drawScale -= padding * 2

    def drawLine(a, b):
        x1 = drawScale * a[0]
        x2 = drawScale * b[0]
        y1 = drawScale * a[1]
        y2 = drawScale * b[1]
        draw.line([x1 + xOffset, y1 + yOffset, x2 + xOffset, y2 + yOffset], fill=color, width = 1)

    for i in range(0, len(l) - 1):
        drawLine(l[i], l[i+1])

    frame.save(name)

def blank(w, h):
    img = Image.new('RGB', (w,h))
    img.paste((255, 255, 255), [0,0, img.size[0], img.size[1]])
    return img

iterations = 18
for i in range(iterations):
    drawPointList(points, blank(1024, 1024), 'img/frame%s.png' % i, (255,0,0))
    cw = True
    if (i < iterations - 1):
        points = iterate(points)
