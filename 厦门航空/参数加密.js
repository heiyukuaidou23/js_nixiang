

const CryptoJS = require("crypto-js");


A = function() {
    var e = {}
      , t = -30 || 0
      , a = (new Date).getTime() + t
      , n = "".concat("Mozilla", "_").concat(function() {
        for (var e = [], t = 0; t < 32; t++)
            e[t] = "0123456789abcdef".substr(Math.floor(16 * Math.random()), 1);
        return e.join("")
    }());
    e["Device-Id"] = n;
    var r = function(e) {
        var i = n[0]
          , l = n[1]
        [0].value
          , u = {}
            s = "ojts",
            o = "CipherKey5"
          , c = ["12345678901234567890123456789012", "qwefqwefqwefqwefqwefqwefqwefqwef", "QWDSQWDSQWDSQWDSQWDSQWDSQWDSQWDS", "12345678901234567890123456789012", "qwefqwefqwefqwefqwefqwefqwefqwef", "QWDSQWDSQWDSQWDSQWDSQWDSQWDSQWDS"]
          , d = "".concat(i, "_").concat(c[e])
          , p = CryptoJS.MD5("".concat(s).concat(o)).toString().substring(8, 24)
          , m = CryptoJS.enc.Utf8.parse(CryptoJS.MD5("".concat(s).concat(o)).toString().substring(8, 24));
        u["Crypto-Chars"] = e <= 2 ? CryptoJS.AES.encrypt("".concat(d, "_").concat(l), m, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        }).toString() : CryptoJS.MD5("".concat(d, "_").concat(l, "_").concat(p)).toString();
        var f = CryptoJS.enc.Utf8.parse(CryptoJS.MD5(s).toString().substring(8, 24));
        return u["Crypto-Random"] = CryptoJS.AES.encrypt("".concat(d), f, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        }).ciphertext.toString(CryptoJS.enc.Base64),
        u
    }(Math.abs(a % 6), a, n);
    return e["Crypto-Chars"] = r["Crypto-Chars"],
    e["Crypto-Random"] = r["Crypto-Random"],
    e
};
console.log(A());