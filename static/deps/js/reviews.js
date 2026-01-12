document.querySelectorAll('.main__content-reviews-item').forEach(item => {
	item.addEventListener('click', function() {
		 let modal = document.querySelector('.modal');
		 modal.classList.add('active');
		 
		 // Получаем необходимые элементы
		 const imgElement = this.querySelector('img');
		 const titleElement = this.querySelector('.main__content-reviews-title');
		 const textElement = this.querySelector('.main__content-reviews-text');
		 const transvormElement = this.querySelector('.main__content-reviews-transvormator');
		 const regionElement = this.querySelector('.main__content-reviews-region');
		 
		 // Присваиваем значения в модальное окно
		 document.querySelector('.modal-content img').src = imgElement.src;
		 document.querySelector('.modal-text').innerHTML = `
			<p>${titleElement.innerText}</p>
			<p>${textElement.innerText}</p>
			<p>${transvormElement.innerText}</p>
			<p>${regionElement.innerText}</p>`;
		 
		 // Теперь можно изменять или манипулировать этими элементами
		 // Например, изменяем текст в .main__content-reviews-title
		//  titleElement.innerText = "Новий заголовок"; // Изменение текста заголовка
	});
});

// Закрытие модального окна
document.querySelector('.modal-close').addEventListener('click', function() {
	document.querySelector('.modal').classList.remove('active');
});