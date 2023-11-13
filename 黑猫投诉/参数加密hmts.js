const CryptJS = require('crypto-js')

function main123(timestamp, keyword) {

    var p = function (e, t, r) {
            var n = ""
                , i = t
                , a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
            e && (i = Math.round(Math.random() * (r - t)) + t);
            for (var o = 0; o < i; o++) {
                n += a[Math.round(Math.random() * (a.length - 1))]
            }
            return n
        }(!1, 16)
        , b = "$d6eb7ff91ee257475%",
        d = {
            type0: 1,
            type1: 1,
            type2: 1
        }
        c = 10

    params = {}
    params['timestamp'] = timestamp
    params['p'] = p
    // params['sign'] = sign
    params['sign'] = CryptJS.SHA256([timestamp, p, b, keyword, c, d["type" + 1]].sort().join("")).toString();
    return params
}
