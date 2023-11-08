const CryptJS = require('crypto-js')


function main123(page) {
    function v(t) {
        var n = t.SIGN;
        t = t.str,
            t = decodeURI(t),
            n = CryptJS.HmacSHA1(CryptJS.enc.Utf8.parse(t), n),
            n = CryptJS.enc.Base64.stringify(n).toString();
        hash = CryptJS.MD5(n).toString();
        return hash
    }

    f = "D23ABC@#56"
    j = 'https://api.eol.cn/web/api/?keyword=&page=' + page + '&province_id=&ranktype=&request_type=1&size=20&top_school_id=1476,184,101,2691,1181&type=&uri=apidata/api/gkv3/school/lists';
    l = v({
        SIGN: f,
        str: j.replace(/^\/|https?:\/\/\/?/, "")
    }).toString()
    return l
}

module.exports = main123;

// console.log(l)