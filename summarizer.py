import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def summarize_text(text):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"""You are an expert AI Engineer and Scientist writing a highly curated technical blog post for an audience of experienced AI professionals giving examples using Python codes and snippets. You give citations for all the data used and the links where the data is pulled from. The topic of this blog post is based on the following text input: \n\n{text} 
                                      Requirements:
                                      The content must focus on advanced AI topics, including state-of-the-art techniques, research breakthroughs, and real-world applications.
                                      Provide detailed technical explanations, but also include practical insights that could benefit AI engineers in their work. Use formal, professional language, and assume that the reader has deep expertise in AI, including knowledge of algorithms, machine learning models, and programming. Include code snippets (in Python or other relevant languages) where necessary to demonstrate concepts. Reference recent research papers or advancements in the AI field. Add relevant figures, formulas, or diagrams using Markdown-compatible syntax where appropriate. Break down the content into clear sections with appropriate headings, subheadings, and bullet points to enhance readability. Conclude with a section on potential future directions in the topic area, discussing challenges and opportunities. The output must be a valid Markdown file ready to be uploaded to a website built using the Minimal Mistakes Jekyll framework. Use proper Markdown syntax for headings, code blocks, and links.
                                      Markdown Structure Example:
                                      ---
                                      layout: "posts"
                                      title: "Deep Dive into Transformer Models"
                                      categories: "AI-Engineering"
                                      ---
                                      
                                      # Blog Title: Some cool title.

                                      ## Introduction
                                      The transformer model architecture has revolutionized the field of natural language processing. In this blog post, we explore the internal workings of transformers and how they have evolved...
                                      
                                      ## Architecture Overview
                                      
                                      ### Self-Attention Mechanism
                                      The self-attention mechanism is one of the key innovations of the transformer model. It allows the model to weigh the importance of different words in a sentence...
                                      
                                      ```python
                                      # Example Python code for implementing self-attention
                                      def self_attention(Q, K, V):
                                        scores = Q @ K.T
                                        attention_weights = softmax(scores / sqrt(d_k))
                                        return attention_weights @ V
                                    
                                      # Recent Advancements
                                      The transformer model has seen several notable improvements, including...
                                      
                                      # Conclusion
                                      Transformers continue to be a powerful tool for various AI applications, but challenges such as scaling remain...:
                                      
                                      # Citations:
                                      1. 
                                      2. 
                                      3. 
                                      """)
    return response.text