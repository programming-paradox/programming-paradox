// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;

contract Lottery {
    address public manager;
    address[] public players;

    //Assigning the manager of the contract
    constructor() public {
        manager = msg.sender;
    }

    //Entering the players into the lottery
    function enter() public payable {
        require(msg.value <= 1 ether);
        players.push(msg.sender);
    }


    //Generating a random number that is not totally random bug of program
    function random() public view returns(uint) {
        return uint(sha256(abi.encodePacked(block.difficulty, block.timestamp, players)));
    }

    //Now we are going to pick the winner of the game
    function pickWinner() public restricted {
        uint index = random() % players.length;
        payable(players[index]).transfer(address(this).balance);
        players = new address[] (0);
    }

    modifier restricted() {
        require(msg.sender == manager);
        _;
    }

    function getPlayers() public view returns(address[] memory) {
        return players;
    }

}