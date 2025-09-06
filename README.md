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
   git clone https://github.com/your-username/pizza-review-chatbot.git
   cd pizza-review-chatbot
2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
3. **Prepare the dataset**  
   Ensure `realistic_restaurant_reviews.csv` is in the project folder with columns:  
   - Title  
   - Review  
   - Rating  
   - Date  
4. **Build the vector database** (first time only)  
   ```bash
   python vector.py
5. **Run the chatbot**  
   ```bash
   python main.py

