from brownie import FundMe
from scripts.useful import get_account


def interact_fund():
    fund_me = FundMe[-1]
    min_fund = fund_me.getMinFundWei()
    transaction = fund_me.fund({"from": get_account(), "value": min_fund + 1})
    transaction.wait(1)
    return


def interact_withdraw():
    fund_me = FundMe[-1]
    transaction = fund_me.withdraw({"from": get_account()})
    transaction.wait(1)
    print(f"Contract balance withdraw done")
    return


def funding_activity():
    from brownie import accounts

    fund_me = FundMe[-1]
    min_fund = 99000000000000000000
    accounts_all = [accounts[1], accounts[2], accounts[3], accounts[4], accounts[5]]
    for acc in accounts_all:
        transaction = fund_me.fund({"from": acc, "value": min_fund + 1})
    return


def main():
    interact_fund()
    # funding_activity()
    interact_withdraw()
    return
