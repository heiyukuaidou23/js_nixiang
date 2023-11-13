
const CryptoJS = require("crypto-js");
str = "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"
variate = {
    "key": {
        "words": [
            863652730,
            2036741733,
            1164342596,
            1782662963
        ],
        "sigBytes": 16
    },
    "aceIV": {
        "words": [
            1719227713,
            1314533489,
            1397643880,
            1749959510
        ],
        "sigBytes": 16
    },
    "xgGjcArray": [],
    "xgGjcIndex": 0,
}
function AESDecrypt(str) {
    var nContent = CryptoJS.AES.decrypt(str, variate.key, {
        iv: variate.aceIV,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.ZeroPadding
    })
    var constr = CryptoJS.enc.Utf8.stringify(nContent)
    var data = JSON.parse(constr);
    return data;
}
console.log(AESDecrypt(str))