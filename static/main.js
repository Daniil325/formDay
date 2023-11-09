let pat = document.querySelector('.footer_pattern')
let pat_w = pat.offsetWidth;

let w = pat.offsetWidth - 10;

while (w - 65 > 0){
    pat.innerHTML += "<img class='pattern_image' src='/media/паттерн.png'>";
    w -= 65
}

console.log(pat)
