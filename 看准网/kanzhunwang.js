
const cryptojs = require('crypto-js')

function get_kiv (e) {
    void 0 === e && (e = 16);
    for (var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(""), n = "", r = 0; r < e; r++) {
        n += t[Math.ceil(61 * Math.random())]
    }
    return n
}


// key: o.enc.Utf8.parse(e),
// mode: o.mode.CBC,
// pad: o.pad.Pkcs7

function l (e, t) {
    var key = cryptojs.enc.Utf8.parse('G$$QawckGfaLB97r')
    void 0 === e && (e = ""),
    void 0 === t && (t = "");
    var r = cryptojs.AES.encrypt(e.toString(), key, {
        iv: cryptojs.enc.Utf8.parse(t),
        mode: cryptojs.mode.CBC,
        padding: cryptojs.pad.Pkcs7
    });
    return r = r.toString()
}
function get (e, t) {
    return e ? ("string" != typeof e && (e = e.toString()),
    l(e, t.iv)) : ""
}



function get_b(n){
    var n = JSON.stringify(n);
    var a = get_kiv();
    return get(n, {iv: a}).replace(/\//g, "_").replace(/\+/g, "-").replace(/=/g, "~");

}

console.log(get_b());


// a = M._A()

console.log(get_kiv());