$(document).ready(function() {
  document.getElementById('pro-image').addEventListener('change', readImage, false);

  $( ".preview-images-zone" ).sortable();

  $(document).on('click', '.image-cancel', function() {
      let no = $(this).data('no');
      $(".preview-image.preview-show-"+no).remove();
  });
});


var num = 0;
function readImage() {
  if (window.File && window.FileList && window.FileReader) {
      var files = event.target.files; //FileList object
      var output = $(".preview-images-zone");

      for (let i = 0; i < files.length; i++) {
          var file = files[i];
          var checkdiv = $('div.preview-image').length;
         // lemit line
          if (num <= 5 || checkdiv <= 5){

            var num = checkdiv;
            if (!file.type.match('image')) continue;

            var picReader = new FileReader();

            picReader.addEventListener('load', function (event) {
                var picFile = event.target;
                var html =  '<div class="preview-image preview-show-' + num + '">' +
                            '<div class="image-cancel" data-no="' + num + '">x</div>' +
                            '<div class="image-zone"><img id="pro-img-' + num + '" src="' + picFile.result + '"></div>' +
                            '<div class="tools-edit-image"><a href="javascript:void(0)" data-no="' + num + '" class="btn btn-light btn-edit-image">edit</a></div>' +
                            '</div>';

                output.append(html);
                num = num + 1;
            });
        }
          picReader.readAsDataURL(file);
      }
      $("#pro-image").val('');
  } else {
      console.log('Browser not support');
  }
}




$(document).ready(function() {
  document.getElementById('pro-images').addEventListener('change', readImage, false);

  $( ".preview-images-zones" ).sortable();

  $(document).on('click', '.image-cancel', function() {
      let no = $(this).data('no');
      $(".preview-image.preview-show-"+no).remove();
  });
});


var num = 0;
function readImage() {
  if (window.File && window.FileList && window.FileReader) {
      var files = event.target.files; //FileList object
      var output = $(".preview-images-zones");

      for (let i = 0; i < files.length; i++) {
          var file = files[i];
          var checkdiv = $('div.preview-image').length;
         // lemit line
          if (num <= 5 || checkdiv <= 5){

            var num = checkdiv;
            if (!file.type.match('image')) continue;

            var picReader = new FileReader();

            picReader.addEventListener('load', function (event) {
                var picFile = event.target;
                var html =  '<div class="preview-image preview-show-' + num + '">' +
                            '<div class="image-cancel" data-no="' + num + '">x</div>' +
                            '<div class="image-zone"><img id="pro-img-' + num + '" src="' + picFile.result + '"></div>' +
                            '<div class="tools-edit-image"><a href="javascript:void(0)" data-no="' + num + '" class="btn btn-light btn-edit-image">edit</a></div>' +
                            '</div>';

                output.append(html);
                num = num + 1;
            });
        }
          picReader.readAsDataURL(file);
      }
      $("#pro-images").val('');
  } else {
      console.log('Browser not support');
  }
}




