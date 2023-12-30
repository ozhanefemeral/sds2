gsap.registerPlugin(ScrollToPlugin)

function submitForm(){

    $("form button").addClass("clickedOnce")
    $("#SecOutput").show();

    var form = $("#myform");
    var fd = new FormData(form[0]);

    //WELL
    var seedArray
    if (fd.get("seed") === "" || fd.get("seed") == fd.get("seed").match(/\s+/)) seedArray = []
    else seedArray = fd.get("seed").split(/[,\s]+/).map(Number)
    var size
    if (fd.get("size") === "") size = 1
    else size = parseInt(fd.get("size"),10);

    fetch('http://127.0.0.1:2115', {
        method: "POST",
        body: JSON.stringify({
          seed: seedArray,
          size: size
        }),
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        }
      })
        .then((response) => response.json())
        .then((json) => {
            var output = ""
            for(var el in json){
                output += json[el] + " "
            }
            $("output").text(output)

            try{
              gsap.to(window, { duration: 1, scrollTo: $("#SecOutput").position().top - 70 ,ease: "power2" });
            }
            catch(error){console.log(error)}

        } )
        .catch((error) => {
            console.error('(!) ERROR:', error);
            $("output").text('(!) ERROR: '+ error)
        });
        
}