document.querySelectorAll('.main__inform-body').forEach(item => {
	item.addEventListener('click', function() {
		let modal = document.querySelector('.modal');
		modal.classList.add('active');
		 
		// Обновляем контент модального окна
		const imgSrc = this.querySelector('img').src;
		const title = this.querySelector('.main__inform-text-title').innerText;
		const text = this.querySelector('.main__inform-text-text').innerText;

		document.querySelector('.modal-content img').src = imgSrc;
		
		// Очищаем текущее содержимое модального окна
		const modalTextContainer = document.querySelector('.modal-text');
		modalTextContainer.innerHTML = '';  // Очищаем старые элементы
		
		// Создаём элементы для заголовка и текста
		const titleElement = document.createElement('p');
		titleElement.classList.add('modal-title');
		titleElement.innerText = title;
		
		const textElement = document.createElement('p');
		textElement.classList.add('modal-body');
		textElement.innerText = text;
		
		// Добавляем новые элементы в контейнер
		modalTextContainer.appendChild(titleElement);
		modalTextContainer.appendChild(textElement);
	});
});

// Закрытие модального окна
document.querySelector('.modal-close').addEventListener('click', function() {
	document.querySelector('.modal').classList.remove('active');
});