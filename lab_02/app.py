from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# Router cho trang chủ
@app.route("/")
def home():
    return render_template('index.html')

# Router cho trang Caesar Cipher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

# Route xử lý mã hóa Caesar Cipher
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    
    # Khởi tạo đối tượng CaesarCipher
    Caesar = CaesarCipher()
    
    # Gọi hàm mã hóa
    encrypted_text = Caesar.encrypt_text(text, key)
    
    # Trả về kết quả
    return f"""
        <h3>Kết quả mã hóa</h3>
        <p><b>Văn bản gốc:</b> {text}</p>
        <p><b>Khóa:</b> {key}</p>
        <p><b>Văn bản đã mã hóa:</b> {encrypted_text}</p>
    """

# Route xử lý giải mã Caesar Cipher
@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    
    # Khởi tạo đối tượng CaesarCipher
    Caesar = CaesarCipher()
    
    # Gọi hàm giải mã
    decrypted_text = Caesar.decrypt_text(text, key)
    
    # Trả về kết quả
    return f"""
        <h3>Kết quả giải mã</h3>
        <p><b>Văn bản đã mã hóa:</b> {text}</p>
        <p><b>Khóa:</b> {key}</p>
        <p><b>Văn bản gốc:</b> {decrypted_text}</p>
    """

# Chạy ứng dụng Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
