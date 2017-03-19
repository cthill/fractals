import colorsys

size = 256

def hsv2rgb(h,s,v):
    return tuple(int(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))


palette = []
for i in range(size):
    h = 360 * (i/float(size - 1))
    s = 0.0
    v = 0.0
    if i > 3:
        s = 1.0
        v = 1.0
    palette.append(hsv2rgb(h, s, v))

palette.reverse()
for c in palette:
    print '(%s,%s,%s),'%c ,
