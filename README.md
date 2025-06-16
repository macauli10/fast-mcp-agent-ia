# 🤖 FAST-MCP: Multi-Agent Chatbot com Groq, Supabase e YFinance

Projeto que integra **agentes de IA autônomos** com múltiplas ferramentas como Supabase, YFinance e embeddings com Hugging Face, usando a arquitetura do [FastMCP](https://github.com/crewai/fastmcp) e [CrewAI](https://github.com/joaomdmoura/crewai).


---

## 🧠 Tecnologias Utilizadas

| Tecnologia | Descrição |
|-----------|-----------|
| 🧩 `FastMCP` | Infraestrutura assíncrona para orquestração de agentes multi-ferramentas. |
| 🧠 `CrewAI` | Criação de agentes inteligentes com memória e objetivo definido. |
| 🦙 `Groq + LLaMA 3 70B` | LLM via API da Groq com alto desempenho para linguagem natural. |
| 📦 `Supabase` | Ferramenta de backend usada como fonte de dados e autenticação. |
| 📊 `YFinance` | Consulta e análise de dados financeiros em tempo real. |
| 🧠 `HuggingFaceEmbeddings` | Geração de vetores semânticos para memória contextual dos agentes. |
| 🔐 `python-dotenv` | Carregamento automático de variáveis sensíveis via `.env`. |
| 🧾 `.gitignore` | Evita o versionamento de arquivos sensíveis (como `.env`). |
| 💻 `Visual Studio Code` | Ambiente de desenvolvimento principal. |
| 🌐 `GitHub` | Controle de versão e hospedagem do repositório. |
| 📊 `Streamlit` (planejado) | Interface visual amigável para interação com o chatbot. |

---

## 📁 Estrutura do Projeto

```bash
fast-mcp/
├── .venv/                        # Ambiente virtual Python
├── .env                          # Variáveis secretas (GROQ, Supabase)
├── .gitignore
├── main.py                       # Entry point (pode rodar servidor Streamlit)
├── src/
│   ├── app.py                    # Script principal com chamada ao agente
│   ├── mcp_server.py             # Configuração de ferramentas e agentes
│   └── teste.py                  # Testes e desenvolvimento local
├── requirements.txt              # Dependências do projeto
├── pyproject.toml                # Metadados do projeto Python
├── README.md                     # Documentação do projeto
🔐 Variáveis de Ambiente
Crie um arquivo .env com as seguintes chaves:

env
Copy
Edit
GROQ_API_KEY=your_groq_key_here
SUPABASE_ACCESS_TOKEN=your_supabase_pat
O .env não deve ser commitado! Ele está protegido via .gitignore.

▶️ Como Rodar o Projeto
Clone o repositório

bash
Copy
Edit
git clone https://github.com/seu-usuario/fast-mcp-agent-ia.git
cd fast-mcp
Ative o ambiente virtual

bash
Copy
Edit
# Se estiver usando conda
conda activate fast-mcp

# Ou use venv
source .venv/bin/activate
Instale as dependências

bash
Copy
Edit
pip install -r requirements.txt
Execute o servidor MCP

bash
Copy
Edit
python src/app.py
(Opcional) Execute a interface com Streamlit (se implementada):

bash
Copy
Edit
streamlit run main.py
💡 O que o projeto faz?
Este projeto conecta perguntas do usuário a múltiplas ferramentas, e usa um agente de IA para escolher entre elas. Ele entende perguntas como:

"Quais foram as ações mais valorizadas hoje?"

"Quais os valores armazenados no Supabase?"

"Me dê uma análise de vendas com base nos dados disponíveis."

📌 Status do Projeto
🚧 Em desenvolvimento. A parte de integração com Supabase e YFinance está sendo testada. Interface Streamlit em construção.

