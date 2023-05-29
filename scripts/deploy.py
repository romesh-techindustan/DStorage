from brownie import accounts, config, DStorage


def deploy_storage():
    account= accounts.add(config["wallets"]["from_key"])
    # print(account)
    simple_storage=DStorage.deploy({"from":account})
    # print(simple_storage)
    store_value = simple_storage.retrieve()
    print(store_value)
    file_hash = input("File hash: ")
    file_size = input("File size: ")
    file_type = input("File type: ")
    file_name = input("File name: ")
    file_desc = input("File description: ")
    # transaction = simple_storage.uploadFile("_fileHash", 12, " memory _fileType",  "fileName", "fileDescription",{"from":account})
    transaction = simple_storage.uploadFile(file_hash, file_size, file_type,  file_name, file_desc,{"from":account})
    transaction.wait(1)
    uploaded_value = simple_storage.retrieve()
    print(uploaded_value)

def main():
    deploy_storage()