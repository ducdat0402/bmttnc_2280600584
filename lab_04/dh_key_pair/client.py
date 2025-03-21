from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def generate_client_key_pair(parameters):
    """Tạo cặp khóa client dựa trên thông số DH của server"""
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_secret(private_key, server_public_key):
    """Tạo khóa chung bằng cách trao đổi khóa DH"""
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():
    # Tải khóa công khai của server
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())

    # Lấy thông số DH từ khóa server
    parameters = server_public_key.parameters()
    
    # Tạo khóa riêng tư và khóa công khai của client
    private_key, public_key = generate_client_key_pair(parameters)

    # Trao đổi khóa để tạo khóa chung
    shared_secret = derive_shared_secret(private_key, server_public_key)

    print("Shared Secret:", shared_secret.hex())

if __name__ == "__main__":
    main()
