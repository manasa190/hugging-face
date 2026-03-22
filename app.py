import gradio as gr
import random

def greet(name):
    funny_responses = [
    f'"Oh {name}, like semicolons in code, you pause but never truly stop ;)"',
    f'"{name}, you bloom like WiFi signals… strong near router, weak in exams 🌸📶"',
    f'"In the poetry of life, {name}, you are both the bug and the feature 💀✨"',
    f'"{name}, like unfinished assignments, you remain… pending yet powerful 😌📚"',
    f'"Oh dear {name}, your dreams fly high… but your sleep flies higher 😴🚀"',
    f'"{name}, in this universe of chaos, you still forgot to save your code 😭🌌"',
    f'"Like the moon and deadlines, {name}, you appear only at the last moment 🌙⏳"',
    f'"{name}, your life is a poem… unfortunately written in runtime errors 💻💀"',
    f'"Oh {name}, you shine like stars… but disappear during exams ✨📉"',
    f'"In the rhythm of life, {name}, you dance… mostly away from responsibilities 💃😂"',
    f'"{name}, your thoughts are deep… but your battery is always 2% 🔋😔"',
    f'"Oh {name}, like Python indentation, one mistake and everything collapses 🐍💀"',
    ]
    return random.choice(funny_responses)

with gr.Blocks(
    theme=gr.themes.Soft(primary_hue="pink")
) as demo:

    # 🎨 Pastel Styling
    gr.Markdown("""
    <style>
    body, .gradio-container {
        background: #fff6f9 !important;
    }

    .gradio-container > div {
        background: #ffe4ec !important;
        border-radius: 16px;
        padding: 20px;
    }

    textarea, input {
        background-color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid #ffd6e0 !important;
    }

    button {
        background: linear-gradient(90deg, #ffb6c1, #ffc0cb) !important;
        color: #6b2140 !important;
        border-radius: 12px !important;
        border: none !important;
        font-weight: bold;
        transition: 0.3s;
    }

    button:hover {
        background: linear-gradient(90deg, #ff9eb5, #ffb6c1) !important;
        transform: scale(1.05);
    }

    label {
        color: #b56576 !important;
        font-weight: 600;
    }

    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
    """)

    # 💗 Heading
    gr.Markdown("""
    <h1 style='text-align:center; color:#ff8fab; animation: fadeIn 2s;'>
    💗 My App  💗
    </h1>
    <p style='text-align:center; color:#a64d79;'>
    Simple app ✨
    </p>
    """)

    # 📦 Layout
    with gr.Row():
        name = gr.Textbox(label="Enter your name", placeholder="Type here...")
        output = gr.Textbox(label="Output")

    # 🚀 Button
    submit = gr.Button("🚀 Make me laugh")

    submit.click(greet, inputs=name, outputs=output)

    # 💕 Footer
    gr.Markdown("""
    <p style='text-align:center; color:#a64d79; margin-top:20px;'>
    Made with 💖 (and a little chaos 😌) by ME
    </p>
    """)

demo.launch()
