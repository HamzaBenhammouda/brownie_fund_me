from brownie import FundMe, network, config, MockV3Aggregator
from scripts.useful import get_account, deployMock, LOCAL_BLOCKCHAINS


def deployFundMe():
    my_account = get_account()

    # Get priceFeed
    if network.show_active() not in LOCAL_BLOCKCHAINS:
        priceFeed = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deployMock()
        priceFeed = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        priceFeed,
        {"from": my_account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    return fund_me


def main():
    deployFundMe()
    return
