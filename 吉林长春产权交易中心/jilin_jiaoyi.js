

codeStr = "",
pubPass = "BX1o65CoobwcDP33iQW6ld1OyIPsNzF1",




random = function(e, t) {
    return void 0 === e && (e = 0),
    void 0 === t && (t = 1e4),
    Math.round(Math.random() * (t - e) + e)
}

randomStr = function(e) {
    for (var t = [], n = 0; n < e; n++)
        t.push(random(0, 35).toString(36));
    return t.join("")
}

pubPassNum = [],
publicKey = ""

stringChangeASCIINumberArrs = function(e) {
    for (var t = [], n = 0; n < e.length; n++)
        t.push(e.charCodeAt(n));
    return t
}

setPass = function(e) {
    pubPassNum = stringChangeASCIINumberArrs(e)
}
setPass(pubPass)

// console.log(pubPassNum)

uuid = function(t, n) {
    void 0 === t && (t = 16),
    void 0 === n && (n = !1),
    !n && t < 16 && (console.error("uuid useCase=false 时 len 不能小于 16"),
        t = 16),
    n && t < 12 && (console.error("uuid useCase=true 时 len 不能小于 12"),
        t = 12);
    var i = ((new Date).getTime() + 1e14).toString();
    return i += ("000" + 'NaN').substr(-3, 3),
        i = n ? parseInt(i).to62() : parseInt(i).toString(36),
        i += randomStr(t),
        i = i.substr(0, t),
        i
}


encryptCode = function(e) {
    for (var t = encodeURI(e), n = [], i = 0, r = "", o = random(16, 32), a = randomStr(o), s = stringChangeASCIINumberArrs(a), l = 0, c = 0, u = 0, h = 0; h < t.length; h++)
        i = t.charCodeAt(h),
        l == pubPassNum.length && (l = 0),
        i += pubPassNum[l],
        l++,
        c == s.length && (c = 0),
        i += s[c],
        c++,
        u += i,
        u > 65535 && (u -= 65535),
        r = i.toString(36),
        r = ("00" + r).substr(-2, 2),
        1 == r.length && (r = "0" + r),
        n.push(r);
    var d = "";
    return d = u.toString(36),
    d = ("0000" + r).substr(-4, 4),
    n.unshift(a),
    n.unshift(o.toString(36)),
    n.unshift(d),
    n.join("")
}



 o = {
    "id": uuid(),
    "projectKey": "honsan_cloud_ccprec",
    "clientKey": "rtd9inky1ls8dtla",
    "token": null,
    "clientDailyData": {},
    "acts": []
}



o.acts.push([
    {
        "id": uuid(),
        "fullPath": "/ccprec.com.cn.web/client/info/cqweb_nonphy_cqzr",
        "args": [
            2,
            20,
            null
        ]
    }
])


var a = JSON.stringify(o)
// t = JSON.stringify(a)
console.log(encryptCode(a))

