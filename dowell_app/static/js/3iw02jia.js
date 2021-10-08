var initData;
var count = 0;
var countExtension = 0;
var lengthItem = 0;
function fetch_data() {
    $.ajax({
        url: "/public-api/feedback-extension",
        method: "GET",
      }).done(function(data) {
        if(data !== lengthItem){
            lengthItem = data;
            countExtension++
            if (countExtension > 1){
                $.ajax({
                    url: window.origin
                  }).done(function(data) {
                        const existData = data.split('<tbody class="d-item-wrapper">')[1]
                        let newData = existData.split('</tbody>')[0]
                        $(".d-item-wrapper").children("tr").remove();
                        $(".d-item-wrapper").append(newData);
                  });
            }
        }
      });
}
function removeDlBtn(){
  var head = $("#iframe").contents().find("head");
  var css = '<style type="text/css">' +
            '.styles_footer__PCkie {display:none}; ' +
            '</style>';
  $(head).append(css);
}
removeDlBtn();
fetch_data();
const runningFunc = setInterval(fetch_data, 15000);
$(window).bind("beforeunload", function() { 
    clearInterval(runningFunc)
})