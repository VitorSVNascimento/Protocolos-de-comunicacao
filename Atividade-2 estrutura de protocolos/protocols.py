import bit_protocol as bp


def bit_protocol_function():
    bits_sequence = '0111111010110'
    send = bp.encode(bits_sequence)
    recive = bp.decode(send)
    show_result(bits_sequence,send,recive)

def char_protocol_function():
    pass

def show_result(original,send,recive):
    print(f'Original = {bits_sequence}')
    print(f'Enviado = {send}')
    print(f'Recebido = {recive}')


if __name__ == '__main__':
    bit_protocol_function()



