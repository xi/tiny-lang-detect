var model = {
    'ngrams': [' t', 'ch', ' th', 'er', 'en ', 'a', 'e', 'o'],
    'freq': {
        'de': [0.0005, 0.0194, 0.0002, 0.0299, 0.0202, 0.0574, 0.1465, 0.0311],
        'en': [0.0163, 0.0035, 0.0161, 0.0135, 0.0022, 0.0897, 0.1067, 0.0715],
    },
};

var count = (text, ngram) => {
    return (text.match(new RegExp(ngram, 'g')) || []).length;
};

var dist = (a, b) => {
    return a.reduce((sum, v, i) => sum + Math.pow(v - b[i], 2), 0);
};

var classify = text => {
    var n = text.length + 1;
    var freq = model.ngrams.map(g => count(text, g) / (n - g.length));
    var best = null;
    var bestDist = Infinity;
    for (const lang of Object.keys(model.freq)) {
        var d = dist(model.freq[lang], freq);
        if (d < bestDist) {
            bestDist = d;
            best = lang;
        }
    }
    return best;
};

var textarea = document.querySelector('textarea');
var output = document.querySelector('output');
textarea.addEventListener('input', () => {
    output.textContent = classify(textarea.value);
});
