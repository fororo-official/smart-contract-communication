from web3 import Web3
from web3.middleware import geth_poa_middleware


class SmartContract:
    # 스마트컨트랙 변수
    INFURA_URL = "https://polygon-mainnet.infura.io/v3/5165b64a09a54f10b88e0fb46a7e8aee"
    ABI = [
        {"inputs": [], "stateMutability": 'nonpayable', "type": 'constructor'},
        {
            "inputs": [
                {"internalType": 'address', "name": 'sender', "type": 'address'},
                {"internalType": 'uint256', "name": 'tokenId', "type": 'uint256'},
                {"internalType": 'address', "name": 'owner', "type": 'address'},
            ],
            "name": 'ERC721IncorrectOwner',
            "type": 'error',
        },
        {
            "inputs": [
                {"internalType": 'address', "name": 'operator', "type": 'address'},
                {"internalType": 'uint256', "name": 'tokenId', "type": 'uint256'},
            ],
            "name": 'ERC721InsufficientApproval',
            "type": 'error',
        },
        {
            "inputs": [{"internalType": 'address', "name": 'approver', "type": 'address'}],
            "name": 'ERC721InvalidApprover',
            "type": 'error',
        },
        {
            "inputs": [{"internalType": 'address', "name": 'operator', "type": 'address'}],
            "name": 'ERC721InvalidOperator',
            "type": 'error',
        },
        {
            "inputs": [{"internalType": 'address', "name": 'owner', "type": 'address'}],
            "name": 'ERC721InvalidOwner',
            "type": 'error',
        },
        {
            "inputs": [{"internalType": 'address', "name": 'receiver', "type": 'address'}],
            "name": 'ERC721InvalidReceiver',
            "type": 'error',
        },
        {
            "inputs": [{"internalType": 'address', "name": 'sender', "type": 'address'}],
            "name": 'ERC721InvalidSender',
            "type": 'error',
        },
        {
            "inputs": [{"internalType": 'uint256', "name": 'tokenId', "type": 'uint256'}],
            "name": 'ERC721NonexistentToken',
            "type": 'error',
        },
        {
            "anonymous": False,
            "inputs": [
                {"indexed": True, "internalType": 'address',
                 "name": 'owner', "type": 'address'},
                {"indexed": True, "internalType": 'address',
                 "name": 'approved', "type": 'address'},
                {"indexed": True, "internalType": 'uint256',
                 "name": 'tokenId', "type": 'uint256'},
            ],
            "name": 'Approval',
            "type": 'event',
        },
        {
            "anonymous": False,
            "inputs": [
                {"indexed": True, "internalType": 'address',
                 "name": 'owner', "type": 'address'},
                {"indexed": True, "internalType": 'address',
                 "name": 'operator', "type": 'address'},
                {"indexed": False, "internalType": 'bool',
                    "name": 'approved', "type": 'bool'},
            ],
            "name": 'ApprovalForAll',
            "type": 'event',
        },
        {
            "anonymous": False,
            "inputs": [
                {"indexed": False, "internalType": 'uint256',
                 "name": '_fromTokenId', "type": 'uint256'},
                {"indexed": False, "internalType": 'uint256',
                 "name": '_toTokenId', "type": 'uint256'},
            ],
            "name": 'BatchMetadataUpdate',
            "type": 'event',
        },
        {
            "anonymous": False,
            "inputs": [{"indexed": False, "internalType": 'uint256', "name": '_tokenId', "type": 'uint256'}],
            "name": 'MetadataUpdate',
            "type": 'event',
        },
        {
            "anonymous": False,
            "inputs": [
                {"indexed": True, "internalType": 'address',
                    "name": 'from', "type": 'address'},
                {"indexed": True, "internalType": 'address',
                    "name": 'to', "type": 'address'},
                {"indexed": True, "internalType": 'uint256',
                 "name": 'tokenId', "type": 'uint256'},
            ],
            "name": 'Transfer',
            "type": 'event',
        },
        {
            "inputs": [
                {"internalType": 'address', "name": 'to', "type": 'address'},
                {"internalType": 'uint256', "name": 'tokenId', "type": 'uint256'},
            ],
            "name": 'approve',
            "outputs": [],
            "stateMutability": 'nonpayable',
            "type": 'function',
        },
        {
            "inputs": [{"internalType": 'address', "name": 'owner', "type": 'address'}],
            "name": 'balanceOf',
            "outputs": [{"internalType": 'uint256', "name": '', "type": 'uint256'}],
            "stateMutability": 'view',
            "type": 'function',
        },
        {
            "inputs": [{"internalType": 'uint256', "name": 'tokenId', "type": 'uint256'}],
            "name": 'getApproved',
            "outputs": [{"internalType": 'address', "name": '', "type": 'address'}],
            "stateMutability": 'view',
            "type": 'function',
        },
        {
            "inputs": [{"internalType": 'address', "name": 'NFTowner', "type": 'address'}],
            "name": 'getTokenURIOf',
            "outputs": [{"internalType": 'string[]', "name": '', "type": 'string[]'}],
            "stateMutability": 'view',
            "type": 'function',
        },
        {
            "inputs": [
                {"internalType": 'address', "name": 'owner', "type": 'address'},
                {"internalType": 'address', "name": 'operator', "type": 'address'},
            ],
            "name": 'isApprovedForAll',
            "outputs": [{"internalType": 'bool', "name": '', "type": 'bool'}],
            "stateMutability": 'view',
            "type": 'function',
        },
        {
            "inputs": [
                {"internalType": 'address', "name": '_user', "type": 'address'},
                {"internalType": 'string', "name": 'tokenURI', "type": 'string'},
            ],
            "name": 'mintCertification',
            "outputs": [{"internalType": 'uint256', "name": '', "type": 'uint256'}],
            "stateMutability": 'nonpayable',
            "type": 'function',
        },
        {
            "inputs": [],
            "name": '"name"',
            "outputs": [{"internalType": 'string', "name": '', "type": 'string'}],
            "stateMutability": 'view',
            "type": 'function',
        },
        {
            "inputs": [{"internalType": 'uint256', "name": 'tokenId', "type": 'uint256'}],
            "name": 'ownerOf',
            "outputs": [{"internalType": 'address', "name": '', "type": 'address'}],
            "stateMutability": 'view',
            "type": 'function',
        },
        {
            "inputs": [
                {"internalType": 'address', "name": 'from', "type": 'address'},
                {"internalType": 'address', "name": 'to', "type": 'address'},
                {"internalType": 'uint256', "name": 'tokenId', "type": 'uint256'},
            ],
            "name": 'safeTransferFrom',
            "outputs": [],
            "stateMutability": 'nonpayable',
            "type": 'function',
        },
        {
            "inputs": [
                {"internalType": 'address', "name": 'from', "type": 'address'},
                {"internalType": 'address', "name": 'to', "type": 'address'},
                {"internalType": 'uint256', "name": 'tokenId', "type": 'uint256'},
                {"internalType": 'bytes', "name": 'data', "type": 'bytes'},
            ],
            "name": 'safeTransferFrom',
            "outputs": [],
            "stateMutability": 'nonpayable',
            "type": 'function',
        },
        {
            "inputs": [
                {"internalType": 'address', "name": 'operator', "type": 'address'},
                {"internalType": 'bool', "name": 'approved', "type": 'bool'},
            ],
            "name": 'setApprovalForAll',
            "outputs": [],
            "stateMutability": 'nonpayable',
            "type": 'function',
        },
        {
            "inputs": [{"internalType": 'bytes4', "name": 'interfaceId', "type": 'bytes4'}],
            "name": 'supportsInterface',
            "outputs": [{"internalType": 'bool', "name": '', "type": 'bool'}],
            "stateMutability": 'view',
            "type": 'function',
        },
        {
            "inputs": [],
            "name": 'symbol',
            "outputs": [{"internalType": 'string', "name": '', "type": 'string'}],
            "stateMutability": 'view',
            "type": 'function',
        },
        {
            "inputs": [{"internalType": 'uint256', "name": 'tokenId', "type": 'uint256'}],
            "name": 'tokenURI',
            "outputs": [{"internalType": 'string', "name": '', "type": 'string'}],
            "stateMutability": 'view',
            "type": 'function',
        },
        {
            "inputs": [
                {"internalType": 'address', "name": 'from', "type": 'address'},
                {"internalType": 'address', "name": 'to', "type": 'address'},
                {"internalType": 'uint256', "name": 'tokenId', "type": 'uint256'},
            ],
            "name": 'transferFrom',
            "outputs": [],
            "stateMutability": 'nonpayable',
            "type": 'function',
        },
    ]
    CONTRACT_ADDRESS = '0xe52a59E10EE83f281c73Fe2f2eA5EAFE5cc084Af'
    # 돈 빠져나갈 곳
    ACCOUNT = "0x83F917D36Ba35F2A61B069cdBccdC12F96705fc6"
    PRIVATE_KEY = "32cee991215ccbefa0186c43d56db5e10290edaefd61704bea0a760195b848eb"

    web3: Web3 = Web3(Web3.HTTPProvider(INFURA_URL))
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    contract = web3.eth.contract(CONTRACT_ADDRESS, abi=ABI)
