document.getElementById('health-form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent normal form submission

    const form = event.target;
    const formData = new FormData(form);

    try {
        // Send form data directly (not JSON)
        const response = await fetch('/analyze', {
            method: 'POST',
            body: formData  // Send FormData directly, no JSON conversion
        });

        // Check if the response is HTML (which it should be)
        if (response.ok) {
            const htmlText = await response.text();
            // Replace the current page with the results page
            document.open();
            document.write(htmlText);
            document.close();
        } else {
            console.error('Error:', response.status, response.statusText);
            alert('Bir hata oluştu. Lütfen tekrar deneyin.');
        }

    } catch (error) {
        console.error('API çağrısı hatası:', error);
        alert('Bağlantı hatası. Lütfen tekrar deneyin.');
    }
});