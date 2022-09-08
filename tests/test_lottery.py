from brownie import Lottery, accounts, config, network
from web3 import Web3
from scripts.deploy_lottery import deploy_lottery
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
import pytest


def test_get_entrance_fee():
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    lottery = deploy_lottery()
    # Act
    # 1560 eth / usd
    # usdEntryFee is 50
    # 1560/1 == 50/x == 0.32
    # expected_entrance_fee = Web3.toWei(0.32, "ether")
    entrance_fee = lottery.getEntranceFee()
    # Assert
    assert entrance_fee > Web3.toWei(0.030, "ether")
    assert entrance_fee < Web3.toWei(0.034, "ether")
