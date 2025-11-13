class FenceCipher:
    @staticmethod
    def encrypt(text):
        lst_text = [i for i in text if i != " "]
        new_text = ""
        for i, j in enumerate(lst_text):
            if i % 2 == 0:
                new_text += j
        for i, j in enumerate(lst_text):
            if i % 2 != 0:
                new_text += j

        return new_text

    @staticmethod
    def decrypt(text_enc):
        half_text = text_enc[:len(text_enc) // 2 + 1]
        half_2_text = text_enc[len(text_enc) // 2 + 1:]
        new_text = ""
        count_idx = 0
        while len(new_text) != len(text_enc):
            if count_idx == len(half_text):
                new_text += half_2_text[count_idx]

            if count_idx == len(half_2_text):
                new_text += half_text[count_idx]

            else:
                new_text += half_text[count_idx]
                new_text += half_2_text[count_idx]
                count_idx += 1
        return new_text








print(FenceCipher.decrypt("rtrsmeunoe"))


