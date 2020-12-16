/**

*submitted for verification at etherscan.io on 2020-08-30

*/
// original file came from compound: https://github.com/compound-finance/compound-protocol/blob/master/contracts/timelock.sol
// original audit: https://blog.openzeppelin.com/compound-finance-patch-audit/
// overview:
//    no critical
//    no high
//
// changes made by pylon after audit:
//    formatting, naming, & uint256 instead of uint
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
/// @notice an event emitted when the timelock admin changes
/// @notice an event emitted when a new admin is staged in the timelock
/// @notice an event emitted when a queued transaction is cancelled
/// @notice an event emitted when a queued transaction is executed
/// @notice an event emitted when a new transaction is queued
/// @notice the length of time after the delay has passed that a transaction can be executed
/// @notice the minimum length of the timelock delay
 have to be present for 2 rebases/// @notice the maximum length of the timelock delay
/* require(delay_ >= minimum_delay, "timelock::constructor: delay must exceed minimum delay.");

require(delay_ <= maximum_delay, "timelock::setdelay: delay must not exceed maximum delay."); */
/**

@notice sets the delay

@param delay_ the new delay

*/
/// @notice sets the new admin address
/**

@notice queues a new pendingadmin

@param pendingadmin_ the new pendingadmin address

*/
// allows one time setting of admin for deployment purposes
// timelock not enforced prior to updating the admin. this should occur on
// deployment.
// solium-disable-next-line security/no-call-value
// solium-disable-next-line security/no-block-members
