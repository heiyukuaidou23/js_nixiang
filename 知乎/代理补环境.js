
function proxy(proxy_array){
    for (let i = 0; i < proxy_array.length; i++){
        eval(proxy_array[i] + `= new Proxy(`+proxy_array[i]+ `, {
            get(target, key){
            console.log('【`+ proxy_array[i]+`】 取属性' + key+ ' 值: ' + target[key]);
            console.log("--------->>>>")
            return target[key];
        }
    });`)
    }
}
var proxy_array = ['window', 'navigator','location','history','screen','div','script','CanvasRenderingContext2D','document','alter'];
proxy(proxy_array);