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

var sum = a => {
    return a.reduce((s, v) => s + v, 0);
};

var dist = (p, q) => {
    // KL divergence breaks down for a single value
    if (p.length === 1) {
        return Math.abs(p[0] - q[0]);
    }

    // 0 does not mean impossible, just very unlikely
    var pp = p.map(pi => pi + 0.0000001);
    var qq = q.map(qi => qi + 0.0000001);

    // https://en.wikipedia.org/wiki/Kullback-Leibler_divergence
    return sum(pp.map((pi, i) => pi * Math.log(pi / qq[i]))) / sum(pp);
};

var classify = text => {
    var n = text.length + 1;
    var freq = model.ngrams.map(g => count(text, g) / (n - g.length));
    var best = null;
    var bestDist = Infinity;
    for (const lang of Object.keys(model.freq)) {
        var d = dist(freq, model.freq[lang]);
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
