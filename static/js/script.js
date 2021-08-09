let audio = document.querySelector("#audio")
let tocar = document.querySelector("#personagem")

audio.pause()

tocar.addEventListener('mouseover', () => {
    audio.currentTime = 0
    audio.play()
})

tocar.addEventListener('mouseout', () => {
    audio.pause()
})