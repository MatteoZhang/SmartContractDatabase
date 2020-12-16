





pragma solidity ^0.6.0;




library safemath {


function add(uint256 a, uint256 b) internal pure returns (uint256) {

uint256 c = a + b;

require(c >= a, "safemath: addition overflow");



return c;

}




function sub(uint256 a, uint256 b) internal pure returns (uint256) {

return sub(a, b, "safemath: subtraction overflow");

}




function sub(uint256 a, uint256 b, string memory errormessage) internal pure returns (uint256) {

require(b <= a, errormessage);

uint256 c = a - b;



return c;

}




function mul(uint256 a, uint256 b) internal pure returns (uint256) {




if (a == 0) {

return 0;

}



uint256 c = a * b;

require(c / a == b, "safemath: multiplication overflow");



return c;

}




function div(uint256 a, uint256 b) internal pure returns (uint256) {

return div(a, b, "safemath: division by zero");

}




function div(uint256 a, uint256 b, string memory errormessage) internal pure returns (uint256) {

require(b > 0, errormessage);

uint256 c = a / b;




return c;

}




function mod(uint256 a, uint256 b) internal pure returns (uint256) {

return mod(a, b, "safemath: modulo by zero");

}




function mod(uint256 a, uint256 b, string memory errormessage) internal pure returns (uint256) {

require(b != 0, errormessage);

return a % b;

}

}


















pragma solidity 0.6.12;








contract timelock {

using safemath for uint;



event newadmin(address indexed newadmin);

event newpendingadmin(address indexed newpendingadmin);

event newdelay(uint indexed newdelay);

event canceltransaction(bytes32 indexed txhash, address indexed target, uint value, string signature,  bytes data, uint eta);

event executetransaction(bytes32 indexed txhash, address indexed target, uint value, string signature,  bytes data, uint eta);

event queuetransaction(bytes32 indexed txhash, address indexed target, uint value, string signature, bytes data, uint eta);



uint public constant grace_period = 14 days;

uint public constant minimum_delay = 2 days;

uint public constant maximum_delay = 30 days;



address public admin;

address public pendingadmin;

uint public delay;

bool public admin_initialized;



mapping (bytes32 => bool) public queuedtransactions;





constructor(address admin_, uint delay_) public {

require(delay_ >= minimum_delay, "timelock::constructor: delay must exceed minimum delay.");

require(delay_ <= maximum_delay, "timelock::constructor: delay must not exceed maximum delay.");



admin = admin_;

delay = delay_;

admin_initialized = false;

}




receive() external payable { }



function setdelay(uint delay_) public {

require(msg.sender == address(this), "timelock::setdelay: call must come from timelock.");

require(delay_ >= minimum_delay, "timelock::setdelay: delay must exceed minimum delay.");

require(delay_ <= maximum_delay, "timelock::setdelay: delay must not exceed maximum delay.");

delay = delay_;



emit newdelay(delay);

}



function acceptadmin() public {

require(msg.sender == pendingadmin, "timelock::acceptadmin: call must come from pendingadmin.");

admin = msg.sender;

pendingadmin = address(0);



emit newadmin(admin);

}



function setpendingadmin(address pendingadmin_) public {


if (admin_initialized) {

require(msg.sender == address(this), "timelock::setpendingadmin: call must come from timelock.");

} else {

require(msg.sender == admin, "timelock::setpendingadmin: first call must come from admin.");

admin_initialized = true;

}

pendingadmin = pendingadmin_;



emit newpendingadmin(pendingadmin);

}



function queuetransaction(address target, uint value, string memory signature, bytes memory data, uint eta) public returns (bytes32) {

require(msg.sender == admin, "timelock::queuetransaction: call must come from admin.");

require(eta >= getblocktimestamp().add(delay), "timelock::queuetransaction: estimated execution block must satisfy delay.");



bytes32 txhash = keccak256(abi.encode(target, value, signature, data, eta));

queuedtransactions[txhash] = true;



emit queuetransaction(txhash, target, value, signature, data, eta);

return txhash;

}



function canceltransaction(address target, uint value, string memory signature, bytes memory data, uint eta) public {

require(msg.sender == admin, "timelock::canceltransaction: call must come from admin.");



bytes32 txhash = keccak256(abi.encode(target, value, signature, data, eta));

queuedtransactions[txhash] = false;



emit canceltransaction(txhash, target, value, signature, data, eta);

}



function executetransaction(address target, uint value, string memory signature, bytes memory data, uint eta) public payable returns (bytes memory) {

require(msg.sender == admin, "timelock::executetransaction: call must come from admin.");



bytes32 txhash = keccak256(abi.encode(target, value, signature, data, eta));

require(queuedtransactions[txhash], "timelock::executetransaction: transaction hasn't been queued.");

require(getblocktimestamp() >= eta, "timelock::executetransaction: transaction hasn't surpassed time lock.");

require(getblocktimestamp() <= eta.add(grace_period), "timelock::executetransaction: transaction is stale.");



queuedtransactions[txhash] = false;



bytes memory calldata;



if (bytes(signature).length == 0) {

calldata = data;

} else {

calldata = abi.encodepacked(bytes4(keccak256(bytes(signature))), data);

}




(bool success, bytes memory returndata) = target.call.value(value)(calldata);

require(success, "timelock::executetransaction: transaction execution reverted.");



emit executetransaction(txhash, target, value, signature, data, eta);



return returndata;

}



function getblocktimestamp() internal view returns (uint) {


return block.timestamp;

}

}
