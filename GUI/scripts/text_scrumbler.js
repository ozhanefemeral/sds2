let el //= document.getElementById("scrumble")
el = document.querySelector("form button")

function randomChars(str_length=1){
    const chars = "ABCDEFGHIJKLMNOPRSTUWXYZ0123456789"
    let string = ""
    for(let i=0;i<str_length;i++){
        string += chars[Math.floor(Math.random()*chars.length)]
    }
    return string
}

const timer = ms => new Promise(res => setTimeout(res,ms))

let scrumbleRunning = false
async function scrumbleText(event){

    if(scrumbleRunning) return
    scrumbleRunning = true
    const og_str = event.target.textContent 

    for(let i=0;i<6;i++){

        event.target.innerHTML = randomChars(og_str.length)

        await timer(50)
    }

    for(let q=0;q<og_str.length+1;q++){

        event.target.innerHTML = og_str.slice(0,q) + randomChars(og_str.length-q)

        await timer(50)
    }

    event.target.textContent = og_str
    scrumbleRunning = false

}

el.onmouseover = event => scrumbleText(event)
// scrumbleText({target: el})