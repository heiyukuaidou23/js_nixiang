


const CryptoJS = require('crypto-js');

value = '123456'
SECURITYKEY = {
    "key": "3BAAE40770FFC289",
    "iv": "36DAE6C67FD3F514",
    "security": "䐵匠䴵"
}
function desEncrypt(value, xForm, type) {
        var keyObj = {};
        if (type == null || "aes" == type.toLowerCase()) {
            keyObj = SECURITYKEY;
            value = CryptoJS.AES.encrypt(value, CryptoJS.enc.Utf8.parse(keyObj.key), {
                iv: CryptoJS.enc.Utf8.parse(keyObj.iv)
            }).toString()
        }
        return keyObj.security + value
    }
password = desEncrypt('123456');
console.log(password);