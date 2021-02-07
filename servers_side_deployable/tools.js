function bind_icon_input_focus(p_parent, p_icon_focus, p_input_focus, p_icon_unfocus, p_input_unfocus) {

  $(p_parent).focusin(function() {
    $(this).find('i').removeClass(p_icon_unfocus);
    $(this).find('input').removeClass(p_input_unfocus);
    $(this).find('i').addClass(p_icon_focus);
    $(this).find('input').addClass(p_input_focus);
  });

  $(p_parent).focusout(function() {
    $(this).find('i').removeClass(p_icon_focus);
    $(this).find('input').removeClass(p_input_focus);
    $(this).find('i').addClass(p_icon_unfocus);
    $(this).find('input').addClass(p_input_unfocus);
  });

}
