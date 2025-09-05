import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import re

# -----------------------------
# Config
# -----------------------------
MODEL_NAME = "google/flan-t5-base"

# -----------------------------
# Load & cache model pipeline
# -----------------------------
@st.cache_resource
def load_generator():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    gen = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        device_map="auto"
    )
    return gen

generator = load_generator()

# -----------------------------
# Language-specific templates
# -----------------------------
TEMPLATES = {
    "English": "Write a professional, engaging article of 3–4 paragraphs about '{topic}', focusing on storytelling, examples, and insights.",
    "Bengali": "'{topic}' বিষয়ে একটি পেশাদার, আকর্ষণীয় প্রবন্ধ লিখুন। এটি ৩–৪ অনুচ্ছেদের হতে হবে এবং গল্প বা উদাহরণ ব্যবহার করুন।",
    "Spanish": "Escribe un artículo profesional y atractivo sobre '{topic}' en 3–4 párrafos, incluyendo historias y ejemplos."
}

# -----------------------------
# Generation function
# -----------------------------
def generate_linkedin_post(topic: str, language: str = "English") -> str:
    prompt = TEMPLATES.get(language, TEMPLATES["English"]).format(topic=topic)

    out = generator(
        prompt,
        max_new_tokens=1000,       # increase for full posts
        do_sample=True,
        top_p=0.9,
        top_k=50,
        temperature=0.7,
        no_repeat_ngram_size=3,
        length_penalty=1.2,
        early_stopping=True,
        num_return_sequences=1
    )

    text = out[0]["generated_text"].strip()

    # Better paragraph formatting
    text = re.sub(r'(?<=[.?!])\s+(?=[A-Z])', '\n\n', text)

    # Remove any accidental platform references
    banned_phrases = ["contact me", "email", "@", "linkedin.com", "linkedin", "all rights reserved", "©"]
    for phrase in banned_phrases:
        if phrase.lower() in text.lower():
            text = "\n\n".join([p for p in text.split("\n\n") if phrase.lower() not in p.lower()])

    return text

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="LinkedIn Post Generator", page_icon="🚀")
st.title("🚀 LinkedIn Post Generator (Free AI Demo)")

topic = st.text_input("Enter topic:")
language = st.selectbox("Select language:", ["English", "Bengali", "Spanish"])

if st.button("Generate Post"):
    if not topic.strip():
        st.warning("Please enter a topic to generate the post.")
    else:
        with st.spinner("Generating post..."):
            try:
                post = generate_linkedin_post(topic.strip(), language)
                st.subheader("Generated Post:")
                st.write(post)

                # Download button
                st.download_button(
                    label="📥 Download Post as .txt",
                    data=post,
                    file_name=f"post_{language.lower()}.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"Generation error: {e}")
