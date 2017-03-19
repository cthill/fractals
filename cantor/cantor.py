from PIL import Image, ImageDraw

cantorSet = {0.0, 1.0}

def iterateSet(s):
    return {x/3.0 for x in s} | {(x/3.0 + 2.0/3.0) for x in s}

def blank(w, h):
    img = Image.new('RGB', (w,h))
    img.paste((255, 255, 255), [0,0, img.size[0], img.size[1]])
    return img

def drawPointList(l, frame, yOffset, name):
    # draw set
    draw = ImageDraw.Draw(frame)
    padding = 16
    lineWidth = (frame.size[0] - padding * 2)
    for i in range(0, len(l), 2):
        x1 = padding + lineWidth * l[i]
        x2 = padding + lineWidth * l[i+1]
        draw.line([x1, yOffset, x2, yOffset], fill=(255,0,0), width = 4)

    frame.save(name)

iterations = 10
cantorList = []
lastFrame = blank(1024, 1024)
for i in range(iterations):
    cantorList = list(cantorSet)
    cantorList.sort()

    drawPointList(cantorList, lastFrame, i * 32 + 16, 'img/frame%s.png' % i)

    # iterate set
    if (i < iterations - 1):
        cantorSet = iterateSet(cantorSet)
