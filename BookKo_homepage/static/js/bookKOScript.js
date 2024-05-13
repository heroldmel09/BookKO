
const animetion_search = (search, button) => {
    const searchBar = document.getElementById(search),
        searchbutton = document.getElementById(button)
    searchbutton.addEventListener('click', () => {
        searchBar.classList.toggle("show")
    })
}

animetion_search('search-bar', 'search-b')
//good night

const loginlink = document.querySelector(".login-signup")
const registerlink = document.querySelector(".register-signup")
const LoginContainer = document.querySelector(".login-container");
const btnLogin = document.querySelector(".user");
const btnClose = document.querySelector(".close-login-btn");
const btnRegister = document.querySelector(".Registerbtn")



registerlink.addEventListener('click', () => {
    LoginContainer.classList.add("Active-user");
})

loginlink.addEventListener('click', () => {
    LoginContainer.classList.remove("Active-user");
    LoginContainer.classList.remove("Active-userR");
})

btnLogin.addEventListener('click', () => {
    LoginContainer.classList.add("pop-upLogin");
    LoginContainer.classList.remove("Active-user");
    LoginContainer.classList.remove("Active-userR");
})

btnClose.addEventListener('click', () => {
    LoginContainer.classList.remove("pop-upLogin");
    LoginContainer.classList.remove("Active-userR");
    LoginContainer.classList.remove("Active-user");
})

btnRegister.addEventListener('click', () => {
    LoginContainer.classList.add("pop-upLogin");
    LoginContainer.classList.add("Active-userR");
})

