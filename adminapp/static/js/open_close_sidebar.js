function open_sidebar() {
    document.getElementById("adminapp_users").style.width = "65%";
    document.getElementById("side__part").style.width = "25%";
    document.getElementById("admin_sidebar").style.display = "block";
    document.getElementById("close_button").style.display = "flex";
    document.getElementById("open_button").style.display = "none";
};

function close_sidebar() {
    document.getElementById("side__part").style.width = "3%";
    document.getElementById("adminapp_users").style.width = "90%";
    document.getElementById("admin_sidebar").style.display = "none";
    document.getElementById("close_button").style.display = "none";
    document.getElementById("open_button").style.display = "flex";
    document.getElementById("open_button").style.width = "100%";
};