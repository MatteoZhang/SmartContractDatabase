// file: @openzeppelin/contracts/math/safemath.sol
// spdx-license-identifier: mit
/**

* @dev wrappers over solidity's arithmetic operations with added overflow

* checks.

*

* arithmetic operations in solidity wrap on overflow. this can easily result

* in bugs, because programmers usually assume that an overflow raises an

* error, which is the standard behavior in high level programming languages.

* `safemath` restores this intuition by reverting the transaction when an

* operation overflows.

*

* using this library instead of the unchecked operations eliminates an entire

* class of bugs, so it's recommended to use it always.

*/
/**

* @dev returns the addition of two unsigned integers, reverting on

* overflow.

*

* counterpart to solidity's `+` operator.

*

* requirements:

*

* - addition cannot overflow.

*/
/**

* @dev returns the subtraction of two unsigned integers, reverting on

* overflow (when the result is negative).

*

* counterpart to solidity's `-` operator.

*

* requirements:

*

* - subtraction cannot overflow.

*/
/**

* @dev returns the subtraction of two unsigned integers, reverting with custom message on

* overflow (when the result is negative).

*

* counterpart to solidity's `-` operator.

*

* requirements:

*

* - subtraction cannot overflow.

*/
/**

* @dev returns the multiplication of two unsigned integers, reverting on

* overflow.

*

* counterpart to solidity's `*` operator.

*

* requirements:

*

* - multiplication cannot overflow.

*/
// gas optimization: this is cheaper than requiring 'a' not being zero, but the
// benefit is lost if 'b' is also tested.
// see: https://github.com/openzeppelin/openzeppelin-contracts/pull/522
/**

* @dev returns the integer division of two unsigned integers. reverts on

* division by zero. the result is rounded towards zero.

*

* counterpart to solidity's `/` operator. note: this function uses a

* `revert` opcode (which leaves remaining gas untouched) while solidity

* uses an invalid opcode to revert (consuming all remaining gas).

*

* requirements:

*

* - the divisor cannot be zero.

*/
/**

* @dev returns the integer division of two unsigned integers. reverts with custom message on

* division by zero. the result is rounded towards zero.

*

* counterpart to solidity's `/` operator. note: this function uses a

* `revert` opcode (which leaves remaining gas untouched) while solidity

* uses an invalid opcode to revert (consuming all remaining gas).

*

* requirements:

*

* - the divisor cannot be zero.

*/
// assert(a == b * c + a % b); // there is no case in which this doesn't hold
/**

* @dev returns the remainder of dividing two unsigned integers. (unsigned integer modulo),

* reverts when dividing by zero.

*

* counterpart to solidity's `%` operator. this function uses a `revert`

* opcode (which leaves remaining gas untouched) while solidity uses an

* invalid opcode to revert (consuming all remaining gas).

*

* requirements:

*

* - the divisor cannot be zero.

*/
/**

* @dev returns the remainder of dividing two unsigned integers. (unsigned integer modulo),

* reverts with custom message when dividing by zero.

*

* counterpart to solidity's `%` operator. this function uses a `revert`

* opcode (which leaves remaining gas untouched) while solidity uses an

* invalid opcode to revert (consuming all remaining gas).

*

* requirements:

*

* - the divisor cannot be zero.

*/
// file: contracts/timelock.sol
// copied from https://github.com/compound-finance/compound-protocol/blob/master/contracts/governance/governoralpha.sol
// copyright 2020 compound labs, inc.
// redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
// 1. redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
// 2. redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
// 3. neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
// this software is provided by the copyright holders and contributors "as is" and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. in no event shall the copyright holder or contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.
//
// ctrl+f for xxx to see all the modifications.
// xxx: pragma solidity ^0.5.16;
// xxx: import "./safemath.sol";
// xxx: function() external payable { }
// allows one time setting of admin for deployment purposes
// solium-disable-next-line security/no-call-value
// solium-disable-next-line security/no-block-members
