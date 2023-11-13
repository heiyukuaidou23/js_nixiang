

const CryptJS = require('crypto-js')

text = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0' + (new Date).getDate() + 'list'

function sha256(text){
    encryt1 = CryptJS.SHA256(text).toString()
    return encryt1
}


// console.log(sha256(ua))