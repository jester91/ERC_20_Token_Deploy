from brownie import accounts, config, SmallToken

initial_supply = 1337
token_name = "SmallToken"
token_symbol = "SMT"


def main():
    account = accounts[0]
    erc20 = SmallToken.deploy(
        initial_supply, {"from": account}
    )
