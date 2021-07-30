let inputUser = document.querySelector("#user")
let inputPassword = document.querySelector("#password")
let btnEntrar= document.querySelector("#entrar")
let userOk = false
let passwordOk = false
let audio = document.querySelector("audio")

btnEntrar.disabled = true

inputUser.addEventListener('mouseover', () => {
    audio.currentTime = 0
    audio.play()
})

inputUser.addEventListener('keyup', () => { 
    if(inputUser.value == "admin"){
        userOk = true
    } else {
        userOk = false
    }

    if(userOk && passwordOk){
        btnEntrar.disabled = false
    } else{
        btnEntrar.disabled = true
    }
})



inputPassword.addEventListener('keyup', () => {

    if(inputPassword.value == "1234") {
        passwordOk = true
    } else {
        passwordOk = false
    }

    if(userOk && passwordOk){
        btnEntrar.disabled = false
    } else{
        btnEntrar.disabled = true
    }
})

btnEntrar.addEventListener('click', () => {
   alert("Acesso liberado")
})