class Converter:

    @staticmethod
    def dec_to_gray(number: int, bit_size: int) -> str:
        binary_string = Converter.__dec_to_bin(number)
        gray_string = Converter.__bin_to_gray(binary_string).zfill(bit_size)
        return f"{gray_string}"

    @staticmethod
    def gray_to_dec(gray_code: str) -> int:
        binary_string = Converter.__gray_to_bin(gray_code)
        number = Converter.__bin_to_dec(binary_string)
        return number

    def __dec_to_bin(number):
        return f"{bin(number)[2:]}"

    def __bin_to_dec(binary_string):
        return int(binary_string, 2)

    def __bin_to_gray(binary_string):
        binary = int(binary_string, 2)
        binary ^= (binary >> 1)
        return bin(binary)[2:]

    def __gray_to_bin(gray_string):
        n = int(gray_string, 2)
        mask = n
        while mask != 0:
            mask >>= 1
            n ^= mask
        return bin(n)[2:]
