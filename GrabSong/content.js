// content.js
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "clicked_browser_action" ) {
      var firstHref = $("a[href^='http']").eq(0).attr("href");

      console.log(request.url);

      // This line is new!
      /**$.ajax({
      	type: "POST",
      	url: "http://127.0.0.1:5000/grabsong",
      	link: request.url,
    	});*/
      chrome.runtime.sendMessage({"message": "open_new_tab", "url": request.url});


    }
  }
);