## Project Overview

This repository contains the MCP Sentiment project, which provides sentiment analysis using Gradio and Hugging Face Spaces.

### Features

- Sentiment analysis via a web interface
- Easy deployment to Hugging Face Spaces
- Example usage and API documentation

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://huggingface.co/spaces/stevenloaiza/mcp-sentiment
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run locally:
    ```bash
    python app.py
    ```

## License

See [LICENSE](./LICENSE) for details.

## Sync with HF Repo

Error Syncing repo with HF due to png files.

-------------------------------------------------------------------------
remote: Your push was rejected because it contains binary files.
remote: Please use https://git-lfs.github.com/ to store binary files.
remote: See also: https://hf.co/docs/hub/repositories-getting-started#terminal
remote: 
remote: Offending files:
remote:   - mcp_server.png (ref: refs/heads/feature/gradio_mcp)
remote: -------------------------------------------------------------------------
To https://huggingface.co/spaces/stevenloaiza/mcp-sentiment

### How to Fix Binary File Issues

Hugging Face repositories do not support direct storage of binary files (such as `.png` images) in the main repository. To resolve this:

1. **Install Git LFS**  
    Download and install Git Large File Storage (LFS):  
    [https://git-lfs.github.com/](https://git-lfs.github.com/)

2. **Track Binary Files**  
    Run the following commands in your repository root:
    ```bash
    git lfs install
    git lfs track "*.png"
    git add .gitattributes
    git add mcp_server.png
    git commit -m "Track PNG files with Git LFS"
    ```

3. **Push Again**  
    Push your changes:
    ```bash
    git push
    ```

For more details, see the [Hugging Face documentation](https://hf.co/docs/hub/repositories-getting-started#terminal).