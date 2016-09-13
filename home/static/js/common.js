var ip;
var isp;
var browser;
var os;
var url = 'http://chaxun.1616.net/s.php?type=ip&output=json&callback=?&_='+Math.random(); 
$.getJSON(url, function(data){
    ip = data.Ip;
    isp = data.Isp;
    browser = data.Browser;
    os = data.OS;
});

window.onresize = function() {
    resize();
    $(".menu").css("height",window.innerHeight+'px');
}

window.onload = function() {
    $.get("/view/",{'ip':ip,'isp':isp,'browser':browser,'os':os}, function(){});
    $(".menu").css("height",window.innerHeight+'px');
    init();//initial other js program.
    resize();
    
    $(".menuLine").mouseenter(function() {
        $("#line1").css({"transform":"rotate(15deg)","box-shadow":"0px 0px 3px rgb(158,158,158)"});
        $("#line2").css({"box-shadow":"0px 0px 3px rgb(158,158,158)"});
        $("#line3").css({"transform":"rotate(-15deg)","box-shadow":"0px 0px 3px rgb(158,158,158)"});
    });
    $(".menuLine").mouseleave(function() {
        $("#line1").css({"transform":"rotate(0deg)","box-shadow":""});
        $("#line2").css({"box-shadow":""});
        $("#line3").css({"transform":"rotate(0deg)","box-shadow":""});
    });
    $(".menuLine").click(function() {
        $(".menu").toggleClass("menu-open");
        $(".container").toggleClass("menu-open");
    });

    $(".closeMenu").click(function() {
        $(".menu").toggleClass("menu-open");
        $(".container").toggleClass("menu-open");
    });

    $(".category").click(function() {
        $("#category").toggleClass("fa-sort-desc");
        $("#category").toggleClass("fa-sort-asc");
        $(".category").toggleClass("ul-focus");
        $(".category ul li a").toggleClass("category-open");
    });
}