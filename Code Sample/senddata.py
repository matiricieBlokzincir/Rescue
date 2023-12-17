from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/59ed87f9fdb0404ab3163bc51c300ff6'))

assert w3.is_connected()

contract_address = w3.to_checksum_address('0xe83bA4A1De59A084e6879De11c10092973E0Df2D')
contract_abi = [
	{
		"inputs": [],
		"name": "EmployeeDetails",
		"outputs": [
			{
				"internalType": "string",
				"name": "Name",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "EmpId",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "Age",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "addrs",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "addEmployeeDetails",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]


contract = w3.eth.contract(address=contract_address, abi=contract_abi)

private_key = 'dbfebe60567dfaf171e35b2e828d24d4832bd871abb492b24d4d63b88025f69d'
account_address = '0xfE971eE29ACAe70C8D68DDbC6719f9B50F5926E9'


