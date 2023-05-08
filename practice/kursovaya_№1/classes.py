
class BasicWord:
    def __init__(self, base_word, subwords):
        self.base_word = base_word
        self.subwords = subwords

    #проверка введенного слова в списке допустимых подслов
    def has_subword(self, word):
        if word.lower() in self.subwords:
            return True

        return False

    #подсчет кол-ва подслов
    def subwords_len(self):
        return len(self.subwords)


    def __repr__(self):
        return f"{self.base_word} содержит {len(self.subwords)} слов"



class Player:
    def __init__(self, name):
        self.name = name
        self.used_words = []

    #получение кол-ва использованных слов
    def count_used_words(self):
        return len(self.used_words)

    #добавление слова в использованные слова(в список)
    def add_word_to_used(self, new_word):
        self.used_words.append(new_word)

    #проверка использования данного слова до этого
    def has_used(self, word):
        # return word in self.used_words #хуйня тоже работает но хуй пойми как
        if word.lower() in self.used_words:
            return True
        return False

    def __repr__(self):
        return f"{self.name} угадал слова: {', '.join(self.used_words)}"

