function loadTextFile() {
    // Path to your text file
    const filePath = 'score.txt';

    // Use fetch API to get the content of the file
    fetch(filePath)
        .then(response => response.text())
        .then(data => {
            // Split lines into an array
            const lines = data.split('\n');

            // Get the container element
            const container = document.getElementById('text-container');

            // Append each line to the container
            lines.forEach(line => {
                const p = document.createElement('p');
                p.textContent = line;
                container.appendChild(p);
            });
        })
        .catch(error => console.error('Error loading text file:', error));
}

// Call the function when the page is loaded
window.onload = loadTextFile;