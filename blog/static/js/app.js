const mainMenu = document.querySelector(".mainMenu");
const openMenu = document.querySelector(".openMenu");
const closeMenu = document.querySelector(".closeMenu");

openMenu.addEventListener('click', show);
closeMenu.addEventListener('click', hide);

function show() {
    mainMenu.style.display = 'flex';
    mainMenu.style.top = '0';
}

function hide() {
    mainMenu.style.top = '-100%';
}