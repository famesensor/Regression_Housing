$(document).ready( function() {
  // Example starter JavaScript for disabling form submissions if there are invalid fields
    (function() {
      'use strict';
      window.addEventListener('load', function() {
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function(form) {
          form.addEventListener('submit', function(event) {
            if (form.checkValidity() === false) {
              event.preventDefault();
              event.stopPropagation();
            }
            form.classList.add('was-validated');
          }, false);
        });
      }, false);
    })();

    var myInputs = document.querySelectorAll('.fixed');
    myInputs.forEach(function(elem) {
      elem.addEventListener("input", function() {
        var dec = elem.getAttribute('decimals');
        var regex = new RegExp("(\\.\\d{" + dec + "})\\d+", "g");
        elem.value = elem.value.replace(regex, '$1');
      });
    });
});

