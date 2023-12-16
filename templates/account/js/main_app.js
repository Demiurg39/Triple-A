// ! SEARCH
// Функция для сохранения данных в локальное хранилище
function saveToLocalStorage(key, value) {
    localStorage.setItem(key, JSON.stringify(value));
}

// Функция для загрузки данных из локального хранилища
function loadFromLocalStorage(key) {
    const data = localStorage.getItem(key);
    return data ? JSON.parse(data) : null;
}

// Обработчик события для формы поиска
document.getElementById('searchForm').addEventListener('submit', function (event) {
    event.preventDefault(); 
    const searchTerm = document.getElementById('searchInput').value;

    // Проверка на пустой поисковый запрос
    if (!searchTerm) {
        alert("Please enter a search term");
        return;
    }

    // Получаем ранее сохраненные поисковые запросы
    let searchHistory = loadFromLocalStorage('searchHistory') || [];
    
    // Добавляем текущий запрос в историю
    searchHistory.push(searchTerm);
    
    // Сохраняем обновленную историю в локальное хранилище
    saveToLocalStorage('searchHistory', searchHistory);

    // Очищаем поле ввода
    document.getElementById('searchInput').value = '';

    // Выводим в консоль для проверки
    console.log("Search term saved:", searchTerm);
    console.log("Search history:", searchHistory);
});
    // !  MODAL
    let modalMenu = document.querySelector("#modalBurgerMenu")
    modalMenu
    let burgerMenu = document.querySelector("#burgerMenu");
    burgerMenu.addEventListener("click", ()=> {
        // Отображаем модальное окно при клике
        let modal = new bootstrap.Modal(document.getElementById('modalBurgerMenu'));
        modal.show();
    });
    