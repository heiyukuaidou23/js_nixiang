const CryptoJS = require("crypto-js");


s = "appKey=bcceb522717c2c49f895b561fa913d10callId=1700897370021password=e10adc3949ba59abbe56e057f20f883esessionKey=user=17312345678bcceb522717c2c49f895b561fa913d10"
sig = CryptoJS.MD5(s).toString()
console.log(sig);
