document.querySelectorAll('.main__inform-body').forEach(item => {
    item.addEventListener('click', function() {
        const modal = document.querySelector('.modal');
        modal.classList.add('active');

        // Получаем элементы
        const imgElement = this.querySelector('img') || this.querySelector('video');
        const imgSrc = imgElement ? imgElement.src : '';

        const title = this.querySelector('.main__inform-text-title')?.innerText || '';
        const text = this.querySelector('.main__inform-text-text')?.innerHTML || '';
        const region = this.querySelector('.main__inform-text-region')?.innerText || '';
        const heading = this.querySelector('.main__inform-text-heading')?.innerText || '';
        const date = this.querySelector('.main__inform-text-date')?.innerText || '';

        // Обновляем картинку/видео
        const modalImage = document.querySelector('.modal-image');
        const modalVideo = document.querySelector('.modal-video');

        if (imgElement && imgElement.tagName === 'IMG') {
            modalImage.src = imgSrc;
            modalImage.style.display = 'block';
            modalVideo.style.display = 'none';
        } else if (imgElement && imgElement.tagName === 'VIDEO') {
            modalVideo.src = imgSrc;
            modalVideo.style.display = 'block';
            modalImage.style.display = 'none';
        }

        // Обновляем текстовый контент
        const modalTextContainer = document.querySelector('.modal-text');
        modalTextContainer.innerHTML = `
            <div class="modal-text-content">${text}</div>
            <p class="modal-region">${region}</p>
            <p class="modal-name">${title}</p>
            <p class="modal-heading">${heading}</p>
            <p class="modal-date">${date}</p>
        `;
    });
});

// Закрытие модального окна
document.querySelector('.modal-close').addEventListener('click', function() {
    const modal = document.querySelector('.modal');
    modal.classList.remove('active');

    // Очищаем источники
    document.querySelector('.modal-image').src = '';
    document.querySelector('.modal-video').src = '';
});
