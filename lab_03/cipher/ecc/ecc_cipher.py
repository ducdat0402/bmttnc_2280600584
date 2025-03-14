import ecdsa
import os

# Tạo thư mục lưu trữ nếu chưa tồn tại
os.makedirs('cipher/ecc/keys', exist_ok=True)

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        # Tạo khóa riêng tư
        sk = ecdsa.SigningKey.generate()
        # Lấy khóa công khai từ khóa riêng tư
        vk = sk.get_verifying_key()

        # Lưu khóa vào file
        with open('cipher/ecc/keys/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())

        with open('cipher/ecc/keys/publicKey.pem', 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        with open('cipher/ecc/keys/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())

        with open('cipher/ecc/keys/publicKey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())

        return sk, vk

    def sign(self, message, key):
        # Ký dữ liệu bằng khóa riêng tư
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature):
        _, vk = self.load_keys()  # Chỉ lấy khóa công khai
        try:
            return vk.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False

# Test chương trình
if __name__ == "__main__":
    ecc = ECCCipher()
    
    # Tạo khóa nếu chưa có
    if not os.path.exists('cipher/ecc/keys/privateKey.pem'):
        print("Generating new ECC keys...")
        ecc.generate_keys()
    
    sk, vk = ecc.load_keys()

    # Ký một thông điệp
    message = "Hello, ECC!"
    signature = ecc.sign(message, sk)
    print(f"Message: {message}")
    print(f"Signature: {signature.hex()}")

    # Kiểm tra xác minh chữ ký
    is_valid = ecc.verify(message, signature)
    print(f"Signature valid: {is_valid}")
