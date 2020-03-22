import re
from typing import List
from flair.data import Token

class AmharicSegmenter:
    SENT_PUNC =  []
    WORD_PUNC =  []
    def __init__(self, sent_punct, word_punct):
        if sent_punct:
            self.SENT_PUNC = sent_punct
        else:
            self.SENT_PUNC = ["።","፥","፤","፨","::","፡፡","?","!"]
        if word_punct:
            self.WORD_PUNC = word_punct
        else:
            self.WORD_PUNC =  ["።","፥","፤","፨","?","!",":","፡","፦"]
            
    def amharic_tokenizer(text: str) -> List[Token]:
        """
        Tokenizer based on space character and different Amharic punctuation marksonly.
        """
        tokens: List[Token] = []
        word = ""
        index = -1
        previchar = ''
        for index, char in enumerate(text):
            if char == " ":
                if len(word) > 0:
                    start_position = index - len(word)
                    tokens.append(
                        Token(
                            text=word, start_position=start_position, whitespace_after=True
                        )
                    )

                word = ""
            elif char in self.WORD_PUNC:
                if len(word) > 0 and previchar != char:
                    print(word)
                    start_position = index - len(word)
                    tokens.append(
                        Token(
                            text=word, start_position=start_position, whitespace_after=True
                        )
                    )
                    word = ""
                previchar = char
                word += char

            else:
                word += char
        # increment for last token in sentence if not followed by whitespace
        index += 1
        if len(word) > 0:
            print(word)
            start_position = index - len(word)
            tokens.append(
                Token(text=word, start_position=start_position, whitespace_after=False)
            )
        return tokens

    def tokenize_sentence(self, text: str):
        tokenized_text = []
        idxs = [-1]
        for sep in self.SENT_PUNC:
            idx = text.find(sep)
            if idx > 0:
                idxs.append(idx+len(sep)-1)
        idxs = sorted(idxs)
        for i in range(len(idxs)-1):
            tokenized_text.append(text[idxs[i]+1:idxs[i+1]+1].strip())
        return tokenized_text
