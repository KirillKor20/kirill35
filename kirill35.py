class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
    def get_all_words(self):
        self.all_words = {}
        self.words = []
        self.pun = [',', '.', '=', '!', '?', ';', ':', '-']
        for a in self.file_names:
            with open(a, encoding='utf-8') as file:
                for r in file:
                    r = r.lower()
                    for out in self.pun:
                        if out != ' - ':
                            r = r.replace(out, '')
                        else:
                            r = r.replace(out, ' ')
                    self.words.extend(r.split())
        self.all_words = {self.file_names[0]: self.words}
        return self.all_words

    def find(self, word):
        word = word.lower()
        new_all_words = {}
        for a, r in self.get_all_words().items():
            if word in r:
                new_all_words = {self.file_names[0]: r.index(word) + 1}
        return new_all_words

    def count(self, word):
        new_all_words = {}
        word = word.lower()
        cnt = []
        for a, r in self.get_all_words().items():
            cnt.extend(r)
        new_all_words = {self.file_names[0]: cnt.count(word)}
        return new_all_words

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего