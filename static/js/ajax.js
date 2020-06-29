function like(slug, id){
  token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  card = document.getElementById("card_"+id);
  card.style.display = 'none';

  $.ajax({
    type: 'POST',
    url: '../like/' + id + '/',
    data: {
      csrfmiddlewaretoken: token
    },
    success: function(result) {
      $("#message").text(result.mensagem);
      $("#percentual").text(result.percentual+'%');
      $("#percentual").css("width",result.percentual+'%');
      $("#activist_count").text(result.activist_count);
      $("#theorist_count").text(result.theorist_count);
      $("#reflector_count").text(result.reflector_count);
      $("#pragmatist_count").text(result.pragmatist_count);
    }
  });
}

function dislike(slug, id){
  token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  card = document.getElementById("card_"+id);
  card.style.display = 'none';

  $.ajax({
    type: 'POST',
    url: '../dislike/' + id + '/',
    data: {
      csrfmiddlewaretoken: token
    },
    success: function(result) {
      $("#message").text(result.mensagem);
      $("#percentual").text(result.percentual+'%');
      $("#percentual").css("width",result.percentual+'%');
    }

  });

}
