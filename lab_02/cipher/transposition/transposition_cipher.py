class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        """Mã hóa văn bản bằng Transposition Cipher."""
        encrypted_text = ""  # Sửa lỗi khởi tạo biến
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        """Giải mã văn bản bằng Transposition Cipher."""
        num_cols = (len(text) + key - 1) // key  # Tính số cột (chính xác hơn)
        num_rows = key  # Số hàng chính là key
        num_shaded_boxes = (num_cols * num_rows) - len(text)  # Ô trống

        decrypted_text = [''] * num_cols
        col, row = 0, 0

        for symbol in text:
            decrypted_text[col] += symbol
            col += 1

            if col == num_cols or (col == num_cols - 1 and row >= num_rows - num_shaded_boxes):
                col = 0
                row += 1

        return ''.join(decrypted_text)