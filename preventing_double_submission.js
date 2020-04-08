(function($){
    $(document).ready(function() {
      $("#id-submit-button").click(function() {
        var $form = $(this);
        if ($form.data('submitted') === true) {
        $(this).attr("disabled", true);
        } else {
          console.log('submitted!');
        }
        $form.data('submitted', true);
      });
    });
  })(jQuery);
  