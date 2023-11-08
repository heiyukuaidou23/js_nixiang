const CryptJS = require('crypto-js')


function main123(timestamp){
    // time = (new Date).getTime()
    des1 = CryptJS.MD5('appId=5053&cityCode=500100&t='+timestamp+'&pageIndex=1&pageSize=12&categoryCode=54&order=0750F82C2-D8F6-49F6-878C-1E7EBEBC8DA2').toString()
    return des1
}