const CryptoJS = require("crypto-js");


function md5encrypt(e) {
    var a = CryptoJS.MD5('www_maomaozu_com').toString()
    return a = 0 == e ? a.substring(0, 16) : a.substring(16, 32)
}
// 用来保存生成的数据的数组
const dataArray = [];


for (let page = 1; page <= 151; page++) {
     a = {
        "Type": 0,
        "page": page,
        "expire": (new Date).getTime()
    };

function aes_encrypt(e) {
    return AESdecrypt(md5encrypt(0), e)
}

function AESdecrypt(e, a) {
    return e = CryptoJS.enc.Utf8.parse(e),
        a = CryptoJS.enc.Utf8.parse(a),
        CryptoJS.AES.encrypt(a, e, {
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7,
            iv: e
        }).toString()
}

    data = aes_encrypt(JSON.stringify(a))
    dataArray.push(data);
}

// 使用join函数将数据用逗号隔开并输出
joinedData = dataArray.join(',');
console.log(joinedData);