import gradio as gr

def greet(name):
    return f"Halo {name}! CI/CD GitHub Actions & Hugging Face berhasil!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
if __name__ == "__main__":
    demo.launch()