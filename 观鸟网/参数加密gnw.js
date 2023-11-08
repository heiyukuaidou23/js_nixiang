
const crypto1 = require('crypto-js')
function md5s(arg){
    return crypto1.MD5(arg).toString()
}



function getUuid() {
    var s = [];
    var a = "0123456789abcdef";
    for (var i = 0; i < 32; i++) {
        s[i] = a.substr(Math.floor(Math.random() * 0x10), 1)
    }
    s[14] = "4";
    s[19] = a.substr((s[19] & 0x3) | 0x8, 1);
    s[8] = s[13] = s[18] = s[23];
    var b = s.join("");
    return b
}

c = 1699275333000
d= "624d328438ce734dfb38e893dbe495a9"
data = {"limit":"20","page":"6"}
e = JSON.stringify(data)
var sign = md5s(e + d + c);
console.log(sign);