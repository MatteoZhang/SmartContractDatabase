d1 = {
    "0": [
        "@ dev multiplies two numbers , throws on overflow ."
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
        "@ param owner the address from which the balance will be retrieved @ return the balance"
    ],
    "5": [
        "send value amount of tokens to address to"
    ],
    "6": [
        "get the address to query ."
    ],
    "7": [
        "send value amount of tokens to address to"
    ],
    "8": [
        "@ dev emitted when value tokens are moved from one account ( from ) to another ( to ) . note that value may be zero ."
    ],
    "9": [
        "@ param owner the address of the account owning tokens @ param spender the address of the account able to transfer the tokens @ return amount of constant allowed value"
    ],
    "10": [
        "@ dev transfer tokens from one address to another . @ param from the address you want to send tokens from . @ param to the address you want to"
    ],
    "11": [
        "set allowance for other address allows spender to spend no more than value tokens on your behalf @ param spender the address authorized to spend @ param value the max"
    ],
    "12": [
        "@ dev emitted when the allowance of a spender for an owner is set by a call to { approve } . value is the new allowance ."
    ],
    "13": [
        "@ dev distr token transfer @ param to the address of the sender @ param value the amount of token to be transferred @ return true if the given value"
    ],
    "14": [
        "@ return total amount of tokens"
    ],
    "15": [
        "@ param owner the address from which the balance will be retrieved @ return the balance"
    ],
    "16": [
        "@ dev emitted when value tokens are moved from one account ( from ) to another ( to ) . note that value may be zero ."
    ],
    "17": [
        "@ dev emitted when the allowance of a spender for an owner is set by a call to { approve } . value is the new allowance ."
    ],
    "18": [
        "events"
    ],
    "19": [
        "@ dev emitted during finish minting"
    ],
    "20": [
        "@ dev emitted when value tokens are burnt from one account ( burner ) @ param burner address which burned tokens @ param value amount of tokens burned"
    ],
    "21": [
        "@ dev tokens can be minted only before minting finished ."
    ],
    "22": [
        "@ dev throws if called by any account other than the owner ."
    ],
    "23": [
        "@ dev throws if called by any account other than the blacklist"
    ],
    "24": [
        "@ dev gets the balance of database"
    ],
    "25": [
        "@ dev allows the current owner to transfer control of the contract to a new owner . @ param new owner the address to transfer ownership to ."
    ],
    "26": [
        "@ notice distribution tokens and nothing the function"
    ],
    "27": [
        "@ dev private function to distr alpaca"
    ],
    "28": [
        "@ dev fallback function to accept eth . goblins will send eth back the pool ."
    ],
    "29": [
        "@ dev get investor staking contract ."
    ],
    "30": [
        "@ dev gets the balance of the specified address . @ param owner the address to query the the balance of . @ return an uint256 representing the amount owned"
    ],
    "31": [
        "mitigates the erc20 short address attack"
    ],
    "32": [
        "@ dev transfer token for a specified address @ param to the address to transfer to . @ param amount the amount to be transferred ."
    ],
    "33": [
        "@ dev moves amount tokens from sender to recipient using the allowance mechanism . amount is then deducted from the caller ' s allowance . returns a boolean value indicating"
    ],
    "34": [
        "allow spender to withdraw from your account , multiple times . to change the approve amount you first have to reduce the addresses allowance to zero by calling approve ("
    ],
    "35": [
        "@ dev function to check the amount of tokens that an owner allowed to a spender . @ param owner address the address which owns the funds . @ param"
    ],
    "36": [
        "@ param token address the address of the token contract @ return the token address"
    ],
    "37": [
        "@ dev withdraw ether from contract @ param ether address uint256 amount of ether transfer"
    ],
    "38": [
        "@ dev burns a specific amount of tokens . @ param value the amount of token to be burned . no need to require value < total supply , since"
    ],
    "39": [
        "@ dev withdraw ether to withdraw tokens from contract"
    ]
}
d2 = {}
file_path = "smart_contracts/SiaCashCoin.comment"


def merge_dict(d1, d2, file_path):
    for c in range(len(d2)):
        d1[str(len(d1))] = d2[str(c)]

    with open(file_path, "w") as file:
        for c in d1:
            file.write(d1[c][0] + "\n")


merge_dict(d1, d2, file_path)
