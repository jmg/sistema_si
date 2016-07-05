
function showNotification(html, source) {
    html = $(html);
    html.hide();
    if (typeof source!=='undefined' && source) {
        $($(source.closest(".panel-body")).find(".msgs-container")).html(html);
    } else {
        $(".msgs-container.general").html(html);
    }

    $(html).fadeIn();
    setTimeout(function(){
        $(html).fadeOut();
    }, 3000);
}

;(function(d){

    d.alert= function(message, title, source) {
        alertify.set('notifier','position', 'top-right');
        alertify.error(message);
    };

    d.warning= function(message, title, source){
        alertify.set('notifier','position', 'top-right');
        alertify.warning(message);
    };

    d.info= function(message, title, source){
        alertify.set('notifier','position', 'top-right');
        alertify.success(message);
    };

})(jQuery);
