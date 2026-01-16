# WikiHopper  
Shortest Wikipedia click-path demo with RAG sentence explanations.

## Run
'''bash
python3 hop.py

# OUTPUT

    Path: Toaster → Air conditioning → Electricity → Albert Einstein → Black hole  
    • Toaster → Air conditioning: “Air conditioning is a member of systems that provide HVAC…”  
    • Electricity → Black hole: “Einstein used general relativity to argue black holes were impossible”

# TECH
NetworkX (shortest-path)
Wikipedia-API (live data)
Sentence-Transformers (RAG retrieval)

# INSTALL

    git clone https://github.com/doofenshirmtz/wikiHopper.git
    cd wikiHopper
    python3 -m venv venv && source venv/bin/activate
    pip install -r requirements.txt
    python3 build_graph.py   # one-time graph build
    python3 hop.py           # demo run


