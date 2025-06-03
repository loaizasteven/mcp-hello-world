import gradio as gr
from textblob import TextBlob

def sentiment_analysis(text:str) -> dict:
    """
    Perform sentiment analysis on the input text.
    
    Args:
        text (str): The input text to analyze.
    
    Returns:
        dict: A dictionary containing the polarity, assessment, and subjectivity of the text.
    """
    blob = TextBlob(text)
    return {
        "polarity": round(blob.sentiment.polarity, 2),
        "subjectivity": round(blob.sentiment.subjectivity, 2),
        "assessment": "Positive" if blob.sentiment.polarity > 0 else "Negative" if blob.sentiment.polarity < 0 else "Neutral"
    }


dmeo = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(label="Input Text", placeholder="Type your text here..."),
    outputs=gr.JSON(),
    title="Sentiment Analysis",
    description="This tool performs sentiment analysis on the input text and returns the polarity, subjectivity, and overall assessment (Positive, Negative, or Neutral)."
)


if __name__ == "__main__":
    dmeo.launch(mcp_server=True)
