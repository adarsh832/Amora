# 💖 Amora 💬 - Love in the Air

A sweet and loving chatbot built with Gradio that simulates a personalized conversation with your romantic partner — be it a girlfriend or boyfriend! Customize your partner’s name and nature, and chat with a warm, affectionate AI that responds with love and emojis.

---

## Features

* Choose your partner type: Girlfriend or Boyfriend
* Name your virtual love
* Describe their personality/nature (e.g., caring, bold, sweet)
* Chat with a responsive AI that mimics your partner’s style with loving messages and emojis
* Clean, romantic UI with pastel gradient background and pink-themed chat interface
* Clear chat functionality to start fresh anytime

---

## How to Use

1. **Setup your partner**

   * Select if your partner is a Girlfriend or Boyfriend.
   * Enter their name (e.g., Lily, Alex).
   * Describe their nature/personality (e.g., sweet, caring, bold).
   * Click **Start Chat**.

2. **Start chatting**

   * Type your message to your partner in the message box.
   * Press Enter or click send to get loving responses.
   * Clear the chat anytime with the **Clear Chat** button.

---

## Installation

Make sure you have Python installed (preferably 3.8+).

Install dependencies using pip:

```bash
pip install gradio openai
```

> Note: This example assumes you have an API wrapper or environment configured to use the LLM (`model.chat.completions.create`) for generating responses.

---

## Code Overview

* **setup()**: Initializes partner details and toggles UI visibility.
* **gen()**: Generates AI responses by sending partner details and prompt to the language model.
* **respond()**: Manages conversation history and calls `gen()` to get AI replies.
* **Gradio UI**: Two main screens — setup and chat, styled with custom CSS for a romantic feel.

---

## Customization

* Change `partner_type`, `partner_name`, and `partner_nature` to create different personality styles.
* Adjust CSS inside the `gr.Blocks` context for personalized UI themes.
* Extend the prompt in `gen()` to include more personality traits or conversational style.

---


