import gradio as gr

def letter_counter(word:str, letter:str) -> int:
    """Counts the occurrences of a letter in a word."""
    return word.lower().count(letter.lower())

# Create the Gradio interface
demo = gr.Interface(
    fn=letter_counter,
    inputs=[
        gr.Textbox(label="Word", placeholder="Enter a word"),
        gr.Textbox(label="Letter", placeholder="Enter a letter")
    ],
    outputs=gr.Number(label="Count of Letter"),
    title="Letter Counter",
    description="This app counts how many times a specific letter appears in a given word."
)

# Launch the Gradio app and the MCP server
if __name__ == "__main__":
    demo.launch(mcp_server=True)
    