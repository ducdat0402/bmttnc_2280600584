from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading

# Khởi tạo socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Tạo cặp khóa RSA
client_key = RSA.generate(2048)

# Nhận khóa công khai của server
server_public_key = RSA.import_key(client_socket.recv(2048))

# Gửi khóa công khai của client cho server
client_socket.send(client_key.publickey().export_key(format='PEM'))

# Nhận khóa AES đã mã hóa từ server
encrypted_aes_key = client_socket.recv(2048)

# Giải mã khóa AES bằng khóa private của client
cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)

# Hàm mã hóa tin nhắn
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

# Hàm giải mã tin nhắn
def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

# Hàm nhận tin nhắn từ server
def receive_messages():
    while True:
        try:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message:
                break

            decrypted_message = decrypt_message(aes_key, encrypted_message)
            print("Received:", decrypted_message)

        except Exception as e:
            print(f"Error receiving message: {e}")
            break

# Bắt đầu luồng nhận tin nhắn
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Gửi tin nhắn từ client
while True:
    message = input("Enter message ('exit' to quit): ")
    encrypted_message = encrypt_message(aes_key, message)
    client_socket.send(encrypted_message)

    if message.lower() == "exit":
        break

# Đóng kết nối
client_socket.close()
