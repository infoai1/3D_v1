import json, streamlit as st
import streamlit.components.v1 as components

# read your graph
with open("graph.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# build the standalone HTML page
html = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <style>
    html,body,#graph{{margin:0;width:100%;height:100%;background:#000;}}
  </style>
  <script src="https://cdn.jsdelivr.net/npm/3d-force-graph"></script>
</head>
<body>
  <div id="graph"></div>
  <script>
    const Graph = ForceGraph3D({{controlType:'orbit'}})(document.getElementById('graph'))
      .graphData({json.dumps(data)})
      .nodeLabel(d => d.text || d.label)
      .nodeAutoColorBy('type')
      .linkDirectionalParticles(2)
      .linkDirectionalParticleSpeed(0.005);
  </script>
</body>
</html>
"""

components.html(html, height=700, scrolling=False)
