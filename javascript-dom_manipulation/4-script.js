document.querySelector('#add_item').addEventListener('click', function() {
  const list = document.querySelector('ul.my_list');
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  list.appendChild(newItem);
});
