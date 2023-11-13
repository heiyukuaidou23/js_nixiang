

const CryptoJS = require('crypto-js')
ts = (new Date).getTime()
e = {
    "ts": ts,
    "pageNo": 4,
    "pageSize": 20,
    "total": 4545,
    "AREACODE": "",
    "M_PROJECT_TYPE": "",
    "KIND": "GCJS",
    "GGTYPE": "1",
    "PROTYPE": "",
    "timeType": "6",
    "BeginTime": "2023-05-12 00:00:00",
    "EndTime": "2023-11-12 23:59:59",
    "createTime": []
}

r = {
    "h": "福建省公共资源交易电子公共服务平台",
    "g": "福建省公共资源交易公共服务平台有限公司",
    "b": [
        "主办单位：福建省经济信息中心",
        "闽ICP备10207592号-4",
        "网站标识码：3500000080"
    ],
    "f": [
        {
            "type": "1",
            "value": "",
            "children": [
                {
                    "ADDRESS": "",
                    "TITLE": "国务院部门网站"
                }
            ]
        },
        {
            "value": "",
            "type": "6",
            "children": [
                {
                    "ADDRESS": "",
                    "TITLE": "省直厅局单位"
                }
            ]
        },
        {
            "value": "",
            "type": "3",
            "children": [
                {
                    "ADDRESS": "",
                    "TITLE": "各地市公共资源交易中心"
                }
            ]
        },
        {
            "value": "",
            "type": "4",
            "children": [
                {
                    "ADDRESS": "",
                    "TITLE": "其他网站"
                }
            ]
        }
    ],
    "d": [
        {
            "name": "联系我们",
            "link": "/contact"
        }
    ],
    "e": "EB444973714E4A40876CE66BE45D5930",
    "i": "B5A8904209931867",
    "a": "B3978D054A72A7002063637CCDF6B2E5",
    "c": [
        {
            "title": "福建省数字安全证书管理有限公司",
            "img": "data:image/png;base64,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",
            "btn3": [
                "/img/CA产品图正面1.fa938f55.jpg",
                "/img/CA产品图反面1（320X80）.18bf735e.png",
                "/img/CA产品图正面2（320X80）.fabb422b.jpg",
                "/img/CA产品图反面2（320X80）.6c8f0a85.png"
            ],
            "btn2": {
                "title": "福建CA客户端微信客服",
                "url": "/img/qrcode.5951c1e2.jpg"
            },
            "btn1": "https://ggzyfw.fujian.gov.cn/Website/Packages/福建CA.rar",
            "btn6": "https://ggzyjd.fj.gov.cn/npm/CA/福建CA.pdf",
            "kfTel": "0591-87760022",
            "area": "省级、福州、平潭、泉州、龙岩、莆田、漳州、三明、南平"
        },
        {
            "title": "北京天威诚信电子商务服务有限公司",
            "img": "data:image/png;base64,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",
            "btn3": [
                "/img/福建CA-反面.55183f26.png",
                "/img/福建CA-正面.fefed477.png",
                "/img/天威-反面.b61d8b09.png",
                "/img/天威-正面.32242868.png"
            ],
            "btn1": "https://ggzyfw.fujian.gov.cn/Website/Packages/天威诚信.rar",
            "btn6": "https://ggzyjd.fj.gov.cn/npm/CA/天威诚信.pdf",
            "kfTel": "4009996901（厦门）、4009029660（宁德）",
            "area": "厦门、宁德"
        },
        {
            "title": "中金金融认证中心有限公司",
            "img": "/img/CFCA.35087a1a.jpg",
            "btn3": [
                "/img/CFCA1-1_320x80.f1dc9625.png",
                "/img/CFCA1-2_320x80.33d4dad0.jpg",
                "/img/CFCA2-1_320x80.9e10a6cf.png",
                "/img/CFCA2-2_320x80.28e38c0e.png",
                "/img/产品海迈CA.a3e897e7.jpg",
                "/img/海迈1-1_320x80.a6dd51e5.png",
                "/img/海迈1-2_320x80.89f5453b.png",
                "/img/海迈2-1_320x80.ac85d066.png",
                "/img/海迈2-2_320x80.f1dc9625.png"
            ],
            "btn1": "https://ggzyfw.fujian.gov.cn/Website/Packages/CFCA.rar",
            "btn6": "https://ggzyjd.fj.gov.cn/npm/CA/CFCA.pdf",
            "btn4": "https://ggzyfw.fujian.gov.cn/Website/CA/images/ca/%E5%87%AF%E7%89%B9%E5%9B%BE%E7%89%87/%E6%93%8D%E4%BD%9C%E6%89%8B%E5%86%8C/%E5%85%AC%E5%85%B1%E8%B5%84%E6%BA%90%E4%BA%A4%E6%98%93%E4%B8%AD%E5%BF%83%E7%BB%9F%E4%B8%80ca%E6%93%8D%E4%BD%9C%E6%89%8B%E5%86%8C%EF%BC%88CFCA%EF%BC%89.docx",
            "kfTel": "7*24小时客服电话：400-616-9958（全省工程招投标与政府采购适用）<p>原海易招、邵武、武夷山（仅工程招投标类使用）客服：0599-6220685（工作日8:30-17:30）</p>"
        },
        {
            "title": "深圳市电子商务安全证书管理有限公司",
            "img": "/img/szca.89450cd0.png",
            "btn3": [
                "/img/SZCA产品图正面.51451249.jpg",
                "/img/SZCA产品图正面.51451249.jpg"
            ],
            "btn5": "https://kefu.easemob.com/webim/im.html?configId=3e6ce8ec-bc9f-4d83-810d-e8ff5c52a7b3",
            "btn1": "https://ggzyfw.fujian.gov.cn/Website/Packages/深圳CA.rar",
            "btn6": "https://ggzyjd.fj.gov.cn/npm/CA/深圳CA.pdf",
            "kfTel": "400-112-3838  /  0755-26588388  ",
            "area": "随行交易系统"
        }
    ],
    "j": [
        {
            "id": "1",
            "title": "福建晨曦信息科技集团股份有限公司",
            "img": "/img/u57.5e08e93f.png",
            "btn": "",
            "tel": ""
        },
        {
            "id": "6",
            "title": "福建省五星信息科技有限公司",
            "img": "/img/u84.149ed99a.png",
            "btn": "",
            "tel": ""
        },
        {
            "id": "5",
            "title": "厦门海迈科技股份有限公司",
            "img": "/img/u77.63f9d325.png",
            "btn": "",
            "tel": ""
        },
        {
            "id": "2",
            "title": "漳州大盛软件有限公司",
            "img": "/img/u91.59c235ac.png",
            "btn": "",
            "tel": ""
        },
        {
            "id": "3",
            "title": "广联达软件股份有限公司",
            "img": "/img/u70.abf4468d.png",
            "btn": "",
            "tel": ""
        },
        {
            "id": "4",
            "title": "国泰新点软件股份有限公司",
            "img": "/img/u100.ef546c93.png",
            "btn": "",
            "tel": ""
        },
        {
            "id": "7",
            "title": "深圳市斯维尔科技股份有限公司",
            "img": "/img/u11.dc8bbbdb.png",
            "btn": "",
            "tel": ""
        }
    ]
}
function s(t, e) {
    return t.toString().toUpperCase() > e.toString().toUpperCase() ? 1 : t.toString().toUpperCase() == e.toString().toUpperCase() ? 0 : -1
}
function l(t) {
    for (var e = Object.keys(t).sort(s), n = "", a = 0; a < e.length; a++)
        if (void 0 !== t[e[a]])
            if (t[e[a]] && t[e[a]]instanceof Object || t[e[a]]instanceof Array) {
                var i = JSON.stringify(t[e[a]]);
                n += e[a] + i
            } else
                n += e[a] + t[e[a]];
    return n
}
function d(t) {
    for (var e in t)
        "" !== t[e] && void 0 !== t[e] || delete t[e];
    var n = r["a"] + l(t);
    return CryptoJS.MD5(n).toString().toLocaleLowerCase()
}

console.log(d(e))