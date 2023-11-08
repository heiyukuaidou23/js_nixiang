
const CryptoJS = require('crypto-js')

tu = function e(t) {
    var n;
    if (Array.isArray(t)) {
        for (var r in n = new Array,
        t) {
            var o = t[r];
            for (var i in o)
                null == o[i] ? delete t[r][i] : Array.isArray(t[r][i]) && e(t[r][i])
        }
        return n = t,
        JSON.stringify(n).replace(/^(\s|")+|(\s|")+$/g, "")
    }
    return n = t && t.constructor === Object ? JSON.stringify(t) : t
}

nu = function(e) {
    var t = new Array
      , n = 0;
    for (var i in e)
        t[n] = i,
        n++;
    return t.sort()
}


Jc = function(e, t, time) {
    var n = t + e + time;
    return n =CryptoJS.MD5(n).toString()
}

eu = function(e) {
    var t = nu(e)
      , n = "";
    for (var i in t) {
        var r = tu(e[t[i]]);
        null != r && "" != r.toString() && (n += t[i] + "=" + r + "&")
    }
    return n
}

// param = {
//     "eid": "",
//     "achievementQueryType": "and",
//     "achievementQueryDto": [],
//     "personnelQueryDto": {
//         "queryType": "and"
//     },
//     "aptitudeQueryDto": {
//         "queryType": "and",
//         "nameStr": "",
//         "aptitudeQueryType": "and",
//         "businessScopeQueryType": "or",
//         "filePlaceType": "1",
//         "aptitudeDtoList": [
//             {
//                 "codeStr": "",
//                 "queryType": "and",
//                 "aptitudeType": "qualification"
//             }
//         ],
//         "aptitudeSource": "new"
//     },
//     "page": {
//         "page": 4,
//         "limit": 20,
//         "field": "",
//         "order": ""
//     }
// }
//
// time = (new Date).getTime();
//
//
// var sign = (param, time, t = eu(param),
//     Jc("ghaepVf6IhcHmgnk4NCTXLApxQkBcvh1", Jc("mwMlWOdyM7OXbjzQPulT1ndRZIAjShDB", Jc("ZuSj0gwgsKXP4fTEz55oAG2q2p1SVGKK", t, time), time), time))
// console.log(sign)


function generateSign(param) {
    const time = new Date().getTime();
    const t = eu(param);
    const sign = Jc(
        "ghaepVf6IhcHmgnk4NCTXLApxQkBcvh1",
        Jc(
            "mwMlWOdyM7OXbjzQPulT1ndRZIAjShDB",
            Jc(
                "ZuSj0gwgsKXP4fTEz55oAG2q2p1SVGKK",
                t,
                time
            ),
            time
        ),
        time
    );
    console.log("页码:");
    return sign;
}


// const sign = generateSign(param);
console.log(generateSign());
module.exports = generateSign;



