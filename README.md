### ⚡ **Plano de Ação – MVP com Dados Externos de Filmes e Séries (2 dias)**

#### **🎯 Objetivo**

Consumir informações de filmes e séries (título, sinopse, elenco, data de lançamento etc.) por meio de APIs públicas confiáveis, para uso em recomendações e organização do histórico de consumo sem precisar armazenar localmente.

---

### 📅 **Dia 1 – Integração com APIs Externas**

#### ✅ Manhã

- Pesquisar e escolher **APIs públicas confiáveis**:
  - [OMDb API (Open Movie Database)](https://www.omdbapi.com/) – Gratuita com chave de API (ótima para séries/filmes)
  - [TMDb (The Movie Database)](https://www.themoviedb.org/documentation/api) – Completa e bem estruturada
  - [Trakt.tv](https://trakt.docs.apiary.io/) – Foco em tracking de séries assistidas

#### ✅ Tarde

- Criar chave de API (OMDb ou TMDb)
- Desenvolver função para:
  - Buscar dados por título ou ID (ex: "The Office")
  - Exibir título, sinopse, poster, nota, elenco
- Testar com frontend simples (React ou HTML/JS)

---

### 📅 **Dia 2 – Frontend + Integração com Usuário**

#### ✅ Manhã

- Criar layout de página:
  - Campo de busca por nome de filme/série
  - Resultados com cards de conteúdo vindo da API
- Adicionar recurso de “favoritar” ou “assistido” localmente (pode ser só `localStorage`)

#### ✅ Tarde

- Implementar uma seção de recomendações:
  - Simplesmente “filmes similares” via TMDb
  - Ou “mais assistidos”/“trending” com chamadas específicas
- Testar fluxo completo
- Subir no **Vercel** e entregar link com protótipo funcional

---

### ⚠️ Disclaimers Importantes

- **Não precisa armazenar dados localmente** → tudo vem direto da API em tempo real.
- **Evite uso de scraping ou sites não-oficiais** → respeite limites de requisição e termos de uso.
- **LocalStorage pode ser usado como "rascunho" de funcionalidades futuras (ex: favoritos, metas)**

Se quiser, posso:

- Gerar um exemplo de função `fetch()` para consumir a OMDb
- Criar um template de página para exibir resultados
- Ajudar a configurar e testar sua chave API

projeto-mosquito/
├── setup_environment.sh
├── terraform/
│ ├── main.tf
│ ├── outputs.tf
│ ├── variables.tf
│ └── lambda/
│ └── handler.py
└── scripts/
├── colors.sh
├── zip.sh
└── terraform.sh
