from PIL import Image

def image_to_ascii(image_path, output_width=100, output_height=None):
    try:
        # Open the image file
        img = Image.open(image_path)

        # Resize the image to the desired output dimensions
        if output_height is None:
            aspect_ratio = img.height / img.width
            output_height = int(output_width * aspect_ratio)
        img = img.resize((output_width, output_height))

        # Convert the image to grayscale
        img = img.convert("L")

        # Define a list of ASCII characters to represent pixel intensity
        ascii_chars = "@%#*+=-:. "

        # Convert each pixel to ASCII character
        ascii_art = ""
        for y in range(img.height):
            for x in range(img.width):
                pixel_value = img.getpixel((x, y))
                # Ensure the pixel value is within the valid range
                pixel_index = min(pixel_value // (256 // len(ascii_chars)), len(ascii_chars) - 1)
                ascii_art += ascii_chars[pixel_index]
            ascii_art += "\n"

        print(ascii_art)
    except Exception as e:
        print(f"Error: {e}")

# Example usage
image_path = r"D:\BOBBY\project\class\sir.png"  # Use raw string or double backslashes
image_to_ascii(image_path)
