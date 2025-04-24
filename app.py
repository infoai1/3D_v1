import json, streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ---- load data ----
GRAPH = json.loads(Path("graph.json").read_text(encoding="utf-8"))

# ---- sidebar filters ----
st.sidebar.header("Filters")
all_cats = sorted({n["category"] for n in GRAPH["nodes"] if n["type"]=="chunk"})
all_doms = sorted({n["domain"]   for n in GRAPH["nodes"] if n["type"]=="chunk"})

sel_cats = st.sidebar.multiselect("Reference Category", all_cats, default=all_cats)
sel_doms = st.sidebar.multiselect("Reference Domain",   all_doms, default=all_doms)

# ---- build HTML with injected data ----
template = Path("graph_template.html").read_text(encoding="utf-8")
html = template.replace("{{GRAPH_DATA}}", json.dumps(GRAPH)\
                ).replace("{{FILTERS}}", json.dumps({"categories":sel_cats,
                                                     "domains":sel_doms,
                                                     "query":""}))

components.html(html, height=800, scrolling=False)
