import wikipediaapi,networkx as nx,json
import os

wiki = wikipediaapi.Wikipedia("WikiHopper/0.1", "en")

def get_links(title):
    page=wiki.page(title)
    if page.exists():
        return list(page.links.keys())
    return [] #incase page doesnt exist


G=nx.DiGraph()

list_titles=['Toaster', 'Electricity', 'Electron', 'Energy', 'Black hole', 'Universe'] 

for i in list_titles:
    G.add_node(i)
    for l in get_links(i)[:100]:
        G.add_edge(i, l)

print(len(G.nodes))
print(len(G.edges))


graph_dict={"nodes":list(G.nodes),"edges":list(G.edges)}


with open("graph.json", "w") as f:
    json.dump(graph_dict, f)
    f.flush()                      # still inside the with
    os.fsync(f.fileno())           # still inside the with


print("graph.json ready –", len(G.nodes), "nodes,", len(G.edges), "edges")
