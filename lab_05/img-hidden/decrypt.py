import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3):  
                binary_message += format(pixel[color_channel], '08b')[-1]

    # Tìm vị trí của dấu hiệu kết thúc '1111111111111110'
    end_marker = '1111111111111110'
    end_index = binary_message.find(end_marker)
    if end_index != -1:
        binary_message = binary_message[:end_index]  # Cắt bỏ phần đánh dấu kết thúc

    # Chuyển chuỗi nhị phân thành văn bản
    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        message += char

    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decode.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()
