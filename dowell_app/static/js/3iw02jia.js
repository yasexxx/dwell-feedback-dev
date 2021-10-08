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

function removeBtnDl(){
  const elList = document.getElementsByClassName('styles_footer__PCkie')
  const new_ = document.getElementById('chat-widget-container');
  console.log(new_);
  console.log("OK ",elList.length);
  if (elList.length){
    for (let ix = 0; ix < elList.length; ix++) {
      const element = elList[ix];
      element.style.display = 'none !important';
    }
  }
}
console.log('MessageBird', MessageBirdChatWidget);
MessageBirdChatWidget.on('toggle', (isOpen) => {
  if (isOpen){
    const timeout = setTimeout(() => {removeBtnDl()}, 1500)
  }
})

// function removeDlBtn(){
  // var head = $("#iframe").contents().find("head");
  // var css = '<style type="text/css">' +
  //           '.styles_footer__PCkie {display:none !important}; ' +
  //           '</style>';
  // $(head).append(css);
// }
// removeDlBtn();
fetch_data();
const runningFunc = setInterval(fetch_data, 15000);
$(window).bind("beforeunload", function() { 
    clearInterval(runningFunc)
})