# VoiceContentAI

[![Twitter Follow](https://img.shields.io/twitter/follow/Luc_AI_Insights?style=social)](https://twitter.com/Luc_AI_Insights)


## Installation

1. Clone the repository:

```bash
git clone https://github.com/luc-pimentel/VoiceContentAI.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Create a `.env` file in the root directory and add your API keys and custom prompts:

```
OPENAI_API_KEY=your_openai_api_key
WHISPER_PROMPT=your_whisper_prompt
DRAFT_CORRECTOR_PROMPT=your_draft_corrector_prompt
ANTHROPIC_API_KEY=your_anthropic_api_key
```

2. Run the Streamlit app:

```bash
python -m streamlit run Home.py
```

3. Follow the instructions in the app to record your voice, get a rough transcript, and refine it with AI.

## Customization

You can customize the prompts and API keys by modifying the corresponding variables in the `.env` file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
