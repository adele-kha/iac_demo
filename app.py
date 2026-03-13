
import gradio as gr
import json

def load_data():
    with open("prompts.json", "r") as f:
        return json.load(f)

def render():
    data = load_data()
    return json.dumps(data, indent=2)

with gr.Blocks(title="IaC Demo") as demo:
    gr.Markdown("## 📄 data.json viewer")
    gr.Markdown("This content is driven by `data.json`. Merge a PR to see it update.")
    output = gr.Code(value=render(), language="json", interactive=False)
    gr.Button("🔄 Reload").click(fn=render, outputs=output)

demo.launch()