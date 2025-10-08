document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('bookForm');
    const submitBtn = document.getElementById('submitBtn');
    const synopsisField = document.getElementById('id_synopsis');
    const charCount = document.getElementById('charCount');
    const photoInput = document.getElementById('id_photo');
    const imagePreview = document.getElementById('imagePreview');
    const previewImg = document.getElementById('previewImg');
    const removePhotoCheckbox = document.getElementById('removePhoto');
    const currentPhoto = document.getElementById('currentPhoto');
    
    // Initialize character counter
    if (synopsisField && charCount) {
        const updateCounter = () => {
            const currentLength = synopsisField.value.length;
            const maxLength = 1000;
            charCount.textContent = `${currentLength}/${maxLength} caracteres`;
            
            if (currentLength > maxLength * 0.9) {
                charCount.classList.add('text-warning');
            } else {
                charCount.classList.remove('text-warning');
            }
            
            if (currentLength > maxLength) {
                charCount.classList.add('text-danger');
                synopsisField.value = synopsisField.value.substring(0, maxLength);
            } else {
                charCount.classList.remove('text-danger');
            }
        };
        
        updateCounter(); // Initialize on load
        synopsisField.addEventListener('input', updateCounter);
    }
    
    // Image preview
    if (photoInput) {
        photoInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                if (file.size > 5 * 1024 * 1024) {
                    alert('Arquivo muito grande! Selecione uma imagem menor que 5MB.');
                    this.value = '';
                    return;
                }
                
                if (!file.type.startsWith('image/')) {
                    alert('Por favor, selecione apenas arquivos de imagem.');
                    this.value = '';
                    return;
                }
                
                const reader = new FileReader();
                reader.onload = function(e) {
                    previewImg.src = e.target.result;
                    imagePreview.style.display = 'block';
                };
                reader.readAsDataURL(file);
            }
        });
    }
    
    // Remove photo checkbox
    if (removePhotoCheckbox && currentPhoto) {
        removePhotoCheckbox.addEventListener('change', function() {
            if (this.checked) {
                currentPhoto.style.opacity = '0.3';
                currentPhoto.style.filter = 'grayscale(100%)';
            } else {
                currentPhoto.style.opacity = '1';
                currentPhoto.style.filter = 'none';
            }
        });
    }
    
    // Form submission
    form.addEventListener('submit', function(e) {
        const originalText = submitBtn.innerHTML;
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Atualizando...';
        
        setTimeout(() => {
            if (submitBtn.disabled) {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalText;
            }
        }, 10000);
    });
    
    // Validations
    const titleField = document.getElementById('id_title');
    const authorField = document.getElementById('id_author');
    
    if (titleField && titleField.value.trim()) {
        titleField.classList.add('is-valid');
        titleField.focus();
        titleField.select();
    }
    
    if (authorField && authorField.value) {
        authorField.classList.add('is-valid');
    }
    
    // Track changes
    let formModified = false;
    let formSubmitted = false;
    
    form.addEventListener('input', () => formModified = true);
    form.addEventListener('submit', () => formSubmitted = true);
    
    window.addEventListener('beforeunload', function(e) {
        if (formModified && !formSubmitted) {
            e.preventDefault();
            e.returnValue = 'Você tem alterações não salvas. Deseja realmente sair?';
        }
    });
    
    const cancelBtn = document.querySelector('a[href*="books_list"]');
    if (cancelBtn) {
        cancelBtn.addEventListener('click', function(e) {
            if (formModified) {
                const confirmed = confirm(
                    'Você tem alterações não salvas.\n\n' +
                    'Deseja realmente cancelar e perder as alterações?'
                );
                if (!confirmed) {
                    e.preventDefault();
                }
            }
        });
    }
});

function removeImage() {
    const photoInput = document.getElementById('id_photo');
    const imagePreview = document.getElementById('imagePreview');
    
    photoInput.value = '';
    imagePreview.style.display = 'none';
}