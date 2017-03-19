import math
from PIL import Image, ImageDraw

# use a list instead of set because order matters for the calculation
koch = [(0.0,0.3), (1.0, 0.3), (0.5, 0.3 + 0.5 * math.sqrt(3))]

def iterateSet(s):
    finalList = []
    def iteration(a, b):
        length = math.sqrt(abs(a[0] - b[0])**2 + abs(a[1] - b[1])**2)/3
        height = 0.5 * math.sqrt(3) * length
        midpoint = ((a[0] + b[0])/2, + (a[1] + b[1])/2)
        x = b[0] - a[0]
        y = a[1] - b[1]
        angle = math.atan(y/x)
        if (x < 0):
            # correct the angle calculation
            angle = angle + math.pi

        p2 = (midpoint[0] - height * math.sin(angle), midpoint[1] - height * math.cos(angle))

        p1 = ((b[0] + 2*a[0])/3, (b[1] + 2*a[1])/3)
        p3 = ((a[0] + 2*b[0])/3, (a[1] + 2*b[1])/3)
        return (p1, p2, p3)

    for i in range(len(s) - 1):
        finalList.append(s[i])
        newItems = iteration(s[i], s[i + 1])
        finalList.append(newItems[0])
        finalList.append(newItems[1])
        finalList.append(newItems[2])

    # special case last elm
    finalList.append(s[-1])
    newItems = iteration(s[-1], s[0])
    finalList.append(newItems[0])
    finalList.append(newItems[1])
    finalList.append(newItems[2])

    return finalList

def blank(w, h):
    img = Image.new('RGB', (w,h))
    img.paste((255, 255, 255), [0,0, img.size[0], img.size[1]])
    return img

def drawPointList(l, frame, name, color):
    # draw set
    draw = ImageDraw.Draw(frame)
    padding = 16

    # the aspect ratio of any koch fractal
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

def colorFade(c1, c2, percent):
    return (int(c1[0] * (1 - percent) + c2[0] * percent), int(c1[1] * (1 - percent) + c2[1] * percent), int(c1[2] * (1 - percent) + c2[2] * percent))

iterations = 7
#lastFrame = blank(1024, 1024)
for i in range(iterations):
    #drawPointList(koch, lastFrame, 'img/frame%s.png' % i, colorFade((255,0,0),(0,255,0), i/float(iterations - 1)))
    drawPointList(koch, blank(1024, 1024), 'img/frame%s.png' % i, (255,0,0))

    if (i < iterations - 1):
        koch = iterateSet(koch)
