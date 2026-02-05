document.addEventListener('DOMContentLoaded', function() {
  document.querySelector('#btn_translate').addEventListener('click', function() {
    const languageCode = document.querySelector('#language_code').value;
    if (languageCode) {
      fetch(`https://hellosalut.stefanbohacek.com/?lang=${languageCode}`)
        .then(response => response.json())
        .then(data => {
          document.querySelector('#hello').textContent = data.hello;
        });
    }
  });
});
