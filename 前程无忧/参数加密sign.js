const CryptoJS = require('crypto-js')

function main123(e){
    sign_key = 'abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b'
    const sha256Hash = CryptoJS.HmacSHA256(e,sign_key);

    const sha256Hex = sha256Hash.toString(CryptoJS.enc.Hex);
    return sha256Hex
}