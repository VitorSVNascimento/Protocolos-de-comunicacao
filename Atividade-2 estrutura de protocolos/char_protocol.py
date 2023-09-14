START_DELIMITE = 'STX'
END_DELIMITE = 'ETX'
BIT_STUFING_SEQUENCES = ['DLESTX','DLEETX','DLEDLE']
FIVE_NUMBERS_ONE_SEQUENCES = ['STX','ETX','DLE']

def __insert_bit_stuffing(bit_sequence:str) -> str:
    bit_sequence = bit_sequence.replace(FIVE_NUMBERS_ONE_SEQUENCES[2],BIT_STUFING_SEQUENCES[2])
    print(f'primeiro = {bit_sequence}')
    bit_sequence = bit_sequence.replace(FIVE_NUMBERS_ONE_SEQUENCES[1],BIT_STUFING_SEQUENCES[1])
    print(f'segundo = {bit_sequence}')
    return bit_sequence.replace(FIVE_NUMBERS_ONE_SEQUENCES[0],BIT_STUFING_SEQUENCES[0])
    pass

def __insert_framing_flags(bit_sequence:str) -> str:
    return f'{START_DELIMITE}{bit_sequence}{END_DELIMITE}'
    pass

def __remove_bit_stuffing(bit_sequence:str) -> str:
    bit_sequence = bit_sequence.replace(BIT_STUFING_SEQUENCES[0],FIVE_NUMBERS_ONE_SEQUENCES[0])
    bit_sequence = bit_sequence.replace(BIT_STUFING_SEQUENCES[1],FIVE_NUMBERS_ONE_SEQUENCES[1])
    return bit_sequence.replace(BIT_STUFING_SEQUENCES[2],FIVE_NUMBERS_ONE_SEQUENCES[2])
    pass

def __remove_framing_flags(bit_sequence:str) -> str:
    return bit_sequence[len(START_DELIMITE):-len(END_DELIMITE)]
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