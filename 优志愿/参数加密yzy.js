

r123 = {
    rotl: function(e, t) {
        return e << t | e >>> 32 - t
    },
    rotr: function(e, t) {
        return e << 32 - t | e >>> t
    },
    endian: function(e) {
        if (e.constructor == Number)
            return 16711935 & r123.rotl(e, 8) | 4278255360 & r123.rotl(e, 24);
        for (var t = 0; t < e.length; t++)
            e[t] = r123.endian(e[t]);
        return e
    },
    randomBytes: function(e) {
        for (var t = []; e > 0; e--)
            t.push(Math.floor(256 * Math.random()));
        return t
    },
    bytesToWords: function(e) {
        for (var t = [], r = 0, n = 0; r < e.length; r++,
        n += 8)
            t[n >>> 5] |= e[r] << 24 - n % 32;
        return t
    },
    wordsToBytes: function(e) {
        for (var t = [], r = 0; r < 32 * e.length; r += 8)
            t.push(e[r >>> 5] >>> 24 - r % 32 & 255);
        return t
    },
    bytesToHex: function(e) {
        for (var t = [], r = 0; r < e.length; r++)
            t.push((e[r] >>> 4).toString(16)),
            t.push((15 & e[r]).toString(16));
        return t.join("")
    },
    hexToBytes: function(e) {
        for (var t = [], r = 0; r < e.length; r += 2)
            t.push(parseInt(e.substr(r, 2), 16));
        return t
    },
    bytesToBase64: function(e) {
        for (var r = [], n = 0; n < e.length; n += 3)
            for (var i = e[n] << 16 | e[n + 1] << 8 | e[n + 2], o = 0; o < 4; o++)
                8 * n + 6 * o <= 8 * e.length ? r.push(t.charAt(i >>> 6 * (3 - o) & 63)) : r.push("=");
        return r.join("")
    },
    base64ToBytes: function(e) {
        e = e.replace(/[^A-Z0-9+\/]/gi, "");
        for (var r = [], n = 0, i = 0; n < e.length; i = ++n % 4)
            0 != i && r.push((t.indexOf(e.charAt(n - 1)) & Math.pow(2, -2 * i + 8) - 1) << 2 * i | t.indexOf(e.charAt(n)) >>> 6 - 2 * i);
        return r
    }
};

var n123 = {
    utf8: {
        stringToBytes: function(e) {
            return n123.bin.stringToBytes(unescape(encodeURIComponent(e)))
        },
        bytesToString: function(e) {
            return decodeURIComponent(escape(n123.bin.bytesToString(e)))
        }
    },
    bin: {
        stringToBytes: function(e) {
            for (var t = [], r = 0; r < e.length; r++)
                t.push(255 & e.charCodeAt(r));
            return t
        },
        bytesToString: function(e) {
            for (var t = [], r = 0; r < e.length; r++)
                t.push(String.fromCharCode(e[r]));
            return t.join("")
        }
    }
};

function des (e, r) {
    e.constructor == String ? e = r && "binary" === r.encoding ? o.stringToBytes(e) : n123.utf8.stringToBytes(e) : i(e) ? e = Array.prototype.slice.call(e, 0) : Array.isArray(e) || e.constructor === Uint8Array || (e = e.toString());
    for (var s = r123.bytesToWords(e), u = 8 * e.length, c = 1732584193, f = -271733879, d = -1732584194, l = 271733878, h = 0; h < s.length; h++)
        s[h] = 16711935 & (s[h] << 8 | s[h] >>> 24) | 4278255360 & (s[h] << 24 | s[h] >>> 8);
    s[u >>> 5] |= 128 << u % 32,
    s[14 + (u + 64 >>> 9 << 4)] = u;
    var p = _ff
      , b = _gg
      , y = _hh
      , m = _ii;
    for (h = 0; h < s.length; h += 16) {
        var g = c
          , v = f
          , _ = d
          , w = l;
        c = p(c, f, d, l, s[h + 0], 7, -680876936),
        l = p(l, c, f, d, s[h + 1], 12, -389564586),
        d = p(d, l, c, f, s[h + 2], 17, 606105819),
        f = p(f, d, l, c, s[h + 3], 22, -1044525330),
        c = p(c, f, d, l, s[h + 4], 7, -176418897),
        l = p(l, c, f, d, s[h + 5], 12, 1200080426),
        d = p(d, l, c, f, s[h + 6], 17, -1473231341),
        f = p(f, d, l, c, s[h + 7], 22, -45705983),
        c = p(c, f, d, l, s[h + 8], 7, 1770035416),
        l = p(l, c, f, d, s[h + 9], 12, -1958414417),
        d = p(d, l, c, f, s[h + 10], 17, -42063),
        f = p(f, d, l, c, s[h + 11], 22, -1990404162),
        c = p(c, f, d, l, s[h + 12], 7, 1804603682),
        l = p(l, c, f, d, s[h + 13], 12, -40341101),
        d = p(d, l, c, f, s[h + 14], 17, -1502002290),
        c = b(c, f = p(f, d, l, c, s[h + 15], 22, 1236535329), d, l, s[h + 1], 5, -165796510),
        l = b(l, c, f, d, s[h + 6], 9, -1069501632),
        d = b(d, l, c, f, s[h + 11], 14, 643717713),
        f = b(f, d, l, c, s[h + 0], 20, -373897302),
        c = b(c, f, d, l, s[h + 5], 5, -701558691),
        l = b(l, c, f, d, s[h + 10], 9, 38016083),
        d = b(d, l, c, f, s[h + 15], 14, -660478335),
        f = b(f, d, l, c, s[h + 4], 20, -405537848),
        c = b(c, f, d, l, s[h + 9], 5, 568446438),
        l = b(l, c, f, d, s[h + 14], 9, -1019803690),
        d = b(d, l, c, f, s[h + 3], 14, -187363961),
        f = b(f, d, l, c, s[h + 8], 20, 1163531501),
        c = b(c, f, d, l, s[h + 13], 5, -1444681467),
        l = b(l, c, f, d, s[h + 2], 9, -51403784),
        d = b(d, l, c, f, s[h + 7], 14, 1735328473),
        c = y(c, f = b(f, d, l, c, s[h + 12], 20, -1926607734), d, l, s[h + 5], 4, -378558),
        l = y(l, c, f, d, s[h + 8], 11, -2022574463),
        d = y(d, l, c, f, s[h + 11], 16, 1839030562),
        f = y(f, d, l, c, s[h + 14], 23, -35309556),
        c = y(c, f, d, l, s[h + 1], 4, -1530992060),
        l = y(l, c, f, d, s[h + 4], 11, 1272893353),
        d = y(d, l, c, f, s[h + 7], 16, -155497632),
        f = y(f, d, l, c, s[h + 10], 23, -1094730640),
        c = y(c, f, d, l, s[h + 13], 4, 681279174),
        l = y(l, c, f, d, s[h + 0], 11, -358537222),
        d = y(d, l, c, f, s[h + 3], 16, -722521979),
        f = y(f, d, l, c, s[h + 6], 23, 76029189),
        c = y(c, f, d, l, s[h + 9], 4, -640364487),
        l = y(l, c, f, d, s[h + 12], 11, -421815835),
        d = y(d, l, c, f, s[h + 15], 16, 530742520),
        c = m(c, f = y(f, d, l, c, s[h + 2], 23, -995338651), d, l, s[h + 0], 6, -198630844),
        l = m(l, c, f, d, s[h + 7], 10, 1126891415),
        d = m(d, l, c, f, s[h + 14], 15, -1416354905),
        f = m(f, d, l, c, s[h + 5], 21, -57434055),
        c = m(c, f, d, l, s[h + 12], 6, 1700485571),
        l = m(l, c, f, d, s[h + 3], 10, -1894986606),
        d = m(d, l, c, f, s[h + 10], 15, -1051523),
        f = m(f, d, l, c, s[h + 1], 21, -2054922799),
        c = m(c, f, d, l, s[h + 8], 6, 1873313359),
        l = m(l, c, f, d, s[h + 15], 10, -30611744),
        d = m(d, l, c, f, s[h + 6], 15, -1560198380),
        f = m(f, d, l, c, s[h + 13], 21, 1309151649),
        c = m(c, f, d, l, s[h + 4], 6, -145523070),
        l = m(l, c, f, d, s[h + 11], 10, -1120210379),
        d = m(d, l, c, f, s[h + 2], 15, 718787259),
        f = m(f, d, l, c, s[h + 9], 21, -343485551),
        c = c + g >>> 0,
        f = f + v >>> 0,
        d = d + _ >>> 0,
        l = l + w >>> 0
    }
    return r123.endian([c, f, d, l])
};

_ff = function(e, t, r, n, i, o, a) {
    var s = e + (t & r | ~t & n) + (i >>> 0) + a;
    return (s << o | s >>> 32 - o) + t
}
            ,
_gg = function(e, t, r, n, i, o, a) {
    var s = e + (t & n | r & ~n) + (i >>> 0) + a;
    return (s << o | s >>> 32 - o) + t
}
,
_hh = function(e, t, r, n, i, o, a) {
    var s = e + (t ^ r ^ n) + (i >>> 0) + a;
    return (s << o | s >>> 32 - o) + t
}
,
_ii = function(e, t, r, n, i, o, a) {
    var s = e + (r ^ (t | ~n)) + (i >>> 0) + a;
    return (s << o | s >>> 32 - o) + t
}



exports = function(e, r) {
    if (null == e)
        throw new Error("Illegal argument " + e);
    var n = r123.wordsToBytes(des(e, r));
    return r && r.asBytes ? n : r && r.asString ? o.bytesToString(n) : r123.bytesToHex(n)
}


function main123(t){
    e = "/youzy.dms.basiclib.api.college.query"


    var r, i = "9SASji5OWnG41iRKiSvTJHlXHmRySRp1", o = "", a = t || {}, s = (e = e || "").split("?");

    o = Object.keys(a).length > 0 ? "".concat(JSON.stringify(a), "&").concat(i) : "&".concat(i);


     return exports(o)
}