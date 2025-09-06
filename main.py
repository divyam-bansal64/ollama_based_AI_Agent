print(">>> Starting main.py")

from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
import json

model = OllamaLLM(model="llama3.2:latest")
print(">>> Model loaded")

template = """
You are an expert on pizza restaurant reviews.

Conversation so far:
{history}

Here are some relevant reviews from the database:
{reviews}

Here is the user's new question:
{question}

Instructions:
1. If the question is about pizza, the restaurant, or customer experience, answer using ONLY the provided reviews. 
   - Mention the review IDs you used in your reasoning.
   - If no reviews are relevant, clearly say that no reviews matched.
2. If the question is NOT related to pizza or the restaurant, ignore the reviews and answer from your own knowledge base.
3. Your response must ALWAYS be valid JSON with the following fields:
   {{
     "answer": "...",             // the full answer to the question
     "relevant_reviews": [...],   // list of review IDs you used, or [] if none
     "show_reviews": True/False   // true if you used reviews, false otherwise
   }}
"""


prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

print(">>> Ready for questions")



chat_history = []

while True:
    print("\n\n-------------------------------")
    question = input("Ask your question (q to quit, clear to reset history): ")
    print("\n\n")
    
    if question.lower() == "q":
        break
    
    # Clear conversation history
    if question.lower() == "clear":
        chat_history = []
        print("✅ Chat history cleared. Starting fresh...")
        continue

    # Retrieve relevant reviews
    reviews = retriever.invoke(question)
    chat_history.append(("User", question))

    # Get model output
    result = chain.invoke({
        "reviews": reviews,
        "question": question,
        "history": chat_history
    })

    # Parse JSON safely
    try:
        response = json.loads(result)
    except json.JSONDecodeError:
        print("Model returned invalid JSON. Raw output:")
        print(result)
        continue
    relevant_ids = response.get("relevant_reviews", [])
    if isinstance(relevant_ids, str):
        relevant_ids = [relevant_ids]
    
    show_reviews = str(response.get("show_reviews", False)).lower() == "true"

    # Always print conclusion
    print("\n\n=== AI Conclusion ===\n")
    print(response.get("answer", "No answer field returned by model."))

    # --- Internal flag logic ---
    # Only print reviews if model explicitly says show_reviews = true
    # Normalize show_reviews to a boolean

    if show_reviews:
        if relevant_ids:
            print("\n\n=== Supporting Reviews ===")
            count = 0
            for r in reviews:
                review_id = str(r.metadata.get("id"))
                if review_id in map(str, relevant_ids) and count < 3:
                    print(f"\nReview {review_id} (Rating: {r.metadata.get('rating')} | Date: {r.metadata.get('date')})")
                    print(r.page_content)
                    count += 1

    # --- End flag logic ---

    chat_history.append(("AI", response.get("answer", "")))
