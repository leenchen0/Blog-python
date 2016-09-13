function init() {
    // content = document.getElementById("content");
    // ctxt_con = content.getContext('2d');
    // process = document.getElementById("process");
    // ctxt_pro = process.getContext('2d');
}

function resize() {
    // ctxt_con.canvas.width  = window.innerWidth*0.87;
    // ctxt_con.canvas.height = ((window.innerHeight-50)*0.98-40);
    // $("#content").css({"height":((window.innerHeight-50)*0.98-40)+'px',"margin-top":(50+(window.innerHeight-50)*0.02)+'px',"width":window.innerWidth*0.87+'px'});
    // ctxt_pro.canvas.width  = window.innerWidth*0.05;
    // ctxt_pro.canvas.height = ((window.innerHeight-50)*0.98-40);
    // $("#process").css({"height":((window.innerHeight-50)*0.98-40)+'px',"margin-top":(50+(window.innerHeight-50)*0.02)+'px',"width":window.innerWidth*0.07+'px'});
    $(".content img").each(function() {
        if ((parseInt($(this).css("width")))>=(parseInt($(".content").css("width"))-20)) {
            $(this).css({"width":(parseInt($(".content").css("width"))-20)+'px',"height":"auto"});
        }
        else {
            $(this).css({"width":"","height":""});
        }
    });
}