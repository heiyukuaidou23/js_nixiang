


function main(F, t, B) {
    var d, b, e, y, k, v, w, c, g;
    function s(i, t, e, s) {
        this.e = p(i),
        this.d = p(t),
        this.m = p(e),
        this.chunkSize = "number" != typeof s ? 2 * _(this.m) : s / 8,
        this.radix = 16,
        this.barrett = new o(this.m)
    }
    function n(t, e, s, n) {
        var o, r, a, c, d, g, p, u = new Array, h = e.length, l = "", f = "string" == typeof s ? s == M.NoPadding ? 1 : s == M.PKCS1Padding ? 2 : 0 : 0, m = "string" == typeof n && n == M.RawEncoding ? 1 : 0;
        for (1 == f ? h > t.chunkSize && (h = t.chunkSize) : 2 == f && h > t.chunkSize - 11 && (h = t.chunkSize - 11),
        o = 0,
        r = 2 == f ? h - 1 : t.chunkSize - 1; o < h; )
            f ? u[r] = e.charCodeAt(o) : u[o] = e.charCodeAt(o),
            o++,
            r--;
        for (1 == f && (o = 0),
        r = t.chunkSize - h % t.chunkSize; 0 < r; ) {
            if (2 == f) {
                for (c = Math.floor(256 * Math.random()); !c; )
                    c = Math.floor(256 * Math.random());
                u[o] = c
            } else
                u[o] = 0;
            o++,
            r--
        }
        for (2 == f && (u[h] = 0,
        u[t.chunkSize - 2] = 2,
        u[t.chunkSize - 1] = 0),
        d = u.length,
        o = 0; o < d; o += t.chunkSize) {
            for (g = new S,
            r = 0,
            a = o; a < o + t.chunkSize; ++r)
                g.digits[r] = u[a++],
                g.digits[r] += u[a++] << 8;
            p = t.barrett.powMod(g, t.e),
            l += 1 == m ? function(i) {
                for (var t = "", e = _(i); -1 < e; --e)
                    t += function(i) {
                        var t = String.fromCharCode(255 & i);
                        return i >>>= 8,
                        String.fromCharCode(255 & i) + t
                    }(i.digits[e]);
                return t
            }(p) : 16 == t.radix ? function(t) {
                for (var e = "", s = (_(t),
                _(t)); -1 < s; --s)
                    e += function(t) {
                        var e = "";
                        for (i = 0; i < 4; ++i)
                            e += w[15 & t],
                            t >>>= 4;
                        return T(e)
                    }(t.digits[s]);
                return e
            }(p) : function(i, t) {
                var e = new S
                  , s = (e.digits[0] = t,
                z(i, e))
                  , n = v[s[1].digits[0]];
                for (; 1 == E(s[0], y); )
                    s = z(s[0], e),
                    digit = s[1].digits[0],
                    n += v[s[1].digits[0]];
                return (i.isNeg ? "-" : "") + T(n)
            }(p, t.radix)
        }
        return l
    }
    function o(i) {
        this.modulus = $(i),
        this.k = _(this.modulus) + 1;
        var t, i = new S;
        i.digits[2 * this.k] = 1,
        this.mu = (t = this.modulus,
        z(i, t)[0]),
        this.bkplus1 = new S,
        this.bkplus1.digits[this.k + 1] = 1,
        this.modulo = r,
        this.multiplyMod = a,
        this.powMod = U
    }
    function r(i) {
        for (var t = l(i, this.k - 1), t = l(u(t, this.mu), this.k + 1), e = N(f(i, this.k + 1), f(u(t, this.modulus), this.k + 1)), s = 0 <= E(e = e.isNeg ? A(e, this.bkplus1) : e, this.modulus); s; )
            s = 0 <= E(e = N(e, this.modulus), this.modulus);
        return e
    }
    function a(i, t) {
        i = u(i, t);
        return this.modulo(i)
    }
    function U(i, t) {
        var e, s, n = new S;
        for (n.digits[0] = 1,
        e = i,
        s = t; 0 != (1 & s.digits[0]) && (n = this.multiplyMod(n, e)),
        0 != (s = x(s, 1)).digits[0] || 0 != _(s); )
            e = this.multiplyMod(e, e);
        return n
    }
    function S(i) {
        this.digits = "boolean" == typeof i && 1 == i ? null : e.slice(0),
        this.isNeg = !1
    }
    function $(i) {
        var t = new S(!0);
        return t.digits = i.digits.slice(0),
        t.isNeg = i.isNeg,
        t
    }
    function O(i) {
        var t, e = new S;
        for (e.isNeg = i < 0,
        i = Math.abs(i),
        t = 0; 0 < i; )
            e.digits[t++] = i & K,
            i >>= d;
        return e
    }
    function T(i) {
        for (var t = "", e = i.length - 1; -1 < e; --e)
            t += i.charAt(e);
        return t
    }
    function Q(i) {
        i = 48 <= i && i <= 57 ? i - 48 : 65 <= i && i <= 90 ? 10 + i - 65 : 97 <= i && i <= 122 ? 10 + i - 97 : 0;
        return i
    }
    function p(i) {
        for (var t = new S, e = i.length, s = 0; 0 < e; e -= 4,
        ++s)
            t.digits[s] = function(i) {
                for (var t = 0, e = Math.min(i.length, 4), s = 0; s < e; ++s)
                    t = (t <<= 4) | Q(i.charCodeAt(s));
                return t
            }(i.substr(Math.max(e - 4, 0), Math.min(e, 4)));
        return t
    }
    function A(i, t) {
        var e, s, n, o;
        if (i.isNeg != t.isNeg)
            t.isNeg = !t.isNeg,
            e = N(i, t),
            t.isNeg = !t.isNeg;
        else {
            for (e = new S,
            o = s = 0; o < i.digits.length; ++o)
                n = i.digits[o] + t.digits[o] + s,
                e.digits[o] = 65535 & n,
                s = Number(b <= n);
            e.isNeg = i.isNeg
        }
        return e
    }
    function N(i, t) {
        var e, s, n, o;
        if (i.isNeg != t.isNeg)
            t.isNeg = !t.isNeg,
            e = A(i, t),
            t.isNeg = !t.isNeg;
        else {
            for (e = new S,
            o = n = 0; o < i.digits.length; ++o)
                s = i.digits[o] - t.digits[o] + n,
                e.digits[o] = 65535 & s,
                e.digits[o] < 0 && (e.digits[o] += b),
                n = 0 - Number(s < 0);
            if (-1 == n) {
                for (o = n = 0; o < i.digits.length; ++o)
                    s = 0 - e.digits[o] + n,
                    e.digits[o] = 65535 & s,
                    e.digits[o] < 0 && (e.digits[o] += b),
                    n = 0 - Number(s < 0);
                e.isNeg = !i.isNeg
            } else
                e.isNeg = i.isNeg
        }
        return e
    }
    function _(i) {
        for (var t = i.digits.length - 1; 0 < t && 0 == i.digits[t]; )
            --t;
        return t
    }
    function X(i) {
        for (var t = _(i), e = i.digits[t], s = (t + 1) * D, n = s; s - D < n && 0 == (32768 & e); --n)
            e <<= 1;
        return n
    }
    function u(i, t) {
        for (var e, s, n, o = new S, r = _(i), a = _(t), c = 0; c <= a; ++c) {
            for (n = c,
            j = e = 0; j <= r; ++j,
            ++n)
                s = o.digits[n] + i.digits[j] * t.digits[c] + e,
                o.digits[n] = s & K,
                e = s >>> d;
            o.digits[c + r + 1] = e
        }
        return o.isNeg = i.isNeg != t.isNeg,
        o
    }
    function I(i, t) {
        var e, s, n, o;
        for (result = new S,
        e = _(i),
        o = s = 0; o <= e; ++o)
            n = result.digits[o] + i.digits[o] * t + s,
            result.digits[o] = n & K,
            s = n >>> d;
        return result.digits[1 + e] = s,
        result
    }
    function h(i, t, e, s, n) {
        for (var o = Math.min(t + n, i.length), r = t, a = s; r < o; ++r,
        ++a)
            e[a] = i[r]
    }
    function C(i, t) {
        var e, s, n, o, r = Math.floor(t / D), a = new S;
        for (h(i.digits, 0, a.digits, r, a.digits.length - r),
        s = D - (e = t % D),
        o = (n = a.digits.length - 1) - 1; 0 < n; --n,
        --o)
            a.digits[n] = a.digits[n] << e & K | (a.digits[o] & c[e]) >>> s;
        return a.digits[0] = a.digits[n] << e & K,
        a.isNeg = i.isNeg,
        a
    }
    function x(i, t) {
        var e, s, n, o, r = Math.floor(t / D), a = new S;
        for (h(i.digits, r, a.digits, 0, i.digits.length - r),
        s = D - (e = t % D),
        o = (n = 0) + 1; n < a.digits.length - 1; ++n,
        ++o)
            a.digits[n] = a.digits[n] >>> e | (a.digits[o] & g[e]) << s;
        return a.digits[a.digits.length - 1] >>>= e,
        a.isNeg = i.isNeg,
        a
    }
    function P(i, t) {
        var e = new S;
        return h(i.digits, 0, e.digits, t, e.digits.length - t),
        e
    }
    function l(i, t) {
        var e = new S;
        return h(i.digits, t, e.digits, 0, e.digits.length - t),
        e
    }
    function f(i, t) {
        var e = new S;
        return h(i.digits, 0, e.digits, 0, t),
        e
    }
    function E(i, t) {
        if (i.isNeg != t.isNeg)
            return 1 - 2 * Number(i.isNeg);
        for (var e = i.digits.length - 1; 0 <= e; --e)
            if (i.digits[e] != t.digits[e])
                return i.isNeg ? 1 - 2 * Number(i.digits[e] > t.digits[e]) : 1 - 2 * Number(i.digits[e] < t.digits[e]);
        return 0
    }
    function z(i, t) {
        var e, s, n, o, r, a, c, d, g, p, u, h, l, f, m = X(i), y = X(t), v = t.isNeg;
        if (m < y)
            i.isNeg ? ((e = $(k)).isNeg = !t.isNeg,
            i.isNeg = !1,
            t.isNeg = !1,
            s = N(t, i),
            i.isNeg = !0,
            t.isNeg = v) : (e = new S,
            s = $(i));
        else {
            for (e = new S,
            s = i,
            n = Math.ceil(y / D) - 1,
            o = 0; t.digits[n] < L; )
                t = C(t, 1),
                ++o,
                ++y,
                n = Math.ceil(y / D) - 1;
            for (s = C(s, o),
            m += o,
            a = P(t, (r = Math.ceil(m / D) - 1) - n); -1 != E(s, a); )
                ++e.digits[r - n],
                s = N(s, a);
            for (c = r; n < c; --c) {
                for (d = c >= s.digits.length ? 0 : s.digits[c],
                g = c - 1 >= s.digits.length ? 0 : s.digits[c - 1],
                p = c - 2 >= s.digits.length ? 0 : s.digits[c - 2],
                u = n >= t.digits.length ? 0 : t.digits[n],
                h = n - 1 >= t.digits.length ? 0 : t.digits[n - 1],
                e.digits[c - n - 1] = d == u ? K : Math.floor((d * b + g) / u),
                l = e.digits[c - n - 1] * (u * b + h),
                f = d * q + (g * b + p); f < l; )
                    --e.digits[c - n - 1],
                    l = e.digits[c - n - 1] * (u * b | h),
                    f = d * b * b + (g * b + p);
                (s = N(s, I(a = P(t, c - n - 1), e.digits[c - n - 1]))).isNeg && (s = A(s, a),
                --e.digits[c - n - 1])
            }
            s = x(s, o),
            e.isNeg = i.isNeg != v,
            i.isNeg && (e = (v ? A : N)(e, k),
            s = N(t = x(t, o), s)),
            0 == s.digits[0] && 0 == _(s) && (s.isNeg = !1)
        }
        return new Array(e,s)
    }
    var M = {
        NoPadding: "NoPadding",
        PKCS1Padding: "PKCS1Padding",
        RawEncoding: "RawEncoding",
        NumericEncoding: "NumericEncoding"
    }
      , D = d = 16
      , L = (b = 65536) >>> 1
      , q = b * b
      , K = b - 1
      , R = 130;
    e = new Array(R);
    for (var m = 0; m < e.length; m++)
        e[m] = 0;
    y = new S,
    (k = new S).digits[0] = 1,
    O(1e15),
    v = new Array("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),
    w = new Array("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"),
    c = new Array(0,32768,49152,57344,61440,63488,64512,65024,65280,65408,65472,65504,65520,65528,65532,65534,65535),
    g = new Array(0,1,3,7,15,31,63,127,255,511,1023,2047,4095,8191,16383,32767,65535),
    t.exports = function(i, t, e) {
        return n(new s(i,"",t), encodeURIComponent(e))
    }
}



RSA_e = "10001"
RSA_m = "a69ae1dd84777e7d40626a29a76f74c176806bb71ce120b259848a730664340bfa550d6fb807b4fe7a2e2a89478ca2f3ea56793440c70b7f3c2017add92e8661924adbda06bff326828ebdc8bef6d094118d64da2eec815812fb70f16aafc73229aa1734727d0a4df65f1c1a2a61946d00a37376822cb30b87127e15f82d68d1"
pwd = "123456"
pwd = main(RSA_e, RSA_m, pwd)
console.log(pwd);