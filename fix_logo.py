from PIL import Image, ImageDraw
import math

def fix_logo(path):
    src = Image.open(path).convert('RGBA')
    w, h = src.size
    px = src.load()

    black_pts = [
        (x, y)
        for y in range(h)
        for x in range(w)
        if px[x, y][0] < 40 and px[x, y][1] < 40 and px[x, y][2] < 40
    ]

    cx = sum(p[0] for p in black_pts) / len(black_pts)
    cy = sum(p[1] for p in black_pts) / len(black_pts)
    radius = max(math.hypot(x - cx, y - cy) for x, y in black_pts) - 2

    size = int(radius * 2)
    out = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size - 1, size - 1), fill=255)

    shifted = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    spx = shifted.load()
    for y in range(size):
        for x in range(size):
            sx = int(x + cx - radius)
            sy = int(y + cy - radius)
            if sx < 0 or sy < 0 or sx >= w or sy >= h:
                continue
            r, g, b, a = px[sx, sy]
            if r > 160 and g > 160 and b > 160:
                spx[x, y] = (255, 255, 255, 255)
            elif r < 120 and g < 120 and b < 120:
                spx[x, y] = (0, 0, 0, 255)

    out = Image.composite(shifted, out, mask)
    out.save(path)
    print(f'Fixed logo saved: {path} ({size}x{size})')

if __name__ == '__main__':
    fix_logo('logo.png')
