function updateNavbar(active_page = false) {
    if (active_page) {
        $("#main-navbar").find("li.active").removeClass("active")
        $(active_page).addClass("active")
    }
}