pragma solidity ^0.5.0;
contract erc20interface {
function totalsupply() public view returns (uint);
function balanceof(address tokenowner) public view returns (uint balance);
function allowance(address tokenowner, address spender) public view returns (uint remaining);
function transfer(address to, uint tokens) public returns (bool success);
function approve(address spender, uint tokens) public returns (bool success);
function transferfrom(address from, address to, uint tokens) public returns (bool success);
event transfer(address indexed from, address indexed to, uint tokens);
event approval(address indexed tokenowner, address indexed spender, uint tokens);
}
contract safemath {
function safeadd(uint a, uint b) public pure returns (uint c) {
c = a + b;
require(c >= a);
}
function safesub(uint a, uint b) public pure returns (uint c) {
require(b <= a); c = a - b; } function safemul(uint a, uint b) public pure returns (uint c) { c = a * b; require(a == 0 || c / a == b); } function safediv(uint a, uint b) public pure returns (uint c) { require(b > 0);
c = a / b;
}
}
contract aliennetworktoken is erc20interface, safemath {
string public name;
string public symbol;
uint8 public decimals; uint8 public decimals; // 18 decimals is the strongly suggested default, avoid changing it
uint256 public _totalsupply;
mapping(address => uint) balances;
mapping(address => mapping(address => uint)) allowed;
constructor() public {
name = "aliennetwork";
symbol = "aln";
decimals = 18;
_totalsupply =50000000000000000000000;
balances[msg.sender] = _totalsupply;
emit transfer(address(0), msg.sender, _totalsupply);
}
function totalsupply() public view returns (uint) {
return _totalsupply  - balances[address(0)];
}
function balanceof(address tokenowner) public view returns (uint balance) {
return balances[tokenowner];
}
function allowance(address tokenowner, address spender) public view returns (uint remaining) {
return allowed[tokenowner][spender];
}
function approve(address spender, uint tokens) public returns (bool success) {
allowed[msg.sender][spender] = tokens;
emit approval(msg.sender, spender, tokens);
return true;
}
function transfer(address to, uint tokens) public returns (bool success) {
balances[msg.sender] = safesub(balances[msg.sender], tokens);
balances[to] = safeadd(balances[to], tokens);
emit transfer(msg.sender, to, tokens);
return true;
}
function transferfrom(address from, address to, uint tokens) public returns (bool success) {
balances[from] = safesub(balances[from], tokens);
allowed[from][msg.sender] = safesub(allowed[from][msg.sender], tokens);
balances[to] = safeadd(balances[to], tokens);
emit transfer(from, to, tokens);
return true;
}
}
