document.addEventListener('DOMContentLoaded', () => {
    // URL base da sua API Flask rodando localmente
    const API_URL = 'http://127.0.0.1:5000/noticias';

    // Atualiza a data no topo do jornal com a data de hoje formatada
    const options = { year: 'numeric', month: 'long', day: 'numeric', weekday: 'long' };
    document.getElementById('current-date').innerText = new Date().toLocaleDateString('pt-BR', options);

    // Função para buscar os dados da API
    async function carregarJornal() {
        try {
            const response = await fetch(API_URL);
            
            if (!response.ok) {
                throw new Error('Falha ao conectar na API de notícias');
            }

            const noticias = await response.get_json ? await response.get_json() : await response.json();

            if (noticias.length === 0) {
                const containers = [document.getElementById('featured-news'), document.getElementById('news-container')];
                containers.forEach(el => el.innerHTML = '<div class="loading">Nenhuma notícia registrada no momento.</div>');
                return;
            }

            // 1. Renderiza a primeira notícia como Destaque Principal (Manchete)
            const destaque = noticias[0];
            const featuredContainer = document.getElementById('featured-news');
            featuredContainer.innerHTML = `
                <div class="main-news-card">
                    <div class="main-content">
                        <span class="bairro-tag">Destaque: Bairro ${destaque.bairro || 'Geral'}</span>
                        <h2 class="main-title">${destaque.titulo}</h2>
                        <p class="main-snippet">${destaque.conteudo}</p>
                        <div class="meta-info">
                            <span>Por: ${destaque.autor || 'Redação'}</span> | 
                            <span>Publicado em: ${destaque.data || 'Recentemente'}</span>
                        </div>
                    </div>
                    <div style="background: #e9e8e4; border: 1px solid #ccc; display: flex; align-items: center; justify-content: center; font-family: 'Playfair Display', serif; font-style: italic; color: #666; font-size: 1.2rem; min-height: 200px;">
                        Espaço Fotográfico Comunitário
                    </div>
                </div>
            `;

            // 2. Renderiza as outras notícias na grade de Bairros
            const gridContainer = document.getElementById('news-container');
            gridContainer.innerHTML = ''; // Limpa o "Carregando"

            const noticiasSecundarias = noticias.slice(1);
            
            noticiasSecundarias.forEach(item => {
                const card = document.createElement('div');
                card.className = 'news-card';
                card.innerHTML = `
                    <span class="bairro-tag" style="background-color: #333;">${item.bairro}</span>
                    <h3 class="card-title">${item.titulo}</h3>
                    <p class="card-text">${item.conteudo}</p>
                    <div class="meta-info" style="margin-top: auto;">
                        <span>${item.data || 'Hoje'}</span> • <span>${item.autor || 'Redação'}</span>
                    </div>
                `;
                gridContainer.appendChild(card);
            });

        } catch (error) {
            console.error('Erro:', error);
            document.getElementById('featured-news').innerHTML = `
                <div class="loading" style="color: var(--accent-color); font-weight: bold;">
                    ⚠️ Erro ao carregar o jornal: Certifique-se que a sua API Flask está rodando na porta 5000!
                </div>
            `;
            document.getElementById('news-container').innerHTML = '';
        }
    }

    // Executa a carga inicial
    carregarJornal();
});