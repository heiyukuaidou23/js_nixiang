



const CryptoJS = require('crypto')
function md5(text){
    return CryptoJS.createHash('md5').update(text).digest('hex')
}
apwd = '123456'
pwd = md5(apwd.substr(0, 16))
console.log(pwd);