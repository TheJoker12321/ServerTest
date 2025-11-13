class CaesarCipher:
    @staticmethod
    def cipher(text, offset: int,status_cipher ):
        lst_chr = [chr(i) for i in range(97,123)]
        new_text = ""
        for i in text:
            if i == " ":
                new_text += " "
            else:
                if status_cipher == "encrypt":
                    new_text += lst_chr[(lst_chr.index(i) + offset) % len(lst_chr)]
                else:
                    new_text += lst_chr[(lst_chr.index(i) - offset) % len(lst_chr)]
        return new_text







