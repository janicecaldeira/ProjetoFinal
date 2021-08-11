let audio = document.querySelectorAll(".audio")
let card = document.querySelectorAll(".card")

for (let c = 0; c < card.length; c++) {
    card[c].addEventListener('mouseover', () => {
        audio[c].play()
        audio[c].volume = 0.3
    })
    card[c].addEventListener('mouseout', () => {
        audio[c].pause()
    })
}