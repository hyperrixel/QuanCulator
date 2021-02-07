$(function() {

  bind_icon_input_focus('.search-input', 'input-focused-icon', 'input-focused-input', 'input-unfocused-icon', 'input-unfocused-input');

  $('.coin-copy').click(function(){
    var address_temp = $('<input>');
    $('body').append(address_temp);
    address_temp.val($(this).find('.coin-addr').text()).select();
    document.execCommand("copy");
  });

  $('#q-click').click(function(){
    $('#q-result').html('');
    if ($('#q-url').val() !== '') {
      $.ajax({ type: 'POST',
               url: 'quanculator.php',
               dataType: 'json',
               data: { q_url: $('#q-url').val() },
               success: function(response){
                 if (response.error == 0) {
                   var q_sum = response.explicit + response.hidden + response.broken + response.spill;
                   if (q_sum == 0) {
                     $('#q-result').html('The page is quantum clear.');
                   } else {
                     var result_text = 'The page contains <span>' + q_sum + '</span> total quantum(s); '
                     result_text += '<span>' + response.explicit + '</span> explicit quantum(s), '
                     result_text += '<span>' + response.hidden + '</span> hidden quantum(s), '
                     result_text += '<span>' + response.broken + '</span> broken quantum(s) '
                     result_text += 'and <span>' + response.spill + '</span> quantum spill(s).'
                     $('#q-result').html(result_text);
                   }
                 } else if (response.error == 1) {
                   $('#q-result').html('Empty query were sent. This should be an internal error. Maybe try another browser.');
                 } else if (response.error == 2) {
                   $('#q-result').html('The text you gave seems to be not a valid URL, sorry. Please try again.');
                 } else if (response.error == 3) {
                   $('#q-result').html('The URL you gave seems not to be good or there is some error on their side.');
                 } else {
                   $('#q-result').html('Thos should not happen. If still happen, quantums are definitely not your friends.');
                 }
               }});
    }
  });

});
