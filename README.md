# 🍕 Pizza Review Chatbot  

This project is an **AI-powered chatbot** that answers user questions about pizza restaurants using real customer reviews.  
It leverages **LangChain**, **Ollama LLM**, **Chroma vector database**, **Pandas**, and **JSON** for structured, context-aware responses.  

---

## 📌 Features  

- Uses **LangChain + Ollama LLM** (`llama3.2:latest`) for natural language understanding.  
- Stores and retrieves reviews with **Chroma vector database**.  
- Converts a CSV file of restaurant reviews into embeddings for semantic search.  
- Provides answers in **structured JSON** format with fields:  

```json
{
  "answer": "...",
  "relevant_reviews": [...],
  "show_reviews": true/false
}
```


## 📂 Project Structure 
```

├── main.py                # Chat interface for user questions
├── vector.py              # Builds/loads Chroma vector DB from CSV reviews
├── realistic_restaurant_reviews.csv   # Dataset of restaurant reviews
├── chroma_langchain_db    # Auto-generated vector database (ignored in Git)
├── __pycache__/           # Auto-generated Python cache files (ignored in Git)
└── README.md              # Project documentation
```

## ⚙️ Setup  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/divyam-bansal64/ollama_based_AI_Agent.git
   cd ollama_based_AI_Agent
2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate
3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
4. **Prepare the dataset**  
   Ensure `realistic_restaurant_reviews.csv` is in the project folder with columns:  
   - Title  
   - Review  
   - Rating  
   - Date  
5. **Build the vector database** (first time only)  
   ```bash
   python vector.py
6. **Run the chatbot**  
   ```bash
   python main.py


## 👥 Contributors
- [Divyam Bansal](https://github.com/DivyamBansal)
- [Hitesh Kholwal](https://github.com/HiteshKholwal)


