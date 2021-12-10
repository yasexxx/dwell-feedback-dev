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

fetch_data();
const runningFunc = setInterval(fetch_data, 15000);


function clearInfoUser() {
  return setTimeout( () => {
    if(window.MessageBirdChatWidget){
      window.MessageBirdChatWidget.logout()
      .then().catch( () => console.error('Fail to erase some information'));
    }
  }, 3000);
}
var timeout = clearInfoUser();

window.addEventListener('beforeunload', function (e) {
    clearInterval(runningFunc);
    clearTimeout(timeout);
});