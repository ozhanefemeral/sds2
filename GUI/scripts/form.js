function isNonNegInt(str){
    var valid = true
    if( str==="" || parseInt(str,10).toString()!=str || parseInt(str,10)<0 )valid = false
    return valid
}

function arrayToBinString(inputArray){
  var result = ""
  for( el of inputArray ){
      for (let i = 31; i >= 0; i--) {
          result += (parseInt(el,10) & (1 << i)) ? '1' : '0';
      }
  }
  return result
}

function fetchAndRenderDataFromTest(binStr,endpoint){

  fetch(`http://127.0.0.1:5001/${endpoint}`, {
    method: "POST",
    mode: 'cors',
    body: JSON.stringify({
      sequence: binStr
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  })
  .then((response) => response.json()).then((json) => {

      if("error" in json){
        console.error(`(!) (${endpoint}) ERROR: ${json['error']}`)
        return
      }

      if(json['result'].split('/')[0] == -1){
        console.log(`${endpoint}: %ctoo small input sequence`,'color: red')
      }
      else if( json['result'].split('/')[0] == json['result'].split('/')[1] 
               || (endpoint=="randomExcursionsVariantTest" && json['result'].split('/')[0]>=16) ){
        console.log(`${endpoint}: %c${json['result']}`,'color: green')
      }
      else{        
        console.log(`${endpoint}: %c${json['result']}`,'color: red')
      }

  })
  .catch((error) => { console.error('(!) ERROR:', error); })

}

function callTests(binStr){
  var form = $("#myform");
  var fd = new FormData(form[0]);
  if( !fd.get("tests") )  return

  $("#SecTests").show();

  // console.log("(!) przechodze do testów")
  // console.log(`(!) bitStr = ${binStr}`)

  // fetchAndRenderDataFromTest(bitsize,"testRandomnessWithNISTPakcage")
  fetchAndRenderDataFromTest(binStr,"frequencyMonobitTest")
  fetchAndRenderDataFromTest(binStr,"frequencyTestWithinBlock")
  fetchAndRenderDataFromTest(binStr,"runsTest")
  fetchAndRenderDataFromTest(binStr,"longestRunOfOnesInABlockTest")
  fetchAndRenderDataFromTest(binStr,"binaryMatrixRankTest")
  fetchAndRenderDataFromTest(binStr,"discreteFourierTransformTest")
  fetchAndRenderDataFromTest(binStr,"nonOverlappingTemplateMatchingTest")
  fetchAndRenderDataFromTest(binStr,"overlappingTemplateMatchingTest")
  fetchAndRenderDataFromTest(binStr,"maurersUniversalStatisticalTest")
  fetchAndRenderDataFromTest(binStr,"serialTest")
  fetchAndRenderDataFromTest(binStr,"approximateEntropyTest")
  fetchAndRenderDataFromTest(binStr,"cumulativeSumsForwardTest")
  fetchAndRenderDataFromTest(binStr,"cumulativeSumsBackwardTest")
  fetchAndRenderDataFromTest(binStr,"randomExcursionsTest")
  fetchAndRenderDataFromTest(binStr,"randomExcursionsVariantTest")

}

function submitForm(){

    $("form button").addClass("clickedOnce")
    $("output").text(" Waiting for data :) ")
    $("#SecTests").hide();

    var form = $("#myform");
    var fd = new FormData(form[0]);    

    switch(currGenerator){

      //TODO: CORS!!!
      case "Xoshiro":

        /// VALIDATE FORM DATA FOR XOSHIRO
        //validate seed <- non-negative INT
        var seed = fd.get("seed")==="" ? 30 : fd.get("seed")
        if( !isNonNegInt(seed) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr SEED")
          return;
        }
        seed = parseInt(seed,10)
        //validate bit size <- non-negative INT
        var bitsize = fd.get("bitsize")==="" ? 50 : fd.get("bitsize")
        if( !isNonNegInt(bitsize) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr BIT SIZE")
          return;
        }
        bitsize = parseInt(bitsize,10)

        /// REQUEST
        fetch(`http://127.0.0.1:5004/api/generate?seed=${encodeURIComponent(seed)}&size=${encodeURIComponent(bitsize)}`, {
            method: "GET",
            mode: 'cors'
        })
        .then((response) => response.json()).then((json) => {
            $("output").text(json)
            callTests(json)
        })
        .catch((error) => { console.error('(!) ERROR:', error); $("output").text('(!) ERROR: '+ error) })

        break;

      //TODO: 
      case "MSWS":
        /// VALIDATE FORM DATA FOR MSWS
        //validate seed
        //validate bit size
        /// REQUEST
        $("output").text("(!) Not implemented")
        break;

      //TODO: 
      case "MM":
        /// VALIDATE FORM DATA FOR MM

        //validate X
        var X = []
        var XArray = []
        if( fd.get("X")!=="" ){
          XArray = fd.get("X").split(/[,\s]+/)
          if(XArray[XArray.length - 1]==="")XArray.pop()
          for(el of XArray){
            if(!isNonNegInt(el)){
              //TODO: wyświetlanie błędu w formularzu
              console.error("niepoprawny parametr X, złe wartości")
              return;
            }
          }
        }        
        X = XArray.map(element => parseInt(element, 10));

        //validate Y
        var Y = []
        var YArray = []
        if( fd.get("Y")!=="" ){
          YArray = fd.get("Y").split(/[,\s]+/)
          if(YArray[YArray.length - 1]==="")YArray.pop()
          for(el of YArray){
            if(!isNonNegInt(el)){
              //TODO: wyświetlanie błędu w formularzu
              console.error("niepoprawny parametr Y, złe wartości")
              return;
            }
          }
        }
        Y = YArray.map(element => parseInt(element, 10));

        //validate aX
        var aX = fd.get("aX")==="" ? 3141592653 : fd.get("aX")
        if( !isNonNegInt(aX) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr aX")
          return;
        }
        aX = parseInt(aX,10)

        //validate cX
        var cX = fd.get("cX")==="" ? 2718281829 : fd.get("cX")
        if( !isNonNegInt(cX) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr cX")
          return;
        }
        cX = parseInt(cX,10)

        //validate mX
        var mX = fd.get("mX")==="" ? 35 : fd.get("mX")
        if( !isNonNegInt(mX) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr mX")
          return;
        }
        mX = parseInt(mX,10)

        //validate seedX
        var seedX = fd.get("seedX")==="" ? 5772156649 : fd.get("seedX")
        if( !isNonNegInt(seedX) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr seedX")
          return;
        }
        seedX = parseInt(seedX,10)

        //validate aY
        var aY = fd.get("aY")==="" ? 2718281829 : fd.get("aY")
        if( !isNonNegInt(aY) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr aY")
          return;
        }
        aY = parseInt(aY,10)

        //validate cY
        var cY = fd.get("cY")==="" ? 3141592653 : fd.get("cY")
        if( !isNonNegInt(cY) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr cY")
          return;
        }
        cY = parseInt(cY,10)

        //validate mY
        var mY = fd.get("mY")==="" ? 35 : fd.get("mY")
        if( !isNonNegInt(mY) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr mY")
          return;
        }
        mY = parseInt(mY,10)
        
        //validate seedY
        var seedY = fd.get("seedY")==="" ? 1781072418 : fd.get("seedY")
        if( !isNonNegInt(seedY) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr seedY")
          return;
        }
        seedY = parseInt(seedY,10)

        //validate k
        var k = fd.get("k")==="" ? 64 : fd.get("k")
        if( !isNonNegInt(k) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr k")
          return;
        }
        else if( XArray.length!=0 && XArray.length < k ){          
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr k, powinien byc mniejszy niż size(X)")
          return;
        }
        k = parseInt(k,10)

        //validate n
        var n = fd.get("n")==="" ? 100 : fd.get("n")
        if( !isNonNegInt(n) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr n")
          return;
        }
        n = parseInt(n,10)

        var endpoint = "algorithm_M_without_data"
        if(X.length!=0 && Y.length!=0){
          endpoint = "algorithm_M_with_data"
        }

        /// REQUEST
        fetch(`http://127.0.0.1:5002/${endpoint}`, {
            method: "POST",
            mode: 'cors',
            body: JSON.stringify({
              aX: aX,
              cX: cX,
              mX: mX,
              seedX: seedX,
              aY: aY,
              cY: cY,
              mY: mY,
              seedY: seedY,
              k: k,
              n: n,
              X: X,
              Y: Y
            }),
            headers: {
              "Content-type": "application/json; charset=UTF-8"
            }
        })
        .then((response) => response.json()).then((json) => {
            var str = ""
            for(var el of json["result"]){
              str += el + " "
            }
            $("output").text(str)
            callTests(arrayToBinString(json["result"]))
        })
        .catch((error) => { console.error('(!) ERROR:', error); $("output").text('(!) ERROR: '+ error) })
        break;

      //TODO: 
      case "BD":   

        /// VALIDATE FORM DATA FOR BD
        //validate X
        var X = []
        var XArray = []
        if( fd.get("X")!=="" ){
          XArray = fd.get("X").split(/[,\s]+/)
          if(XArray[XArray.length - 1]==="")XArray.pop()
          for(el of XArray){
            if(!isNonNegInt(el)){
              //TODO: wyświetlanie błędu w formularzu
              console.error("niepoprawny parametr X, złe wartości")
              return;
            }
          }
        }        
        X = XArray.map(element => parseInt(element, 10));

        //validate aX
        var aX = fd.get("aX")==="" ? 3141592653 : fd.get("aX")
        if( !isNonNegInt(aX) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr aX")
          return;
        }
        aX = parseInt(aX,10)

        //validate cX
        var cX = fd.get("cX")==="" ? 2718281829 : fd.get("cX")
        if( !isNonNegInt(cX) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr cX")
          return;
        }
        cX = parseInt(cX,10)

        //validate mX
        var mX = fd.get("mX")==="" ? 35 : fd.get("mX")
        if( !isNonNegInt(mX) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr mX")
          return;
        }
        mX = parseInt(mX,10)

        //validate seedX
        var seedX = fd.get("seedX")==="" ? 5772156649 : fd.get("seedX")
        if( !isNonNegInt(seedX) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr seedX")
          return;
        }
        seedX = parseInt(seedX,10)

        //validate k
        var k = fd.get("k")==="" ? 64 : fd.get("k")
        if( !isNonNegInt(k) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr k")
          return;
        }
        else if( XArray.length!=0 && XArray.length < k ){          
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr k, powinien byc mniejszy niż size(X)")
          return;
        }
        k = parseInt(k,10)

        //validate n
        var n = fd.get("n")==="" ? 100 : fd.get("n")
        if( !isNonNegInt(n) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr n")
          return;
        }
        n = parseInt(n,10)    

        var endpoint = "algorithm_B_without_data"
        if(X.length!=0){
          endpoint = "algorithm_B_with_data"
        }

        /// REQUEST
        fetch(`http://127.0.0.1:5002/${endpoint}`, {
            method: "POST",
            mode: 'cors',
            body: JSON.stringify({
              aX: aX,
              cX: cX,
              mX: mX,
              seedX: seedX,
              k: k,
              n: n,
              X: X
            }),
            headers: {
              "Content-type": "application/json; charset=UTF-8"
            }
        })
        .then((response) => response.json()).then((json) => {
            var str = ""
            for(var el of json["result"]){
              str += el + " "
            }
            $("output").text(str)
            callTests(arrayToBinString(json["result"]))
        })
        .catch((error) => { console.error('(!) ERROR:', error); $("output").text('(!) ERROR: '+ error) })
        break;

      //TODO:
      case "WELL":

        /// VALIDATE FORM DATA FOR WELL
        //TODO: naprawić 
        //validate seed <- array of 16 non-negative INTs
        var seed = []
        var seedArray = []
        if( fd.get("seed")!=="" ){
          seedArray = fd.get("seed").split(/[,\s]+/)
          if(seedArray[seedArray.length - 1]==="")seedArray.pop()
          if( seedArray.length != 16 ){
            //TODO: wyświetlanie błędu w formularzu
            console.error("niepoprawny parametr SEED, zła długość")
            return;
          }
          for(el of seedArray){
            if(!isNonNegInt(el)){
              //TODO: wyświetlanie błędu w formularzu
              console.error("niepoprawny parametr SEED, złe wartości")
              return;
            }
          }
        }
        seed = seedArray.map(element => parseInt(element, 10));

        //validate size <- non-negative INT
        //TODO: Zmienić z 630 -> 100
        var size = fd.get("size")==="" ? 630 : fd.get("size")
        if( !isNonNegInt(size) ){
          //TODO: wyświetlanie błędu w formularzu
          console.error("niepoprawny parametr SIZE")
          return;
        }
        size = parseInt(size,10)

        /// REQUEST
        fetch("http://127.0.0.1:5003", {
            method: "POST",
            mode: 'cors',
            body: JSON.stringify({
              seed: seed,
              size: size
            }),
            headers: {
              "Content-type": "application/json; charset=UTF-8"
            }
        })
        .then((response) => response.json()).then((json) => {
            var str = ""
            for(var el in json){
              str += json[el] + " "
            }
            $("output").text(str)
            callTests(arrayToBinString(json))
        })
        .catch((error) => { console.error('(!) ERROR:', error); $("output").text('(!) ERROR: '+ error) })

        break;
    }

    // $("#SecOutput").show();
    // gsap.to(window, { duration: 1, scrollTo: $("#SecOutput").position().top - 70 ,ease: "power2" });
        
}
