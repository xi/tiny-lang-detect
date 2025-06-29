var model = {
    'ngrams': ['o', 'e', 'a', 'en ', 'er', ' th', 'ch', ' t'],
    'freq': {
        'en': [0.0716, 0.1067, 0.0897, 0.0023, 0.0135, 0.0161, 0.0036, 0.0164],
        'de': [0.0311, 0.1466, 0.0574, 0.0202, 0.0299, 0.0002, 0.0195, 0.0006],
    },
};

var count = (text, ngram) => {
    return (text.match(new RegExp(ngram, 'g')) || []).length;
};

var prod = a => a.reduce((s, v) => s * v, 1);
var max = (a, key) => a.reduce((m, v) => !m || key(v) > key(m) ? v : m, null);

var probability = (p, q) => {
    return prod(p.map((pi, i) => Math.pow(q[i], pi) * Math.pow(1 - q[i], 1 - pi)));
};

var classify = text => {
    var n = text.length + 1;
    var freq = model.ngrams.map(g => count(text, g) / (n - g.length));
    return max(Object.keys(model.freq), lang => probability(freq, model.freq[lang]));
};

var textarea = document.querySelector('textarea');
var output = document.querySelector('output');
textarea.addEventListener('input', () => {
    output.textContent = classify(textarea.value);
});
