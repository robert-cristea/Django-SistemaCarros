


function changeLanguage() {
 console.log("todo ok");
  var lang = $('html').attr('lang');
  if(lang == 'en') $('html').attr('lang','fr');
  if(lang == 'fr') $('html').attr('lang','en');
}