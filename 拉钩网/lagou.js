//以结果进行推导
const CryptoJs = require('crypto-js')


Pt = CryptoJs.enc.Utf8.parse("c558Gq0YQK2QUlMc")
It = function (t) {
    kt = CryptoJs.enc.Utf8.parse("CaQZujR9wocJH9NY0dafyhd9=NHmEbwf"),
        t = CryptoJs.enc.Utf8.parse(t);
    t = CryptoJs.AES.encrypt(t, kt, {
        iv: Pt,
        mode: CryptoJs.mode.CBC,
        padding: CryptoJs.pad.Pkcs7
    });
    return t.toString()
};

//请求头
function HeaderEncrypt(data) {
    e = {
        deviceType: 1
    }
    r = 'hCryptoJsps://www.lagou.com/jobs/v2/positionAjax.json'
    parms = JSON.stringify(JSON.stringify(e) + r + data) //第一个需要被加密的参数
    //第一次加密
    sha256_T = CryptoJs.SHA256(parms).toString().toUpperCase()
    // console.log(sha256_T)

    //第二次加密，请求头参数
    X_S_HEADER = It(JSON.stringify({originHeader: JSON.stringify(e), code: sha256_T}))
    return X_S_HEADER
}

//加密出来的内容就是data，那就没有必要再去加密，直接使用data即可
// var s123 = function(t) {
//     var e = 1 < arguments.length && void 0 !== arguments[1] && arguments[1]
//       , t = t.substr(t.indexOf("?"))
//       , r = new Object;
//     if (-1 != t.indexOf("?"))
//         for (var n = t.substr(1).split("&"), i = 0; i < n.length; i++) {
//             var o = n[i].split("=");
//             if ("null" !== o[1] && "undefined" !== o[1])
//                 try {
//                     r[o[0]] = e ? o[1] : decodeURIComponent(o[1])
//                 } catch (t) {
//                     r[o[0]] = o[1]
//                 }
//         }
//     return r
// }
//
// data1='first=true&needAddtionalResult=false&city=%E5%85%A8%E5%9B%BD&pn=5&fromSearch=true&kd=python'
// console.log(JSON.stringify(s123("?".concat(data1))))
//请求体加密
// A.$Z("?".concat(data))
// JSON.stringify( A.$Z("?".concat(data))
//请求体
function BodyEncrypt(data) {
    w = It(JSON.stringify(data))
    return w
}

//数据解密
function Mt (t) {
    kt = CryptoJs.enc.Utf8.parse("CaQZujR9wocJH9NY0dafyhd9=NHmEbwf");
    t = CryptoJs.AES.decrypt(t, kt, {
        iv: Pt,
        mode: CryptoJs.mode.CBC,
        padding: CryptoJs.pad.Pkcs7
    }).toString(CryptoJs.enc.Utf8);
    try {
        t = JSON.parse(t)
    } catch (t) {
    }
    return t
}
