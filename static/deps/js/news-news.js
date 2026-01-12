document.querySelectorAll('.main__news-item').forEach(item => {
	item.addEventListener('click', function() {
		 const modal = document.querySelector('.modal');
		 modal.classList.add('active');

		 // Получаем элементы модального окна
		 const modalImage = document.querySelector('.modal-image');
		 const modalVideo = document.querySelector('.modal-video');
		 const modalText = document.querySelector('.modal-text');

		 // Определяем, какой тип медиа контента кликнут
		 const imgElement = this.querySelector('img');
		 const videoElement = this.querySelector('video');
		 
		 if (imgElement) {
			  modalImage.src = imgElement.src;
			  modalImage.style.display = 'block';
			  modalVideo.style.display = 'none';
		 } else if (videoElement) {
			  modalVideo.src = videoElement.src;
			  modalVideo.style.display = 'block';
			  modalImage.style.display = 'none';
		 }

		 // Обновляем текстовый контент
		 modalText.innerHTML = `
			  <p class="modal-text-content">${this.querySelector('.main__news-item-text p').innerText}</p>
			  <p class="modal-region">${this.querySelector('.main__news-item-region').innerText}</p>
			  <p class="modal-name">${this.querySelector('.main__news-item-name').innerText}</p>
			  <p class="modal-heading">${this.querySelector('.main__news-item-heading').innerText}</p>
		 `;
	});
});

// Закрытие модального окна
document.querySelector('.modal-close').addEventListener('click', function() {
	const modal = document.querySelector('.modal');
	modal.classList.remove('active');

	// Очищаем источники, чтобы предотвратить продолжение воспроизведения
	document.querySelector('.modal-image').src = '';
	document.querySelector('.modal-video').src = '';
});