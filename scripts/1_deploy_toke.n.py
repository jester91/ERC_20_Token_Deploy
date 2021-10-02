from brownie import accounts, config, TokenERC20

initial_supply = 1337
token_name = "Jester"
token_symbol = "JSTR"


def main():
    account = account.add(config["wallets"]["from_key"])
    erc20 = TokenERC20.deploy(
        initial_supply, token_name, token_symbol, {"from": account},publish_source=True
    )
