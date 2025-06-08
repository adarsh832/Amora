import gradio as gr
import time
from openai import OpenAI
model = OpenAI(api_key="your-api-key-here")



partner_type = "GF"
partner_name = "Love"
partner_nature = "sweet"

def gen(prompt):

    ans = model.chat.completions.create(
        messages=[
            {"role": "system", "content": f"You are a {partner_nature} {partner_type} named {partner_name}. Respond lovingly. add some emojies"},
            {"role": "user", "content": prompt}
        ],
        model="gpt-4o-mini"
    )
    output = ans.choices[0].message.content
    print(f"Bot: {output}")
    return output

def setup(partner, name, nature):
    global partner_type, partner_name, partner_nature
    partner_type = partner
    partner_name = name.strip().capitalize() or "Love"
    partner_nature = nature.lower()
    # Show chat UI and hide setup UI
    return gr.update(visible=True), gr.update(visible=False)

def respond(message, chat_history):
    chat_history.append({"role": "user", "content": message})
    bot_message = gen(message)
    chat_history.append({"role": "assistant", "content": bot_message})
    time.sleep(0.5)
    return "", chat_history

with gr.Blocks(css="""
    body {
        background: linear-gradient(145deg, #ffdde1, #ee9ca7);
        font-family: 'Segoe UI', sans-serif;
        display: flex;
        justify-content: center;
        padding: 40px 10px;
    }
    .gr-block.gr-box {
        background-color: white !important;
        border-radius: 20px !important;
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
    }
    .gr-chatbox {
        background: rgba(255, 255, 255, 0.9) !important;
        border-radius: 12px !important;
        border: 1px solid #ffc0cb !important;
    }
    textarea {
        background-color: #fff5f8 !important;
        border: 2px solid #ff9eaf !important;
        border-radius: 10px !important;
        color: #b3005e !important;
        padding: 10px;
    }
    button {
        background-color: #ff66a3 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 10px !important;
        padding: 8px 16px;
        margin-top: 10px;
        transition: 0.3s;
    }
    button:hover {
        background-color: #ff3385 !important;
        transform: scale(1.05);
    }
    .gr-markdown h1 {
        color: #b3005e;
        text-align: center;
        margin-bottom: 20px;
    .gen{
        font-size: 18px !important;
    } 
        
""") as demo:

    gr.Markdown("## 💖 Amora 💬 - Love in the air")

    setup_ui = gr.Column(elem_id="setup-ui", visible=True)
    with setup_ui:
        partner = gr.Radio(["Girlfriend", "Boyfriend"], label="Choose your partner 💑", value="Girlfriend",)
        name = gr.Textbox(label="Name your love 💗", placeholder="e.g., Lily, Alex",elem_id="gen")
        nature = gr.Textbox(label="What’s their nature?", placeholder="e.g., Caring, Bold")
        start_btn = gr.Button("Start Chat 💌")

    chat_ui = gr.Column(elem_id="chat-ui", visible=False)
    with chat_ui:
        chatbot = gr.Chatbot(label="💬 LoveBot", type="messages")
        msg = gr.Textbox(placeholder="Send your love note...", label="💗 Your Message")
        clear = gr.ClearButton([msg, chatbot], value="💔 Clear Chat")

    start_btn.click(setup, [partner, name, nature], [chat_ui, setup_ui])
    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()
