
const CryptoJS = require("crypto-js");
encryptByDES = function(t){
    return CryptoJS.MD5(t + "TuD00Iqz4ge7gzIe2rmjSAFFKtaIBmnr8S").toString()
}

a = encryptByDES('123456');
console.log(a);