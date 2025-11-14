document.addEventListener('DOMContentLoaded', function() {
    const header = document.getElementById('experimento-header');
    const content = document.getElementById('experimento-content');
    const icon = document.getElementById('experimento-icon');
    
    if (header && content && icon) {
        header.addEventListener('click', function() {
            if (content.style.display === 'none') {
                content.style.display = 'block';
                icon.style.transform = 'rotate(180deg)';
            } else {
                content.style.display = 'none';
                icon.style.transform = 'rotate(0deg)';
            }
        });
    }
});

async function encerrarEExportarExperimento(button) {
    button.disabled = true;
    button.textContent = 'Processando...';

    const csvUrl = button.dataset.csvUrl;
    const encerrarUrl = button.dataset.encerrarUrl;
    const csrfToken = button.dataset.csrf;

    try {
        // 1. Baixa o CSV
        const link = document.createElement('a');
        link.href = csvUrl;
        link.download = '';
        link.click();

        await new Promise(resolve => setTimeout(resolve, 500));

        const response = await fetch(encerrarUrl, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            credentials: 'same-origin'
        });

        if (response.ok) {
            window.location.href = response.url;
        } else {
            throw new Error('Erro ao encerrar experimento');
        }

    } catch (error) {
        console.error('Erro:', error);
        alert('Erro ao processar. Tente novamente.');
        button.disabled = false;
        button.textContent = 'Encerrar';
    }
}
