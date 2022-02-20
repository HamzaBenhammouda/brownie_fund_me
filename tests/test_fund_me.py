from scripts.useful import get_account, LOCAL_BLOCKCHAINS
from scripts.deploy import deployFundMe
from brownie import network, accounts, exceptions
import pytest


def test_fund():
    # Rearrange
    account = get_account()
    # Act
    fund_me = deployFundMe()
    min_fund = fund_me.getMinFundWei()
    transaction = fund_me.fund({"from": account, "value": min_fund + 1})
    transaction.wait(1)
    # Assert
    assert fund_me.addressToamount(account.address) == min_fund + 1
    return


def test_withdraw():
    # Rearrange
    account = get_account()
    # Act
    fund_me = deployFundMe()
    transaction = fund_me.withdraw({"from": account})
    transaction.wait(1)
    # Assert
    assert fund_me.addressToamount(account.address) == 0
    return


def test_onlyOwner():
    if network.show_active() not in LOCAL_BLOCKCHAINS:
        pytest.skip("Only valid for local blockchains")
    # Rearrange
    fund_me = deployFundMe()
    account = get_account()
    bad_account = accounts.add()
    # Act
    transaction = fund_me.withdraw({"from": account})
    transaction.wait(1)
    # Assert
    with pytest.raises(exceptions.VirtualMachineError):
        transaction = fund_me.withdraw({"from": bad_account})
        transaction.wait(1)
    return
