// ===== EDIÇÃO DE AUTOR - JAVASCRIPT ===== //

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('authorForm');
    const submitBtn = document.getElementById('submitBtn');
    const biographyField = document.getElementById('id_biography');
    const bioCharCount = document.getElementById('bioCharCount');
    const photoInput = document.getElementById('id_photo');
    const imagePreview = document.getElementById('imagePreview');
    const previewImg = document.getElementById('previewImg');
    const removePhotoCheckbox = document.getElementById('removePhoto');
    const currentPhoto = document.getElementById('currentPhoto');
    
    // Initialize character counter
    if (biographyField && bioCharCount) {
        const updateCounter = () => {
            const currentLength = biographyField.value.length;
            const maxLength = 2000;
            bioCharCount.textContent = `${currentLength}/${maxLength} caracteres`;
            
            if (currentLength > maxLength * 0.9) {
                bioCharCount.classList.add('text-warning');
            } else {
                bioCharCount.classList.remove('text-warning');
            }
            
            if (currentLength > maxLength) {
                bioCharCount.classList.add('text-danger');
                biographyField.value = biographyField.value.substring(0, maxLength);
            } else {
                bioCharCount.classList.remove('text-danger');
            }
        };
        
        updateCounter(); // Update on load
        biographyField.addEventListener('input', updateCounter);
    }
    
    // Image preview for new photo
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
    
    // Remove photo checkbox handler
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
    
    // Field validations
    const nameField = document.getElementById('id_name');
    const birthDateField = document.getElementById('id_birth_date');
    const nationalityField = document.getElementById('id_nationality');
    
    // Name validation
    if (nameField) {
        nameField.addEventListener('input', function() {
            const value = this.value.trim();
            if (value.length >= 3) {
                this.classList.add('is-valid');
                this.classList.remove('is-invalid');
            } else if (value.length > 0) {
                this.classList.add('is-invalid');
                this.classList.remove('is-valid');
            }
        });
        
        // Mark as valid on load
        if (nameField.value.trim().length >= 3) {
            nameField.classList.add('is-valid');
        }
        
        // Auto-focus and select
        nameField.focus();
        nameField.select();
    }
    
    // Birth date validation
    if (birthDateField) {
        birthDateField.addEventListener('change', function() {
            const selectedDate = new Date(this.value);
            const today = new Date();
            
            if (selectedDate > today) {
                alert('A data de nascimento não pode ser no futuro.');
                this.value = '';
                this.classList.add('is-invalid');
            } else if (this.value) {
                this.classList.add('is-valid');
                this.classList.remove('is-invalid');
            }
        });
        
        const today = new Date().toISOString().split('T')[0];
        birthDateField.setAttribute('max', today);
        
        if (birthDateField.value) {
            birthDateField.classList.add('is-valid');
        }
    }
    
    // Nationality auto-capitalize
    if (nationalityField) {
        nationalityField.addEventListener('blur', function() {
            if (this.value) {
                this.value = this.value.charAt(0).toUpperCase() + this.value.slice(1).toLowerCase();
                this.classList.add('is-valid');
            }
        });
        
        if (nationalityField.value) {
            nationalityField.classList.add('is-valid');
        }
    }
    
    // Biography validation
    if (biographyField && biographyField.value.trim()) {
        biographyField.classList.add('is-valid');
    }
    
    // Track form changes
    let formModified = false;
    let formSubmitted = false;
    
    form.addEventListener('input', () => formModified = true);
    form.addEventListener('submit', () => formSubmitted = true);
    
    // Warn before leaving
    window.addEventListener('beforeunload', function(e) {
        if (formModified && !formSubmitted) {
            e.preventDefault();
            e.returnValue = 'Você tem alterações não salvas. Deseja realmente sair?';
        }
    });
    
    // Cancel confirmation
    const cancelBtn = document.querySelector('a[href*="authors_list"]');
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

// Function to remove new uploaded image
function removeNewImage() {
    const photoInput = document.getElementById('id_photo');
    const imagePreview = document.getElementById('imagePreview');
    
    photoInput.value = '';
    imagePreview.style.display = 'none';
}

console.log('✅ Edit Author JS carregado!');