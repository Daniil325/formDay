let header = document.querySelector('.header');
let width = window.screen.width;

if (width >= 900){
    header.innerHTML += "<img class='header-image' src='/media/Шапка%20пк%20(1)-min.png' alt=''>"
}
else{
    header.innerHTML += "<img class='header-image' src='/media/Шапка%20мобил%201-min.png' alt=''>"
}

let pat = document.querySelector('.footer_pattern')
let pat_w = pat.offsetWidth;

let w = pat.offsetWidth - 10;

while (w - 65 > 0){
    pat.innerHTML += "<img class='pattern_image' src='/media/паттерн.png'>";
    w -= 65
}

