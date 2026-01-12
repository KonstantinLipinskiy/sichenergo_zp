document.querySelectorAll('.main__content-documents-item img').forEach(img => {
	img.addEventListener('click', function () {
	  const modal = document.querySelector('.image-modal');
	  const modalImg = modal.querySelector('img');
 
	  modalImg.src = this.src; // Устанавливаем изображение
	  modal.classList.add('active'); // Активируем модальное окно
	});
 });
 
 document.querySelector('.image-modal-close').addEventListener('click', () => {
	document.querySelector('.image-modal').classList.remove('active');
 });
 
 // Закрытие модального окна при клике на фон
 document.querySelector('.image-modal').addEventListener('click', (e) => {
	if (e.target === e.currentTarget) {
	  e.currentTarget.classList.remove('active');
	}
 });
 