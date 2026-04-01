import os
import math
from PIL import Image, ImageDraw, ImageFont

POSTS_DIR = os.path.join(os.path.dirname(__file__), "..", "Posts")
WATERMARK_TEXT = "PRAMOD B N"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def apply_watermarks(filepath):
    img = Image.open(filepath).convert("RGBA")
    w, h = img.size

    font_br_size = max(40, int(w * 0.035))
    font_br = ImageFont.truetype(FONT_PATH, font_br_size)

    font_diag_size = int(math.sqrt(w**2 + h**2) * 0.09)
    font_diag = ImageFont.truetype(FONT_PATH, font_diag_size)

    overlay = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    # 1. Bottom-right watermark
    bbox = draw.textbbox((0, 0), WATERMARK_TEXT, font=font_br)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    padding = int(w * 0.025)
    x = w - tw - padding
    y = h - th - padding
    shadow = max(2, font_br_size // 20)
    draw.text((x + shadow, y + shadow), WATERMARK_TEXT, font=font_br, fill=(0, 0, 0, 140))
    draw.text((x, y), WATERMARK_TEXT, font=font_br, fill=(255, 255, 255, 200))

    img = Image.alpha_composite(img, overlay)

    # 2. Diagonal watermark (one large, slightly transparent)
    diagonal = int(math.sqrt(w**2 + h**2))
    canvas = Image.new("RGBA", (diagonal, diagonal), (255, 255, 255, 0))
    draw2 = ImageDraw.Draw(canvas)
    bbox2 = draw2.textbbox((0, 0), WATERMARK_TEXT, font=font_diag)
    tw2, th2 = bbox2[2] - bbox2[0], bbox2[3] - bbox2[1]
    cx = (diagonal - tw2) // 2
    cy = (diagonal - th2) // 2
    draw2.text((cx, cy), WATERMARK_TEXT, font=font_diag, fill=(255, 255, 255, 130))

    angle = math.degrees(math.atan2(h, w))
    rotated = canvas.rotate(angle, expand=False)
    rx, ry = rotated.size
    cropped = rotated.crop(((rx - w) // 2, (ry - h) // 2, (rx - w) // 2 + w, (ry - h) // 2 + h))

    result = Image.alpha_composite(img, cropped)
    result.save(filepath, "PNG")


def main():
    posts_dir = os.path.abspath(POSTS_DIR)
    images = sorted(f for f in os.listdir(posts_dir) if f.lower().endswith(".png"))

    if not images:
        print("No PNG images found in Posts/")
        return

    for filename in images:
        filepath = os.path.join(posts_dir, filename)
        apply_watermarks(filepath)
        print(f"Watermarked: {filename}")

    print(f"\nDone. {len(images)} image(s) processed.")


if __name__ == "__main__":
    main()
