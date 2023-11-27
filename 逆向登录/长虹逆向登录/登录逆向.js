
const CryptoJS = require("crypto-js");
message = '123456'
function encryptByDES(message) {
    var key = "passport-gw-pc";
    var keyHex = CryptoJS.enc.Utf8.parse(key);
    var encrypted = CryptoJS.DES.encrypt(message, keyHex, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return encrypted.toString();
}


pass = encryptByDES('123456')
console.log(pass);
