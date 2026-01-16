# WikiHopper  
Shortest Wikipedia click-path demo with RAG sentence explanations.

## Run  
```bash
python hop.py



Path: Toaster → Air conditioning → Electricity → Albert Einstein → Black hole  
• Toaster → Air conditioning: “Air conditioning is a member of systems that provide HVAC…”  
• Electricity → Black hole: “Einstein used general relativity to argue black holes were impossible”


Tech

    NetworkX (shortest-path)
    Wikipedia-API (live data)
    Sentence-Transformers (RAG retrieval)
    Local cache (zero cost after first run)

Install

git clone https://github.com/doofenshirmtz/wikiHopper.git
cd wikiHopper
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python build_graph.py   # one-time graph build
python hop.py           # demo run
