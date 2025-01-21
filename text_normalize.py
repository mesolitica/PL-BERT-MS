from malaya_speech.tts import load_text_ids
from functools import cache

@cache
def get_normalizer():
    normalizer = load_text_ids(pad_to = None, understand_punct = True, is_lower = False)
    return normalizer


def normalize_text(text, add_fullstop = False):

    normalizer = get_normalizer()
    t, ids = normalizer.normalize(text, add_fullstop = add_fullstop)
    return t

if __name__ == '__main__' : 
    text = 'hello (23 Jan 2020)'
    out = normalize_text(text)
    print(out)

