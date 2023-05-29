from brownie import DStorage, accounts

def test_deploy():
    # arrange
    account = accounts[0]

    #acting
    simple_storage = DStorage.deploy({'from': account})
    starting_value = simple_storage.retrieve()
    expected = 0 

    # Assert
    assert starting_value==expected

def test_uploadingFile():
    #arrange
    account = accounts[0]
    simple_storage = DStorage.deploy({'from': account})
    #acting
    expected = 1
    simple_storage.store(expected,{'from': account})
    # Assert
    assert expected == simple_storage.retrieve()