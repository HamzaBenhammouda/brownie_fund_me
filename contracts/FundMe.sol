// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

contract FundMe {
    using SafeMathChainlink for uint256;

    //variables
    address owner;
    AggregatorV3Interface public priceFeed;
    address[] public funders;
    mapping(address => uint256) public addressToamount;
    uint256 min_fund_usd = 50;

    //constructor
    constructor(address _priceFeed_address) public {
        owner = msg.sender;
        priceFeed = AggregatorV3Interface(_priceFeed_address);
    }

    //modifier
    modifier onlyOwner() {
        assert(owner == msg.sender);
        _;
    }

    //functions
    function convertUSDtoWei(uint256 _usd_amount)
        public
        view
        returns (uint256)
    {
        (, int256 price, , , ) = priceFeed.latestRoundData();
        return
            (_usd_amount * (1 * 10**8) * 1000000000000000000) / uint256(price);
    }

    function getMinFundWei() public view returns (uint256) {
        return convertUSDtoWei(min_fund_usd);
    }

    function fund() public payable {
        require(msg.value >= getMinFundWei(), "Minimun fund is not satisfied!");
        funders.push(msg.sender);
        addressToamount[msg.sender] += msg.value;
    }

    function withdraw() public payable onlyOwner {
        //withdraw all contract balance to owner
        msg.sender.transfer(address(this).balance);

        for (uint256 i = 0; i < funders.length; i++) {
            addressToamount[funders[i]] = 0;
        }
        funders = new address[](0);
    }
}
