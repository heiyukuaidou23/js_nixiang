const CryptoJS = require('crypto-js')


function main123(text, lastFetchTime){
    var i = CryptoJS.enc.Utf8.parse(lastFetchTime + "000")
  , a = CryptoJS.enc.Utf8.parse(lastFetchTime + "000")
  , s = CryptoJS.AES.decrypt(text.toString(), i, {
    iv: a
}).toString(CryptoJS.enc.Utf8).toString()
    return JSON.parse(s)
}
