import json
import networkx as nx
import os
import argparse, sentence_transformers
import wikipediaapi
from sentence_transformers import SentenceTransformer, util


cache = {}                       # explanation cache
model = SentenceTransformer('all-MiniLM-L6-v2')
wiki = wikipediaapi.Wikipedia("WikiHopper/0.1", "en")


with open("graph.json", "r") as f:
    data = json.load(f)
G = nx.Graph()
G.add_nodes_from(data["nodes"])
G.add_edges_from(data["edges"])


def find_path(start, end):
    path = nx.shortest_path(G, source=start, target=end)
    return path[:5] if len(path) > 5 else path

def get_page_text(title):
    page = wiki.page(title)
    return page.text if page.exists() else ""

# rag retriever
def best_sentence(from_page, to_page):
    key = f"{from_page}|{to_page}"
    if key in cache:                     
        return cache[key]

    text = get_page_text(to_page)
    raw  = text.split('. ')
    sentences = [s.strip() for s in raw if s.strip()]
    if not sentences:
        cache[key] = "No explanation found."
        return cache[key]

    hop_vec   = model.encode(f"{from_page} to {to_page}")
    sent_vecs = model.encode(sentences)
    scores    = util.cos_sim(hop_vec, sent_vecs)
    best_idx  = scores.argmax().item()
    best      = sentences[best_idx]

    cache[key] = best
    return best

if __name__ == "__main__":
    path = find_path("Toaster", "Black hole")
    print("Path:", " → ".join(path))
    for a, b in zip(path, path[1:]):
        print(f"• {a} → {b}: “{best_sentence(a, b)}”")


with open("cache.json", "w") as f:
    json.dump(cache, f)