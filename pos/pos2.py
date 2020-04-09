class tag():
    def __init__(self):  
        infile = open('pos2.txt', "r", encoding='utf-8')
        self.lines = infile.readlines()
        self.sen = []
        self.tag = []
    def tagger(self):

        for line in self.lines:
            self.tag.append(line.split(' '))

        for words in self.tag:
            for w in words:
                self.sen.append(w.split('/'))

        return self.sen

obj = tag()
print(obj.tagger())
