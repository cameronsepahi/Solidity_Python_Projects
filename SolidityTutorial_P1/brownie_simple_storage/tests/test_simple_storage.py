from brownie import SimpleStorage, accounts


def test_deploy():
    # Testing smart contracts can be seperated into 3 categories: (1) Arrange, (2) Act, and (3) Asserting
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 15
    simple_storage.store(expected, {"from": account})  # where we store to 15
    # Assert
    assert expected == simple_storage.retrieve()
