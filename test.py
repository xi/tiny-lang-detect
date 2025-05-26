import argparse
import json
import math

LANG_MAP = {
    'afr': 'af',
    'ara': 'ar',
    'bul': 'bg',
    'ben': 'bn',
    'cat': 'ca',
    'ces': 'cs',
    'cym': 'cy',
    'dan': 'da',
    'deu': 'de',
    'ell': 'el',
    'eng': 'en',
    'spa': 'es',
    'est': 'et',
    'fas': 'fa',
    'fin': 'fi',
    'fra': 'fr',
    'guj': 'gu',
    'heb': 'he',
    'hin': 'hi',
    'hrv': 'hr',
    'hun': 'hu',
    'ind': 'id',
    'ita': 'it',
    'jpn': 'ja',
    'kan': 'kn',
    'kor': 'ko',
    'lit': 'lt',
    'lav': 'lv',
    'mkd': 'mk',
    'mal': 'ml',
    'mar': 'mr',
    'nep': 'ne',
    'nld': 'nl',
    'nor': 'no',
    'pan': 'pa',
    'pol': 'pl',
    'por': 'pt',
    'ron': 'ro',
    'rus': 'ru',
    'slk': 'sk',
    'slv': 'sl',
    'som': 'so',
    'sqi': 'sq',
    'swe': 'sv',
    'swa': 'sw',
    'tam': 'ta',
    'tel': 'te',
    'tha': 'th',
    'tgl': 'tl',
    'tur': 'tr',
    'ukr': 'uk',
    'urd': 'ur',
    'vie': 'vi',
    'zho': 'zh-cn',
    # 'zho': 'zh-tw',
}


def probability(p, q):
    # 0 does not mean impossible, just very unlikely
    a = 0.0000001
    qq = [qi * (1 - 2 * a) + a for qi in q]
    return math.prod(qi ** pi * (1 - qi) ** (1 - pi) for pi, qi in zip(p, qq))


def classify(model, text):
    n = len(text) + 1
    freq = [text.count(g) / (n - len(g)) for g in model['ngrams']]
    return max(model['freq'], key=lambda lang: probability(freq, model['freq'][lang]))


def test(model):
    total = 0
    correct = 0

    with open('data/wili/x_test.txt') as fh:
        with open('data/wili/y_test.txt') as fh2:
            for lang, text in zip(fh2, fh):
                lang = LANG_MAP.get(lang.rstrip())
                text = text.rstrip()
                if lang in model['freq']:
                    actual = classify(model, text)
                    total += 1
                    if actual == lang:
                        correct += 1

    print(
        f'{correct} out of {total} samples were detected correctly'
        f' ({correct / total:.1%})'
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('model')
    args = parser.parse_args()

    with open(args.model) as fh:
        model = json.load(fh)

    test(model)
