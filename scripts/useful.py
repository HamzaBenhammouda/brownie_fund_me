from brownie import accounts, network, MockV3Aggregator

MAIN_NET_FORK = ["mainnet-fork-dev"]
LOCAL_BLOCKCHAINS = ["development", "ganache-local"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAINS
        or network.show_active() in MAIN_NET_FORK
    ):
        return accounts[0]
    else:
        return accounts.load("testAccount")


def deployMock():
    _decimals = 8
    _initialAnswer = 200000000000
    if len(MockV3Aggregator) <= 0:
        mock = MockV3Aggregator.deploy(
            _decimals, _initialAnswer, {"from": get_account()}
        )
    return
