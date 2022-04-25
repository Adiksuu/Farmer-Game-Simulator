const cookieBox = document.querySelector(".wrapper"),
acceptBtn = cookieBox.querySelector(".buttons button");

    acceptBtn.onclick = () => {
         document.cookie = "CookieBy=CodeAdiksuu; max-age" + 60 * 60 * 24 * 30;

        if (document.cookie) {
        cookieBox.classList.add("hide");
        } else {
         alert("Cookies can't be set!");
    }
}

let checkCookie = document.cookie.indexOf("CookieBy=CodeAdiksuu");
checkCookie != -1 ? cookieBox.classList.add("hide") : cookieBox.classList.remove("hide");


const showMenu = (toggleId, navId) => {
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId)

    if(toggle && nav) {
        toggle.addEventListener('click', ()=>{
            nav.classList.toggle('show')
        })
    }
}

showMenu('nav-toggle', 'nav-menu')

const navLink = document.querySelectorAll('.nav__link')

function linkAction() {
    navLink.forEach(n => n.classList.remove('active'))
    this.classList.add('active')

    const navMenu = document.getElementById('nav-menu')
    navMenu.classList.remove('show')
}

navLink.forEach(n => n.addEventListener('click', linkAction))


const scrollBtn = document.querySelector(".scrollToTop-btn");

window.addEventListener("scroll", function(){
  scrollBtn.classList.toggle("active", window.scrollY > 100);
});


scrollBtn.addEventListener("click", () => {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
});



 const popupScreen = document.querySelector(".popup-screen");
    const popupBox = document.querySelector(".popup-box");
    const closeBtn = document.querySelector(".close-btn");

    window.addEventListener("load", () => {
      setTimeout(() => {
        popupScreen.classList.add("active");
      }, 500);
    });

    closeBtn.addEventListener("click", () => {
        
        popupScreen.classList.remove("active"); 
        
      document.cookie = "News=News; max-age=" + 24 * 12 *12 ;
    });

    
    const WebsiteCookie = document.cookie.indexOf("News=");

    if(WebsiteCookie != -1){
      popupScreen.style.display = "none";
    }
    else{
      popupScreen.style.display = "flex";
    }

function newWeb() {
  window.open("https://patreon.com/adiksuu", "target=_blank");
}
function downloadGame() {
  window.open("https://github.com/Adiksuu/Farmer-Game-Simulator/releases/download/Farmer-Game-v1.8/game.exe", "target=_blank");
}