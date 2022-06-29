let addMessage = document.querySelector('.message'),
    addButton = document.querySelector('.add'),
    todo = document.querySelector('.todo');

    let todoList = [];

    /*Проверка данных в памяти и их вывод */
    if(localStorage.getItem('todo')){
        todoList = JSON.parse(localStorage.getItem('todo'));
        displayMessages();
    }

    /* Обработчик событий*/
addButton.addEventListener('click', function(){
    if(!addMessage.value) return;
    let newTodo = {
        todo: addMessage.value,
        checked: false,
        important: false
    };

    todoList.push(newTodo);
    displayMessages();
    /* Сохранение данных */
    localStorage.setItem('todo' , JSON.stringify(todoList));
    addMessage.value = '';
});
     /* Вывод на экран*/
function displayMessages(){
    let displayMessage = '';
    if(todoList.length === 0) todo.innerHTML = '';
    todoList.forEach(function(item, i){
        /* верства сообщения, добавление сообщения и проверка сосотояния*/
        displayMessage += `
        <li>
            <input type='checkbox' id='item_${i}' ${item.checked ? 'checked' : ''}>
            <label for='item_${i}' class="${item.important ? 'important' : ''}">${item.todo}</label>        
        </li>
        `;
        todo.innerHTML = displayMessage;
    });
}
/* Проверка постановки галочки */
todo.addEventListener('change', function(event){
    let valueLabel = todo.querySelector('[for='+ event.target.getAttribute('id') +']').innerHTML;
    todoList.forEach(function(item){
         if (item.todo === valueLabel){
             item.checked = !item.checked;
             localStorage.setItem('todo' , JSON.stringify(todoList));
         }
    });
}); 

/* Контекстное меню для удаления и выделения элементов */
todo.addEventListener('contextmenu', function(event){
    event.preventDefault();
    todoList.forEach(function(item, i){
        if(item.todo === event.target.innerHTML){
            if(event.ctrKey || event.metaKey){
                todoList.splice(i, 1);
            }else{
                item.important = !item.important;
            }
            displayMessages();
            localStorage.setItem('todo' , JSON.stringify(todoList));
        }
    });
});