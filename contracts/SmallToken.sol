pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract SmallToken is ERC20 {
    constructor() public ERC20("SmallToken", "SMT") {
        _mint(msg.sender, 2888);
    }
}