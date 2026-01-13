// Обработчик для карточек из main__content
document.querySelectorAll('.main__content-reviews-item').forEach(item => {
    item.addEventListener('click', function() {
        let modal = document.querySelector('.modal');
        modal.classList.add('active');
        
        const imgElement = this.querySelector('img');
        const titleElement = this.querySelector('.main__content-reviews-title');
        const textElement = this.querySelector('.main__content-reviews-text');
        const transvormElement = this.querySelector('.main__content-reviews-transvormator');
        const regionElement = this.querySelector('.main__content-reviews-region');
        
        document.querySelector('.modal-content img').src = imgElement.src;
        document.querySelector('.modal-text').innerHTML = `
            <p class="modal-title">${titleElement.innerText}</p>
            <div class="modal-text-content">${textElement.innerHTML}</div>
            <p class="modal-name">${transvormElement.innerText}</p>
            <p class="modal-region">${regionElement.innerText}</p>
        `;
    });
});

// Обработчик для блока main__inform
document.querySelectorAll('.main__inform').forEach(informBlock => {
    informBlock.addEventListener('click', function() {
        let modal = document.querySelector('.modal');
        modal.classList.add('active');

        const imgElement = this.querySelector('.main__inform-image img');
        const titleElement = this.querySelector('.main__inform-title');
        const nameElement = this.querySelector('.main__inform-text-title');
        const descriptionElement = this.querySelector('.main__inform-text-text');

        document.querySelector('.modal-content img').src = imgElement.src;
        document.querySelector('.modal-text').innerHTML = `
            <p class="modal-title">${titleElement.innerText}</p>
            <div class="modal-text-content">${descriptionElement.innerHTML}</div>
        `;
    });
});

// Закрытие модального окна
document.querySelector('.modal-close').addEventListener('click', function() {
    document.querySelector('.modal').classList.remove('active');
});
