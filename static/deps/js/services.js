document.querySelectorAll('.main__inform-body').forEach(item => {
	item.addEventListener('click', function() {
		let modal = document.querySelector('.modal');
		modal.classList.add('active');
		
		// Обновляем контент модального окна
		const videoSrc = this.querySelector('video').src;
		const title = this.querySelector('.main__inform-text-title').innerText;
		const text = this.querySelector('.main__inform-text-text').innerText;

		// Заменяем источник видео
		const modalVideo = document.querySelector('.modal-content video');
		modalVideo.src = videoSrc;
		modalVideo.load();  // Загружаем новое видео
		modalVideo.play();  // Автоматически воспроизводим видео

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
	const modal = document.querySelector('.modal');
	modal.classList.remove('active');

	// Останавливаем видео при закрытии модального окна
	const modalVideo = document.querySelector('.modal-content video');
	modalVideo.pause();
	modalVideo.currentTime = 0;
});

