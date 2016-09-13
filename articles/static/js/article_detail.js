var editor;
function init() {
    // uParse('.content', {
    //     rootPath: '/static/ueditor/',
    // });
    // Timer = setInterval(function() {
    //     if ($("tbody").length>0) {
    //         $("<col style=\"width: 38px\" /><col style=\"width: auto\" />").insertBefore($("tbody"));
    //         clearInterval(Timer);
    //     };
    // },100);
    var tool;
    if (window.innerWidth<800) {
        tool = ['color', 'ol', 'ul', 'blockquote', 'hr']
    } else{
        tool = ['title', 'bold', 'italic', 'underline', 'strikethrough', 'fontScale', 'color', 'ol', 'ul', 'blockquote', 'code', 'table', 'link', 'hr', 'indent', 'outdent', 'alignment']
    };
    editor = new Simditor({
      textarea: $('#editor'),
      toolbar:  tool,
    });

    $("#look_comment").click(function() {
        ScrollToControl('position_comment');
    });
    $(".reply").click(function() {
        $("#reply_btn").css("display", "inline-block");
        $("#reply_btn").html("取消回复");
        $("#rid").attr("value", $(this).attr("id"));
        ScrollToControl('position_reply');
    });
    $("#reply_btn").click(function() {
        $(this).css("display", "none");
        $("#rid").attr("value", "-1");
    });
    $(".com_met").click(function() {
        tmp = parseInt($(this).attr("value"));
        if (tmp == 0) {
            $(".visitor").css("display", "none");
            $(".login").css("display", "block");
        } else{
            $(".login").css("display", "none");
            $(".visitor").css("display", "block");
        };
    });

    $("#ip").attr('value', ip);
    $("#isp").attr('value', isp);
    $("#browser").attr('value', browser);
    $("#os").attr('value', os);
}

function sync_content() {
    $("#editor").attr('value', editor.getValue());
    return true;
}

function wechatlogin() {
    alert("暂不支持微信登录~");
    return false;
}

function resize() {
    $(".content img").each(function() {
        if ((parseInt($(this).css("width")))>=(parseInt($(".content").css("width"))-20)) {
            $(this).css({"width":(parseInt($(".content").css("width"))-20)+'px',"height":"auto"});
        }
        else {
            $(this).css({"width":"","height":""});
        }
    });
}

var wzt = encodeURIComponent(document.title);
var wztb = escape(document.title);
var wzu = encodeURIComponent(location.href);
var wzub = escape(location.href);
var title = document.title;
var sc = location.href;

function getSocialLink(s){
    switch(s){
        case "qq":
            return "http://connect.qq.com/widget/shareqq/index.html?url="+wzu+"&title="+wzt+"&site=Pencil's Blog";
        case "renren":
            return "http://share.renren.com/share/buttonshare.do?link="+wzu+"&title="+wzt;
        case "kaixin001":
            return "http://www.kaixin001.com/repaste/share.php?rurl="+wzu+"&rcontent="+wzu+"&rtitle="+wzt;
        case "qzone":
            return "http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url="+wzu+"&title="+wzt;
        case "douban":
            return "http://www.douban.com/recommend/?url="+wzu+"&title="+wzt;
        case "sina-weibo":
            return "http://v.t.sina.com.cn/share/share.php?appkey=2233047537&ralateUid=1883113397&url="+wzu+"&title="+wzt;
        case "qq-weibo":
            return "http://v.t.qq.com/share/share.php?appkey=a8eb5c5b39804bac8ef40d2babb55572&title="+wzt+'&url='+wzu;
        case "sohu-weibo":
            return "http://t.sohu.com/third/post.jsp?&url="+wzu+"&title="+wztb;
        case "delicious":
            return "http://www.delicious.com/save?v=5&noui&jump=close&url="+wzu+'&title='+title;
        case "digg":
            return "http://digg.com/submit?url="+wzu+'&title='+title;
        case "google+":
            return "https://plus.google.com/share?url="+wzu;
    }
}


// ScrollSmoothly
function elementPosition(obj) {
    var curleft = 0, curtop = 0;
    if (obj.offsetParent) {
        curleft = obj.offsetLeft;
        curtop = obj.offsetTop;
        while (obj = obj.offsetParent) {
            curleft += obj.offsetLeft;
            curtop += obj.offsetTop;
        }
    }
    return { x: curleft, y: curtop };
}
function ScrollToControl(id) {
    var elem = document.getElementById(id);
    var scrollPos = elementPosition(elem).y;
    scrollPos = scrollPos - document.documentElement.scrollTop;
    var remainder = scrollPos % 50;
    var repeatTimes = (scrollPos - remainder) / 50;
    ScrollSmoothly(scrollPos,repeatTimes);
    window.scrollBy(0,remainder);
}
var repeatCount = 0;
var cTimeout;
var timeoutIntervals = new Array();
var timeoutIntervalSpeed;
function ScrollSmoothly(scrollPos,repeatTimes) {
    if(repeatCount < repeatTimes) {
        window.scrollBy(0,50);
    } else {
        repeatCount = 0;
        clearTimeout(cTimeout);
        return;
    }
    repeatCount++;
    cTimeout = setTimeout("ScrollSmoothly('"+scrollPos+"','"+repeatTimes+"')",10);
}
// ScrollSmoothly end