
const CryptoJS = require("crypto-js");

// n = {
//     "loginMethod": "1",
//     "name": "17320469497",
//     "password": "12345678"
// }
// h = Object.assign({
//     userCode: "2",
//     channelCode: "101",
//     transTime: (new Date).getTime(),
//     transToken: "",
//     customerId: "",
//     transSerialNumber: ""
// })
l = {"body":{"loginMethod":"1","name":"17320469497","password":"12345678"},"head":{"userCode":null,"channelCode":"101","transTime":1700489947112,"transToken":"","customerId":null,"transSerialNumber":""}}
e = {
    "words": [
        -2066010810,
        -1716199041,
        -2056174356,
        -1599973162,
        -1940245320,
        976459667,
        905425065,
        705348573,
        -1220603222,
        -721255491,
        1406963955,
        -1918520169,
        1955172417,
        -1488777712,
        -1722087071,
        -1098167396,
        671400794,
        -1740722418,
        -1300952079,
        -2144146512,
        -616761203,
        -1123467933,
        1721786518,
        -272684395,
        -2112797444,
        22260608,
        -1518454334,
        1646973137,
        -912038952,
        1015240140,
        -2063232250,
        2009232472,
        1890877533,
        -847285497,
        1647720960,
        1954915813,
        358368052,
        -1748193086,
        1092597908,
        1584077655,
        -1475280083,
        136324001,
        290792613,
        105724157,
        -1169678895,
        387760054,
        -46799179,
        816885557,
        -1640363953,
        -1852482894,
        1416417120,
        -1666478473
    ],
    "sigBytes": 208
}

stringify = function(e) {
    var t = e.words
      , n = e.sigBytes
      , i = this._map;
    e.clamp();
    for (var r = [], o = 0; o < n; o += 3)
        for (var l = (t[o >>> 2] >>> 24 - o % 4 * 8 & 255) << 16 | (t[o + 1 >>> 2] >>> 24 - (o + 1) % 4 * 8 & 255) << 8 | t[o + 2 >>> 2] >>> 24 - (o + 2) % 4 * 8 & 255, a = 0; a < 4 && o + .75 * a < n; a++)
            r.push(i.charAt(l >>> 6 * (3 - a) & 63));
    var s = i.charAt(64);
    if (s)
        for (; r.length % 4; )
            r.push(s);
    return r.join("")
},

newEncrypt = function(l,e) {
    var n = CryptoJS.enc.Utf8.parse("ShWQ4zCnm5m7DDRA")
      , t = CryptoJS.enc.Utf8.parse("ShWQ4zCnm5m7DDRA")
      , e = CryptoJS.enc.Utf8.parse(l)
      , a = CryptoJS.AES.encrypt(e, n, {
        iv: t,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return CryptoJS.enc.Base64.stringify(e).toString()
}
console.log(newEncrypt(l));


// f = {
//     "body": {
//         "loginMethod": "1",
//         "name": "17320469497",
//         "password": "12345678"
//     },
//     "head": {
//         "userCode": null,
//         "channelCode": "101",
//         "transTime": 1700490207235,
//         "transToken": "",
//         "customerId": null,
//         "transSerialNumber": ""
//     }
// }
// // var f = new c(n,h);
// var C = newEncrypt(JSON.stringify(f))