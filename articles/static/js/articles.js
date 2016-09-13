function init() {
    // $(".spread").click(function() {
    //     if ($("#detail"+$(this).attr('id')).css("display")=="none") {
    //         $("#detail"+$(this).attr('id')).css("display","block");
    //         $(this).html('-');
    //     } else{
    //         $("#detail"+$(this).attr('id')).css("display","none");
    //         $(this).html('+');
    //     }; 
    // });

    // var tags_a = $("#tags a");
    // tags_a.each(function(){
    //     var fzmax = 24;
    //     var fzmin = 14;
    //     var fz = parseInt(Math.random() * (fzmax - fzmin + 1) + fzmin);
    //     var r = parseInt(Math.random() * 254);
    //     var g = parseInt(Math.random() * 254);
    //     var b = parseInt(Math.random() * 254);
    //     var clor = "rgb("+r+","+g+","+b+")";
    //     if (parseInt(Math.random()*9)>5) {
    //         var fw = "bold";
    //     } else{ var fw = "normal"};
    //     $(this).css({"font-size":fz+"px","color":clor,"font-weight":fw});
    // });
}

function resize() {
    $("img").each(function() {
        if ($(this).attr("width")>(parseInt($(".content").css("width"))-20)) {
                $(this).css({"width":(parseInt($(".content").css("width"))-20)+'px',"height":"auto"});
        }
        else {
            $(this).css({"width":"","height":""});
        }
    })
    $(".main").css({"margin-top":(50+(window.innerHeight-50)*0.02)+'px',"min-height":(window.innerHeight-50)*0.96+'px'});
    $(".articles").css("min-height",(window.innerHeight-50)*0.9+'px');
    $(".sort").css({"min-height":(window.innerHeight-50)*0.45+'px'});
    $(".tag").css({"min-height":(window.innerHeight-50)*0.45-20+'px'});
    $(".copyright").css("top",(parseInt($(".main").css("height"))+50+18)+'px');
}
