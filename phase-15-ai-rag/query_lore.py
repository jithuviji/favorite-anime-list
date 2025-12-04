from sentence_transformers import SentenceTransformer
from supabase import create_client, Client
from dotenv import load_dotenv
import numpy as np
import os

load_dotenv()

SUPABASE_URL = os.getenv("https://riwwmdrpwyeaygkfkvca.supabase.co")
SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJpd3dtZHJwd3llYXlna2ZrdmNhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjM0Nzk1MTMsImV4cCI6MjA3OTA1NTUxM30.fV_FYYgVmQXa3g1UeuamIZJcG2S54AEZlfcNRP6tqEY")

supabase: Client = create_client("https://riwwmdrpwyeaygkfkvca.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJpd3dtZHJwd3llYXlna2ZrdmNhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjM0Nzk1MTMsImV4cCI6MjA3OTA1NTUxM30.fV_FYYgVmQXa3g1UeuamIZJcG2S54AEZlfcNRP6tqEY")

model = SentenceTransformer("all-MiniLM-L6-v2")

def query_lore(question):
    query_vector = model.encode(question).tolist()

    response = supabase.rpc(
        "match_lore",  # this is a Supabase SQL function
        {"query_embedding": query_vector, "match_count": 3}
    ).execute()

    return response.data


if __name__ == "__main__":
    question = input("Ask a lore question: ")
    results = query_lore(question)

    print("\nTop Results:")
    for r in results:
        print("\n---")
        print(r["chunk_text"])
