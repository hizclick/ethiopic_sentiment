from bs4 import BeautifulSoup as soup
import numpy as np



class CoNLL():

    def __init__(self):  
        with open("pos.xml", "r", encoding='utf8') as f:
            
            contents = f.read()

            self.soup = soup(contents, 'lxml')      
        
        self.pos = ['<adj>','<n>','<vrel>', '<vp>','<n>','<nump>','<prep>','<numcr>','<nc>', '<np>','<adj>','<v>','<punc>','<nc>','<aux>']
        self.sentence = list()
    
    def get_title(self): 
        title = []
        for item in self.soup.find_all('title'):
            title.append(str(item).split())
    
        return title
    def get_sentence(self,txt):
        sentence = list()
        for word in txt:
            if '።' in word or word=='።':
                end = word.index('።')
                sentence.append(word[1:end+2])
                txt = txt[1:]
        return sentence
    
    def set_tagger(self,sentence):
        tag = list()
        n = 2
        for se in sentence:
            final = [se[i * n:(i + 1) * n] for i in range((len(se) + n - 1) // n )]  
            tag.append(final)

        return tag

    def append_sentence(self,tag):
        sen = ' '
        all_sentence= []
        for sent in tag:
            for words in sent:
                for w in words:
                    if w not in self.pos:
                        sen = sen + ' ' + w
            all_sentence.append(sen)
            sen = ''
        
     
        return all_sentence


    def write_file(self,all_sentence,tag):
        count = -1
        sent_id = 0

        for sent in all_sentence:
            count = count + 1
            
            if(count<len(tag)):
                text = open('o.txt', 'a', encoding='utf8')
                sent_id = sent_id + 1
                text.writelines('doc_id = mes01a1.htm' + '\n')
                text.writelines('sent_id = ' + str(sent_id) + '\n')
                text.writelines('text = ' + sent + '\n')
                c = 0
                for words in tag[count]:
                    c = c + 1
                    if(len(words)>1):
                        text.writelines(str(c)+ ' '*6 + words[0]+ ' '*3 + words[0] + ' '*3 + words[1]+ ' _ '*6 +'\n')
                c = c + 1
                text.writelines('\n'*4)
obj = CoNLL()
li =  obj.get_title()
tag = obj.get_sentence(li)
