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

    const testsSection = $("#SecTests")
    testsSection.append(`
        <div id=${endpoint}>
        <input type="checkbox" disabled"/>
        <label>${endpoint.replace(/([A-Z])/g, ' $1')}</label>
        </div>`
    )

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
            $(`#${endpoint}>input`).addClass("skipped")
            return
        }

        if(json['result'].split('/')[0] == -1){
            console.log(`${endpoint}: %ctoo small input sequence`,'color: red')
            $(`#${endpoint}>input`).addClass("skipped")
        }
        else if( json['result'].split('/')[0] == json['result'].split('/')[1] 
                || (endpoint=="randomExcursionsVariantTest" && json['result'].split('/')[0]>=16) ){
            console.log(`${endpoint}: %c${json['result']}`,'color: green')
            $(`#${endpoint}>input`).addClass("passed")

            if(endpoint=="randomExcursionsTest" || endpoint=="randomExcursionsVariantTest"){
            $(`#${endpoint}`).append(` ${json['result']}`)
            }
        }
        else{        
            console.log(`${endpoint}: %c${json['result']}`,'color: red')
            $(`#${endpoint}>input`).addClass("failed")

            if(endpoint=="randomExcursionsTest" || endpoint=="randomExcursionsVariantTest"){
            $(`#${endpoint}`).append(` ${json['result']}`)
            }
        }

    })
    .catch((error) => { console.error('(!) ERROR:', error); })

}

function callTests(binStr){
    var form = $("#myform");
    var fd = new FormData(form[0]);
    if( !fd.get("tests") )  return

    $('#SecTests').html("<h1>Testy</h1>")
    $("#SecTests").show();

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



function validateNonNegativeInt(value,defaultValue=0){
    if(value==="") return defaultValue
    if(parseInt(value,10).toString()!=value || parseInt(value,10)<0) return false
    return parseInt(value,10)
}

function validateArrayOfNonNegativeInt(arrayStr,arrayLength=false,defaultValue=[]){
    
    if(arrayStr==="") return defaultValue
    
    var validArray = true
    var arraySplit = arrayStr.split(/[,\s]+/)
    if(arraySplit[arraySplit.length - 1]==="") arraySplit.pop()

    if(arrayLength!==false && arrayLength!=arraySplit.length) return false

    for(el of arraySplit){
        if(validateNonNegativeInt(el)===false) return false
    }

    arraySplit = arraySplit.map(el => parseInt(el, 10));

    return arraySplit
}

function clearFormStyle(){
    var form = $("#myform");
    var inputElements = form.find("input[type='text']")
    for(el of inputElements){
        $(el).removeClass("invalid")
    }
}

function displayInvalidFormData(key){    
    console.error(`(!) Invalid parameter: ${key}`)
    var form = $("#myform");
    var el = form.find(`input[name="${key}"]`)
    el.addClass("invalid")
}



function callXoshiro(fd){

    ///VALIDATE
    var VALID = true

    var seed = validateNonNegativeInt(fd.get("seed"),30);
    if(seed===false){
        displayInvalidFormData("seed")
        VALID = false
    }

    var bitsize = validateNonNegativeInt(fd.get("bitsize"),50);
    if(bitsize===false){
        displayInvalidFormData("bitsize")
        VALID = false
    }

    if(!VALID) {
        gsap.to(window, { duration: 1, scrollTo: $("#SecParameters").position().top - 70 ,ease: "power2" });
        return false
    }

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
}

function callMSWS(fd){

    /// VALIDATE
    var VALID = true

    var seed = validateNonNegativeInt(fd.get("seed"),1234);
    if(seed===false){
        displayInvalidFormData("seed")
        VALID = false
    }

    var bitsize = validateNonNegativeInt(fd.get("bitsize"),30);
    if(bitsize===false){
        displayInvalidFormData("bitsize")
        VALID = false
    }

    if(!VALID) {
        gsap.to(window, { duration: 1, scrollTo: $("#SecParameters").position().top - 70 ,ease: "power2" });
        return false
    }

    /// REQUEST
    fetch(`http://127.0.0.1:8090/api/generate?seed=${encodeURIComponent(seed)}&size=${encodeURIComponent(bitsize)}`, {
        method: "GET",
        mode: 'cors'
    })
    .then((response) => response.json()).then((json) => {
        $("output").text(json)
        callTests(json)
    })
    .catch((error) => { console.error('(!) ERROR:', error); $("output").text('(!) ERROR: '+ error) })
}

function callMM(fd){
    
    ///VALIDATE
    var VALID = true

    var X = validateArrayOfNonNegativeInt(fd.get("X"),false)
    if(X===false){
        displayInvalidFormData("X")
        VALID = false
    }

    var Y = validateArrayOfNonNegativeInt(fd.get("Y"),false)
    if(Y===false){
        displayInvalidFormData("Y")
        VALID = false
    }

    var aX = validateNonNegativeInt(fd.get("aX"),3141592653);
    if(aX===false){
        displayInvalidFormData("aX")
        VALID = false
    }

    var cX = validateNonNegativeInt(fd.get("cX"),2718281829);
    if(cX===false){
        displayInvalidFormData("cX")
        VALID = false
    }

    var mX = validateNonNegativeInt(fd.get("mX"),35);
    if(mX===false){
        displayInvalidFormData("mX")
        VALID = false
    }

    var seedX = validateNonNegativeInt(fd.get("seedX"),5772156649);
    if(seedX===false){
        displayInvalidFormData("seedX")
        VALID = false
    }

    var aY = validateNonNegativeInt(fd.get("aY"),2718281829);
    if(aY===false){
        displayInvalidFormData("aY")
        VALID = false
    }

    var cY = validateNonNegativeInt(fd.get("cY"),3141592653);
    if(cY===false){
        displayInvalidFormData("cY")
        VALID = false
    }

    var mY = validateNonNegativeInt(fd.get("mY"),35);
    if(mY===false){
        displayInvalidFormData("mY")
        VALID = false
    }
    
    var seedY = validateNonNegativeInt(fd.get("seedY"),1781072418);
    if(seedY===false){
        displayInvalidFormData("seedY")
        VALID = false
    }
    
    var k = validateNonNegativeInt(fd.get("k"),64);
    if(k===false || (X.length!=0 && X.length < k)){
        displayInvalidFormData("k")
        VALID = false
    }

    var n = validateNonNegativeInt(fd.get("n"),100);
    if(n===false){
        displayInvalidFormData("n")
        VALID = false
    }

    if(!VALID) {
        gsap.to(window, { duration: 1, scrollTo: $("#SecParameters").position().top - 70 ,ease: "power2" });
        return false
    }

    var endpoint = "algorithm_M_without_data"
    if(X.length!=0){
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
}

function callBD(fd){

    ///VALIDATE
    var VALID = true

    var X = validateArrayOfNonNegativeInt(fd.get("X"),false)
    if(X===false){
        displayInvalidFormData("X")
        VALID = false
    }

    var aX = validateNonNegativeInt(fd.get("aX"),3141592653);
    if(aX===false){
        displayInvalidFormData("aX")
        VALID = false
    }

    var cX = validateNonNegativeInt(fd.get("cX"),2718281829);
    if(cX===false){
        displayInvalidFormData("cX")
        VALID = false
    }

    var mX = validateNonNegativeInt(fd.get("mX"),35);
    if(mX===false){
        displayInvalidFormData("mX")
        VALID = false
    }

    var seedX = validateNonNegativeInt(fd.get("seedX"),5772156649);
    if(seedX===false){
        displayInvalidFormData("seedX")
        VALID = false
    }

    var k = validateNonNegativeInt(fd.get("k"),64);
    if(k===false || (X.length!=0 && X.length < k)){
        displayInvalidFormData("k")
        VALID = false
    }

    var n = validateNonNegativeInt(fd.get("n"),100);
    if(n===false){
        displayInvalidFormData("n")
        VALID = false
    }

    if(!VALID) {
        gsap.to(window, { duration: 1, scrollTo: $("#SecParameters").position().top - 70 ,ease: "power2" });
        return false
    }

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
}

function callWELL(fd){
    
    ///VALIDATE
    var VALID = true

    var seed = validateArrayOfNonNegativeInt(fd.get("seed"),16,[])
    if(seed===false){
        displayInvalidFormData("seed")
        VALID = false
    }

    var size = validateNonNegativeInt(fd.get("size"),100);
    if(size===false){
        displayInvalidFormData("size")
        VALID = false
    }

    if(!VALID) {
        gsap.to(window, { duration: 1, scrollTo: $("#SecParameters").position().top - 70 ,ease: "power2" });
        return false
    }

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

}



function submitForm(){

    $("#SecTests").hide();
    $("#SecOutput").hide();
    $("output").text(" Waiting for data :) ")

    var form = $("#myform");
    var fd = new FormData(form[0]);
    clearFormStyle()

    switch(currGenerator){

        case "Xoshiro":
            if(callXoshiro(fd)===false) return
            break;

        case "MSWS":
            if(callMSWS(fd)===false) return
            break;

        case "MM":
            if(callMM(fd)===false) return    
            break;

        case "BD":
            if(callBD(fd)===false) return
            break;

        case "WELL":
            if(callWELL(fd)===false) return
            break;
    }

    $("form button").addClass("clickedOnce")
    $("#SecOutput").show();
    gsap.to(window, { duration: 1, scrollTo: $("#SecOutput").position().top - 70 ,ease: "power2" });
    
}
