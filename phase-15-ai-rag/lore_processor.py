from sentence_transformers import SentenceTransformer
from supabase import create_client, Client
from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()

SUPABASE_URL = os.getenv("https://riwwmdrpwyeaygkfkvca.supabase.co")
SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJpd3dtZHJwd3llYXlna2ZrdmNhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjM0Nzk1MTMsImV4cCI6MjA3OTA1NTUxM30.fV_FYYgVmQXa3g1UeuamIZJcG2S54AEZlfcNRP6tqEY"
)   # service role key required for vector insert

supabase: Client = create_client("https://riwwmdrpwyeaygkfkvca.supabase.co","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJpd3dtZHJwd3llYXlna2ZrdmNhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjM0Nzk1MTMsImV4cCI6MjA3OTA1NTUxM30.fV_FYYgVmQXa3g1UeuamIZJcG2S54AEZlfcNRP6tqEY")

model = SentenceTransformer("all-MiniLM-L6-v2")


# ---------- Chunking Function ----------
def chunk_text(text, max_length=350):
    words = text.split()
    chunks = []

    current = []

    for word in words:
        current.append(word)
        if len(" ".join(current)) > max_length:
            chunks.append(" ".join(current))
            current = []

    if current:
        chunks.append(" ".join(current))

    return chunks


# ---------- Store embeddings in Supabase ----------
def store_in_supabase(chunk, embedding):
    data = {
        "chunk_text": chunk,
        "embedding": embedding.tolist(),  # convert vector to list
    }
    supabase.table("anime_lore").insert(data).execute()


# ---------- MAIN ----------
def process_lore():
    with open("lore.txt", "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text)
    print(f"Total chunks created: {len(chunks)}")

    for chunk in chunks:
        vector = model.encode(chunk)
        store_in_supabase(chunk, vector)

    print("Lore processing completed! Embeddings stored in Supabase.")


if __name__ == "__main__":
    process_lore()
