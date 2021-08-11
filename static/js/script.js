let audio = document.querySelector(".audio")
let imgbox = document.querySelectorAll(".imgbox")

for(var i = imgbox.length; i--; ){
    imgbox[i].addEventListener('mouseover', () => {
        audio.currentTime = 0
        audio.play()
    })

    imgbox[i].addEventListener('mouseout', () => {
        audio.pause()
    })
}