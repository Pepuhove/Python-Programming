from rembg import remove
from PIL import Image

def remove_background(input_path, output_path):
    inp = Image.open(input_path)
    output = remove(inp)
    output.save(output_path)
    return output

# Example usage:
remove_background("pepukai.jpg", "pepukai.png")