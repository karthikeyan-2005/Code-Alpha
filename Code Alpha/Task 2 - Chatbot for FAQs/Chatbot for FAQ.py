import os
import nltk
import pandas as pd
import tkinter as tk
from tkinter import ttk, scrolledtext
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample CSV content
csv_content = """question,answer
How can I reset my password?,"To reset your password, go to the login page and click on 'Forgot Password'. Follow the instructions sent to your registered email address."
What is the refund policy?,"Our refund policy allows for refunds within 30 days of purchase. Please contact our support team for assistance."
How can I contact customer support?,"You can contact our customer support via email at support@example.com or call us at 1-800-123-4567."
Where can I find the user manual?,"The user manual can be downloaded from our website under the 'Resources' section."
What are the shipping options?,"We offer standard and express shipping options. Standard shipping takes 5-7 business days, while express shipping takes 2-3 business days."
How do I update my account information?,"To update your account information, log in to your account and go to the 'Account Settings' page."
What payment methods are accepted?,"We accept Visa, MasterCard, American Express, and PayPal."
Can I track my order?,"Yes, you can track your order using the tracking number provided in your shipping confirmation email."
What is the warranty period?,"Our products come with a one-year warranty from the date of purchase."
How do I unsubscribe from the newsletter?,"To unsubscribe from the newsletter, click on the 'Unsubscribe' link at the bottom of any newsletter email."
"""

# Save CSV content to a file
with open('faqs.csv', 'w') as file:
    file.write(csv_content)

# Provide the absolute path to the CSV file
file_path = 'faqs.csv'  # Change this path if needed

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load FAQs data
faqs = pd.read_csv(file_path)

# Preprocessing function
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return ' '.join(tokens)

# Preprocess questions
faqs['processed_question'] = faqs['question'].apply(preprocess_text)

# Vectorize the questions
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(faqs['processed_question'])

def get_most_similar_question(user_query):
    user_query_processed = preprocess_text(user_query)
    user_query_tfidf = vectorizer.transform([user_query_processed])
    cosine_similarities = cosine_similarity(user_query_tfidf, tfidf_matrix).flatten()
    most_similar_index = cosine_similarities.argmax()
    return faqs.iloc[most_similar_index]['answer'], cosine_similarities[most_similar_index]

def on_question_select(event):
    # Get the selected question
    index = question_combobox.current()
    selected_question = faqs.iloc[index]['question']
    
    # Display the selected question in the text box
    user_input.delete(1.0, tk.END)
    user_input.insert(tk.END, selected_question)

def chat():
    user_query = user_input.get(1.0, tk.END).strip()
    if user_query.lower() in ['exit', 'quit', 'bye']:
        response_text.config(state=tk.NORMAL)
        response_text.insert(tk.END, "Chatbot: Goodbye!\n")
        response_text.config(state=tk.DISABLED)
    else:
        answer, similarity = get_most_similar_question(user_query)
        response_text.config(state=tk.NORMAL)
        response_text.insert(tk.END, f"Chatbot: {answer}\n\n")
        response_text.config(state=tk.DISABLED)

# Create GUI
root = tk.Tk()
root.title("FAQ Chatbot")

# Frame for questions
question_frame = ttk.Frame(root)
question_frame.pack(pady=10)

# Question combobox
question_combobox = ttk.Combobox(question_frame, state="readonly", width=50)
question_combobox['values'] = faqs['question'].tolist()
question_combobox.current(0)
question_combobox.bind("<<ComboboxSelected>>", on_question_select)
question_combobox.pack(pady=5)

# Textbox for user input
user_input = scrolledtext.ScrolledText(root, width=60, height=5, wrap=tk.WORD)
user_input.pack(pady=5)

# Button to send user query
send_button = ttk.Button(root, text="Send", command=chat)
send_button.pack(pady=5)

# Textbox for displaying responses
response_text = tk.Text(root, width=60, height=10, wrap=tk.WORD)
response_text.pack(pady=5)
response_text.insert(tk.END, "Chatbot: Welcome to the FAQ Chatbot! Ask your questions below.\n\n")
response_text.config(state=tk.DISABLED)

root.mainloop()
