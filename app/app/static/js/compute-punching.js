// Generated by CoffeeScript 1.9.3
(function() {
  var computePunching, main;

  computePunching = function() {
    return $.ajax({
      url: "/api/compute_punching",
      dataType: "json",
      type: "POST",
      data: {
        c_class: $('#id_c_class').val(),
        s_class: $('#id_s_class').val(),
        dsw: $('#id_dsw').val(),
        support: $('#id_support').val(),
        section: $('#id_section').val(),
        b: $('#id_b').val(),
        h: $('#id_h').val(),
        dx: $('#id_dx').val(),
        dy: $('#id_dy').val(),
        lx: $('#id_lx').val(),
        ly: $('#id_ly').val(),
        ad: $('#id_ad').val(),
        lambda_u: $('#id_lambda_u').val(),
        asx: $('#id_asx').val(),
        asy: $('#id_asy').val(),
        design_situation: $('#id_design_situation').val(),
        ved: $('#id_ved').val(),
        beta: $('#id_beta').val(),
        csrfmiddlewaretoken: $.cookie('csrftoken')
      },
      success: function(data, textStatus, jqXHR) {
        var $punchingError, $punchingResults, $vrdc, $vrdmax, error, i, info, j, len, len1, ref, ref1, results;
        $punchingError = $('.js-compute-punching-error');
        $punchingError.html('');
        $punchingResults = $('.js-results');
        $punchingResults.html('');
        $vrdc = $('.js-vrdc');
        $vrdmax = $('.js-vrdmax');
        $vrdc.val('');
        $vrdmax.val('');
        if (data.success === true) {
          ref = data.info;
          for (i = 0, len = ref.length; i < len; i++) {
            info = ref[i];
            $punchingResults.append('<br>' + info);
          }
          $('.form-result2').html('Nośność na przebicie spełniona');
          $vrdc.val(data.vrdc);
          $vrdmax.val(data.vrdmax);
        }
        if (data.success === false) {
          if (data.punching_errors) {
            ref1 = data.punching_errors;
            results = [];
            for (j = 0, len1 = ref1.length; j < len1; j++) {
              error = ref1[j];
              results.push($punchingError.append(error));
            }
            return results;
          }
        }
      },
      error: function(jqXHR, textStatus, errorThrown) {
        return $('.js-compute-punching-error').html("Wystąpił nieoczekiwany błąd o kodzie " + jqXHR.status);
      }
    });
  };

  main = function() {
    return $('.js-compute-punching').click(function(ev) {
      return computePunching();
    });
  };

  $(function() {
    return main();
  });

}).call(this);
