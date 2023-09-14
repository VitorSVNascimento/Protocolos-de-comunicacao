import bit_protocol as bp
import char_protocol as cp


def bit_protocol_function():
    bits_sequence = '0111111010110'
    send = bp.encode(bits_sequence)
    recive = bp.decode(send)
    show_result(bits_sequence,send,recive)

def char_protocol_function():
    bits_sequence = 'STX,DLE,STX,ETX'
    send = cp.encode(bits_sequence)
    recive = cp.decode(send)
    show_result(bits_sequence,send,recive)

def show_result(original,send,recive):
    print(f'Original = {original}')
    print(f'Enviado = {send}')
    print(f'Recebido = {recive}')


if __name__ == '__main__':
    char_protocol_function()



