


const CryptoJS = require("crypto-js");

mobile= "13436294431"

function encryptByDES(mobile) {
    var keyHex = CryptoJS.enc.Utf8.parse("Dsf9CDTfkto=");
    var encrypted = CryptoJS.DES.encrypt(mobile, keyHex, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return encrypted.toString();
}
console.log(encryptByDES(mobile))