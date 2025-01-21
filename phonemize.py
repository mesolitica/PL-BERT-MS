import string
from text_normalize import normalize_text

def phonemize(text, global_phonemizer, tokenizer):
    text = normalize_text(text)
    words = tokenizer.tokenize(text)
    
    phonemes_bad = [global_phonemizer.phonemize([word], strip=True)[0] if word not in string.punctuation else word for word in words]
    input_ids = []
    phonemes = []
    
    for i in range(len(words)):
        word = words[i]
        phoneme = phonemes_bad[i]
        if word == '[UNK]':
            continue
        
        input_ids.append(tokenizer.encode(word)[0])
        phonemes.append(phoneme)
        
    assert len(input_ids) == len(phonemes)
    return {'input_ids' : input_ids, 'phonemes': phonemes}