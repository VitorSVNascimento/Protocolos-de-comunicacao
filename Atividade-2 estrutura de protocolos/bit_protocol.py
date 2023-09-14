FRAMING_FLAG = '01111110'
BIT_STUFING_SEQUENCE = '111110'
FIVE_NUMBERS_ONE_SEQUENCE = '11111'

def __insert_bit_stuffing(bit_sequence:str) -> str:
    return bit_sequence.replace(FIVE_NUMBERS_ONE_SEQUENCE,BIT_STUFING_SEQUENCE)
    pass

def __insert_framing_flags(bit_sequence:str) -> str:
    return f'{FRAMING_FLAG}{bit_sequence}{FRAMING_FLAG}'
    pass

def __remove_bit_stuffing(bit_sequence:str) -> str:
    return bit_sequence.replace(BIT_STUFING_SEQUENCE,FIVE_NUMBERS_ONE_SEQUENCE)
    pass

def __remove_framing_flags(bit_sequence:str) -> str:
    return bit_sequence[len(FRAMING_FLAG):-len(FRAMING_FLAG)]
    pass

def encode(bit_sequence:str) -> str:
    message = __insert_bit_stuffing(bit_sequence)
    message = __insert_framing_flags(message)
    return message


def decode(bit_sequence:str) -> str:
    message =  __remove_framing_flags(bit_sequence)
    message =  __remove_bit_stuffing(message)
    return message
    

#0111111010110