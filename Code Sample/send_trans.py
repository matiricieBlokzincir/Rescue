from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/59ed87f9fdb0404ab3163bc51c300ff6'))


# Gönderen hesap özel anahtarı
private_key = "dbfebe60567dfaf171e35b2e828d24d4832bd871abb492b24d4d63b88025f69d"

# Gönderen hesap
sender_address = "0xfE971eE29ACAe70C8D68DDbC6719f9B50F5926E9"

# Alıcı hesap
recipient_address = "0xb2e902a097e5b9adDBF3A6A7364c73780ba95e40"

# Gönderilecek ETH miktarı (wei cinsinden)
amount_in_wei = w3.to_wei(0.01, 'ether')

# Nonce hesaplamak için gönderen hesap bakiyesini kontrol edin
balance = w3.eth.get_balance(sender_address)
nonce = w3.eth.get_transaction_count(sender_address)

# İşlem verilerini oluşturun
transaction = {
    'to': recipient_address,
    'value': amount_in_wei,
    'gas': 2000000,  # Gas sınırını uygun bir şekilde ayarlayın
    'gasPrice': w3.to_wei('50', 'gwei'),  # Gas fiyatını uygun bir şekilde ayarlayın
    'nonce': nonce,
}

# İşlemi imzalayın
signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)

# İşlemi Ethereum ağına gönderin
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

print(f"Transaction hash: {transaction_hash.hex()}")
