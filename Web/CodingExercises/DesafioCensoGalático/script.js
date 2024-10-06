// Variável global para armazenar os planetas
let planets = [];

// Função para obter a lista de planetas da API
async function fetchPlanets() {
  try {
    const response = await fetch('https://swapi.dev/api/planets/?format=json');
    const data = await response.json();
    planets = data.results; // Armazena os planetas na variável global
    renderPlanets(planets); // Renderiza os planetas
  } catch (error) {
    console.error('Erro ao buscar planetas:', error);
  }
}

// Função para renderizar os botões dos planetas
function renderPlanets(planetsToRender) {
  const planetList = document.getElementById('planet-list');
  planetList.innerHTML = ''; // Limpa a lista antes de renderizar os novos planetas

  planetsToRender.forEach(planet => {
    const button = document.createElement('button');
    button.textContent = planet.name; // Define o nome do planeta no botão
    button.classList.add('planet-btn');
    planetList.appendChild(button);

    // Evento de clique no botão do planeta
    button.addEventListener('click', () => {
      displayPlanetDetails(planet);
    });
  });
}

// Função para exibir os detalhes do planeta
function displayPlanetDetails(planet) {
  const detailsDiv = document.getElementById('planet-details');
  detailsDiv.innerHTML = `
    <h2>${planet.name}</h2>
    <p><strong>Climate:</strong> ${planet.climate}</p>
    <p><strong>Population:</strong> ${planet.population}</p>
    <p><strong>Terrain:</strong> ${planet.terrain}</p>
    <h3>Famous Residents</h3>
    <table id="residents-table">
      <tr>
        <th>Name</th>
        <th>Birth Year</th>
      </tr>
    </table>
  `;

  fetchResidentDetails(planet.residents).then(residents => {
    const table = document.getElementById('residents-table');
    residents.forEach(resident => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${resident.name}</td>
        <td>${resident.birth_year}</td>
      `;
      table.appendChild(row);
    });
  });
}

// Função para obter os detalhes dos residentes
async function fetchResidentDetails(urls) {
  const residents = await Promise.all(
    urls.map(async (url) => {
      const response = await fetch(url + '?format=json');
      return response.json();
    })
  );
  return residents;
}

// Função para filtrar os planetas durante a busca
document.getElementById('search').addEventListener('input', (e) => {
  const searchTerm = e.target.value.toLowerCase();
  const filteredPlanets = planets.filter(planet => 
    planet.name.toLowerCase().includes(searchTerm)
  );
  renderPlanets(filteredPlanets); // Renderiza os planetas filtrados
});

// Inicializa a busca pelos planetas ao carregar a página
fetchPlanets();
