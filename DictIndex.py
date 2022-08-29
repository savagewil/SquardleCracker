import re


class DictIndex:
    def __init__(self, word_list:set):
        self.index = {}
        self.end = False
        for word in word_list:
            if word == "":
                self.end = True
            else:
                letter, end = word[0], word[1:]
                if letter in self.index:
                    self.index[letter].add(end)
                else:
                    self.index[letter] = {end}
        for letter in self.index.keys():
            self.index[letter] = DictIndex(self.index[letter])

    def __contains__(self, item:str):
        if item == "":
            return self.end
        else:
            if item[0] in self.index:
                return self.index[item[0]].__contains__(item[1:])
            else:
                return False

    def prefix(self, item: str):
        if item == "":
            return self
        else:
            if item[0] in self.index:
                return self.index[item[0]].prefix(item[1:])
            else:
                return None

    @staticmethod
    def from_dict_file(dictionary_path:str):
        with open(dictionary_path, "r") as file:
            word_list = {re.sub(r'[^a-zA-Z]', '', word) for word in file.readlines()}
        return DictIndex(word_list)
