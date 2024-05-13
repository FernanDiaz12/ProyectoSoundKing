document.addEventListener('DOMContentLoaded', () => {
    // Definimos la URL base de la API de OpenWeatherMap
    const baseUrl = 'http://api.openweathermap.org/data/2.5/weather';
    
    // Definimos la clave de API (obtén tu propia clave registrándote en https://home.openweathermap.org/users/sign_up)
    const apiKey = '7ddf78b8630cc5fe87fddc6b575a80c7';
    
    // Definimos el nombre de la ciudad para la que queremos obtener el clima
    const city = 'Viña del Mar';

    // Construimos la URL con los parámetros necesarios
    const url = `${baseUrl}?q=${city}&appid=${apiKey}&units=metric`;

    // Hacemos la solicitud HTTP a la API de OpenWeatherMap utilizando fetch
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error('¡Hubo un error al obtener el clima!');
        }
        return response.json();
      })
      .then(data => {
        // Manejamos la respuesta de la API y actualizamos el contenido en el DOM
        const climaInfo = document.getElementById('clima-info');
        climaInfo.innerHTML = `
          <p>Clima actual en ${city}</p>
          <p>Temperatura: ${data.main.temp}°C</p>
          <p>Descripción: ${data.weather[0].description}</p>
        `;
      })
      .catch(error => {
        // Manejamos cualquier error que ocurra durante la solicitud HTTP
        console.error('¡Hubo un error al obtener el clima:', error);
        const climaInfo = document.getElementById('clima-info');
        climaInfo.innerHTML = '<p>Hubo un error al obtener el clima</p>';
      });
  });