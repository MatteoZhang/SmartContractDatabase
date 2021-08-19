d1 = {
    "0": [
        "@ dev multiply tow integers"
    ],
    "1": [
        "@ dev integer division of two numbers , truncating the quotient . assert ( b > 0 ) ; solidity automatically throws when dividing by 0 assert ( a b"
    ],
    "2": [
        "@ dev subtracts two numbers , throws on overflow ( i . e . if subtrahend is greater than minuend ) ."
    ],
    "3": [
        "@ dev adds two numbers , throws on overflow ."
    ],
    "4": [
        "@ dev returns the integer division of two unsigned integers , reverting on division by zero . the result is rounded towards zero . counterpart to solidity ' s operator"
    ],
    "5": [
        "@ dev returns the subtraction of two unsigned integers , reverting on overflow ( when the result is negative ) . counterpart to solidity ' s operator . requirements :"
    ],
    "6": [
        "@ dev returns the greater of two numbers ."
    ],
    "7": [
        "@ dev returns the unlockable of two numbers ."
    ],
    "8": [
        "@ dev saftey logic ."
    ],
    "9": [
        "@ param who the address to query . @ return the balance of the specified address ."
    ],
    "10": [
        "@ dev transfer token for a specified address @ param to the address to transfer to . @ param value the amount to be transferred ."
    ],
    "11": [
        "@ dev emitted when value tokens are moved from one account ( from ) to another ( to ) . note that value may be zero ."
    ],
    "12": [
        "@ dev fix for the erc20 short address attack ."
    ],
    "13": [
        "@ dev transfer token for a specified address @ param to the address to transfer to . @ param value the amount to be transferred ."
    ],
    "14": [
        "what is the balance of a particular account ?"
    ],
    "15": [
        "@ dev function to check the amount of tokens than an owner has allowed to a spender . @ param owner the address which owns the funds . @ param"
    ],
    "16": [
        "@ dev erc20 transfer from , modified such that an allowance of max uint represents an unlimited amount . @ param from address to transfer from . @ param to"
    ],
    "17": [
        "@ dev approve the passed address to spend the specified amount of tokens on behalf of msg . sender . this method is included for erc20 compatibility . increase allowance"
    ],
    "18": [
        "@ dev emitted when the allowance of a spender for an owner is set by a call to { approve } . value is the new allowance ."
    ],
    "19": [
        "@ dev transfer tokens from one address to another @ param from address the address which you want to send tokens from @ param to address the address which you"
    ],
    "20": [
        "allow spender to withdraw from your account , multiple times . to change the approve amount you first have to reduce the addresses allowance to zero by calling approve ("
    ],
    "21": [
        "@ dev function to check the amount of tokens than an owner allowed to a spender . @ param owner address the address which owns the funds . @ param"
    ],
    "22": [
        "@ dev the ownable constructor sets the original owner of the contract to the sender account ."
    ],
    "23": [
        "@ dev throws if called by any account other than the owner ."
    ],
    "24": [
        "@ dev allows the current owner to transfer control of the contract to a new owner . @ param new owner the address to transfer ownership to ."
    ],
    "25": [
        "pausable"
    ],
    "26": [
        "events"
    ],
    "27": [
        "@ dev modifier to make a function callable only when the contract is paused ."
    ],
    "28": [
        "@ dev modifier to allow actions only when the contract is not paused"
    ],
    "29": [
        "@ dev called by the owner to pause , triggers stopped state"
    ],
    "30": [
        "@ dev called by the owner to unpause , returns to normal state"
    ],
    "31": [
        "transfer tokens send value tokens to to from your account @ param to the address of the recipient @ param value the amount to send"
    ],
    "32": [
        "@ dev transfer tokens from one address to another . @ param from the address you want to send tokens from . @ param to the address you want to"
    ],
    "33": [
        "total supply"
    ]
}
d2 = {}
file_path = "smart_contracts/VocToken.comment"


def merge_dict(d1, d2, file_path):
    for c in range(len(d2)):
        d1[str(len(d1))] = d2[str(c)]

    with open(file_path, "w") as file:
        for c in d1:
            file.write(d1[c][0] + "\n")


merge_dict(d1, d2, file_path)
