from PIL import Image

def crop_logo(input_path, output_path):
    img = Image.open(input_path)
    
    # We want to crop out the gray border and everything outside it.
    # We can search for the black color bounding box.
    # Convert image to RGB just in case
    img = img.convert('RGB')
    
    width, height = img.size
    pixels = img.load()
    
    # Find bounding box of pixels that are dark (e.g. R,G,B all < 30)
    # This will find the black circle.
    left, top, right, bottom = width, height, 0, 0
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if r < 30 and g < 30 and b < 30:
                if x < left: left = x
                if x > right: right = x
                if y < top: top = y
                if y > bottom: bottom = y

    # Add a tiny padding or just use the box
    # Let's crop to the bounding box
    if left < right and top < bottom:
        box = (left, top, right, bottom)
        cropped_img = img.crop(box)
        cropped_img.save(output_path)
        print(f"Cropped successfully. New size: {cropped_img.size}")
    else:
        print("Could not find the black logo area.")

if __name__ == "__main__":
    crop_logo('logo.png', 'logo.png')
