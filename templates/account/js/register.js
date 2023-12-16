document.getElementById("btnRegister").addEventListener("click", () => {
    let name = document.getElementById("name").value;
    let firstname = document.getElementById("firstname").value;
    let surname = document.getElementById("surname").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let password_confirm = document.getElementById("password_confirm").value;
    let capcha = document.getElementById("capcha").value;

    if (!name || !firstname || !surname || !email || !password || !password_confirm || !capcha) {
        alert("Please fill in all fields!");
        return;
    }

    if (password !== password_confirm) {
        alert("Passwords do not match!");
        return;
    }

    var user = {
        name: name,
        firstname: firstname,
        surname: surname,
        email: email,
        password: password,
        capcha: capcha
    };

    // Сохраняем пользователя в локальное хранилище
    localStorage.setItem("user", JSON.stringify(user));
    alert("User registered successfully!");

    // Очищаем значения инпутов после регистрации
    document.getElementById("name").value = "";
    document.getElementById("firstname").value = "";
    document.getElementById("surname").value = "";
    document.getElementById("email").value = "";
    document.getElementById("password").value = "";
    document.getElementById("password_confirm").value = "";
    document.getElementById("capcha").value = "";
});