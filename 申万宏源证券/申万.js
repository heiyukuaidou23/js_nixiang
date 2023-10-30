const crypto1 = require('crypto-js')


function decrypt(t) {
    var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : ""
        , r = "rewin-swhysc1234"
        , i = crypto1.enc.Utf8.parse(r)
        , o = crypto1.AES.decrypt(t, i, {
        mode: crypto1.mode.ECB,
        padding: crypto1.pad.Pkcs7
    });
    return crypto1.enc.Utf8.stringify(o).toString()
}

data = 'K0FWJlJJ7hojwG3yOTA/NshaO9jUNRiTzZsxTWdFMAY/ZG/OkUckgKlcCVSiPWYBNiSuMWsiKbsmtVcou1KRsaZ+s/MvAptvHr3rpl2XkvR2QtO+fzvXqHStIpnDCo1En1DI/XUX3mcdPjmFZqJ5Uo4DfbSsgoIEaCEau2/F8N0toSk+B0u8AvC6vfc1Y3q8QeyxHsNDWlP+VsJi2BIJ/pJlatCsvp6llwZnpMcyJzcvVO34Ims8PfqtOEdBx5POul0zdQd3w+RILJEbgxdWbnZC075/O9eodK0imcMKjUSfUMj9dRfeZx0+OYVmonlSjgN9tKyCggRoIRq7b8Xw3S2hKT4HS7wC8Lq99zVjerxB7LEew0NaU/5WwmLYEgn+Ak7pXhRYZV15ISLVVgwClEHquYIpbmR0d+NpUsFqG+PBd6kdDm03mOXyQM2FlHwGV0VfLZpFDK/juXPfx3Z0oe4n45uK8NEtMrNGqXGVEJYGy37uPGflI7Z9ZWWcBGwm0Vnci+i7chm3iihvbMCTLbyIs/zuZKqgNSBhLJF/yNcEx4zIbj3E2SSc/ERwX7k9ckeDNTCNb1DITmgtyQbEJgNdUHuWm3VNZNLzUvovXxxXRV8tmkUMr+O5c9/HdnSh7ifjm4rw0S0ys0apcZUQlgbLfu48Z+Ujtn1lZZwEbCbS6f1M10pmoFS46ZdADgOQvIiz/O5kqqA1IGEskX/I18aZ6oQY5UYJjIJqfb3CE9e+7X168cTjrR1f/fHidVZrA11Qe5abdU1k0vNS+i9fHFdFXy2aRQyv47lz38d2dKG5Y/G7bYOSwwqLUYagrq5RBst+7jxn5SO2fWVlnARsJtFZ3Ivou3IZt4oob2zAky28iLP87mSqoDUgYSyRf8jXQB1aKUk08iQvHxSlFk1791dju+UYKUenvO949VMH6iTjb5x6WzAh3nAzIViX2Xh6cBjSKZotgJdtuUpQ8dBK964f+KmPa4yqWJN0TeivAVBc12MjI7FtOlHUgLwbDCd67rV9D0OC7Ay317GH7DXrxvN5TIzHbVLVkR6+cHjgOodQXDfz2w3LRwmpnPatZc5z6Rahb8GVE1QLeWJerndRT+1kEL686uxD62J/jDP5+fy3JVsW/wU/uhgD1GqUrpjIG50h/ABFYdm4AJeQVngLYcUSTuxAjT3FNjuxHwHL0GX78SPABxIqZIztHJ2wRYUrkKJwfCsKMMhIhjSvKZrJ22jMn4KN20oPFMtF8WPii+/SNqQbxMTIocbDBF+I7hYuqCWc5c1ldZWel/bLrGO7LwGSPRLToUXpa211KfE+4YRENtGow2ek4juHAkqKQ4oedtwlhdgB+WCryluJ2svPccDaoa6cMGAqq5SmiRa7gc7BgfgI870dC/9m9SB77z0NXGy/clJZicPoeC9v9ggpoEHkI6Ei7jWbuAODdBtbd1GoJZzlzWV1lZ6X9susY7sv7SZl6334jAByvmXjv02AGkQ20ajDZ6TiO4cCSopDih523CWF2AH5YKvKW4nay89xwNqhrpwwYCqrlKaJFruBzr2fMHC0cTP1Goz+2ZbBOacE/2X3l/PsXoYrmovLfWDaOzk4xXR00Lpg3onMJczpLqglnOXNZXWVnpf2y6xjuy/tJmXrffiMAHK+ZeO/TYAaRDbRqMNnpOI7hwJKikOKHnbcJYXYAflgq8pbidrLz3GHO7ykHXHXQ3f85SfRxKGnEHCVcxzeH+cmZ6AJPIQawlxsv3JSWYnD6Hgvb/YIKaA3EIeVNgShR5GQvTZupjAz8McQa8FedGnVc6nVut7GuBAvMPwZN0Vkd00JVEw3/b9ngD4dUIznCuyP3tU+oUl0QrIhdqcRyXdBWmjWSpuxi+21R2lPkQ1pvu8xEXWwJ5w='
console.log(decrypt(data))