from . import smart_contract


class NFTProcess(smart_contract.SmartContract):

    def __init__(self):
        pass

    def mintCertification(self, _user: str, tokenURI: str):
        nonce = self.web3.eth.get_transaction_count(self.ACCOUNT)
        requiredGas = self.contract.functions.mintCertification(
            _user, tokenURI).estimate_gas({'from': self.ACCOUNT})
        gasPrice = self.web3.eth.gas_price
        print(requiredGas)
        transaction_data = self.contract.functions.mintCertification(_user, tokenURI).build_transaction(
            {'from': self.ACCOUNT, 'nonce': nonce, "gas": self.web3.to_hex(requiredGas*5),
             "gasPrice": self.web3.to_hex(gasPrice), })
        signed_txn = self.web3.eth.account.sign_transaction(
            transaction_data, self.PRIVATE_KEY)
        transaction_hash = self.web3.eth.send_raw_transaction(
            signed_txn.rawTransaction)
        result = self.web3.eth.wait_for_transaction_receipt(
            transaction_hash)
        if (result["status"] == False):

            raise Exception("Transaction Failed")
        return result["status"]
