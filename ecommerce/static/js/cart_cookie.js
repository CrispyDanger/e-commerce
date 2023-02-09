
function getCookie(name){
    var cookieArr = document.cookie.split(";");

    for (var i = 0; i < cookieArr.length; i++) {
        var cookiePair = cookieArr[i].split("=")

        if (name == cookiePair[0].trim()){
            return decodeURIComponent(cookiePair[1]);
        }
    }

    return null;
}


var user = JSON.parse(getCookie('user'));
console.log('Cart:', user)

if (user == undefined){
    user = cookieValue
    console.log('Cart Created!', user)
    var expireTime = (new Date(Date.now()+ 24*7*60*60*1000)).toUTCString();
    document.cookie = 'user=' + JSON.stringify(cookieValue) +";expires=" + expireTime + ";domain=;path=/"
}
