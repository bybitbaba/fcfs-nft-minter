// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TestNFT {
    bool public mintActive = false;
    uint256 public totalMinted = 0;

    function flipMint() public {
        mintActive = !mintActive;
    }

    function mint(uint256 amount) public payable {
        require(mintActive, "Mint not live");
        require(msg.value >= 0.01 ether * amount, "Pay up");
        totalMinted += amount;
    }
}