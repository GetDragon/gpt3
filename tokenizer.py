from transformers import GPT2TokenizerFast

class TokenizerHelper:
    global tokenizer
    
    def __init__(self):
        self.tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

    def CountTokens(self, words_to_tokenize="The words are: man, woman, car, airplane"):
        encoded = self.tokenizer.encode(words_to_tokenize)
        decoded = [self.tokenizer.decode([t]) for t in encoded]
        print("Tokens: ", len(encoded))
        # print(encoded, "<->", decoded)
        return len(encoded)
