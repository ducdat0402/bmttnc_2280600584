from blockchain import Blockchain

# Khởi tạo Blockchain
my_blockchain = Blockchain()

# Thêm giao dịch
my_blockchain.add_transaction('Alice', 'Bob', 10)
my_blockchain.add_transaction('Bob', 'Charlie', 5)
my_blockchain.add_transaction('Charlie', 'Alice', 3)

# Đào một block mới
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash

# Thêm giao dịch thưởng cho miner
my_blockchain.add_transaction('Genesis', 'Miner', 1)

# Tạo block mới
new_block = my_blockchain.create_block(new_proof, previous_hash)

# Hiển thị Blockchain
for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print("Timestamp:", block.timestamp)
    print("Transactions:", block.transactions)
    print("Proof:", block.proof)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("------")

# Kiểm tra blockchain hợp lệ
print("Is Blockchain Valid:", my_blockchain.is_chain_valid(my_blockchain.chain))
