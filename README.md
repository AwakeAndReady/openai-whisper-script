# Using Whisper by OpenAI on your own computer


This is how to setup and use Whisper by OpenAI to perform ASR (Artificial Speech Recognition) locally on your machine.
It makes you capable of transcribing even larger audio or video files into text files (.txt) or subtitle files (e.g. .vtt) for free
without uploading it to external online services.

BUT: The quality of the transcription can vary. Therefore, it is recommended to repeat the transcription in case of doubt and compare the results. If necessary, optimization can be done using the "temperature" parameter (to be implemented in the script).

## Getting started

1. To avoid clutter in your system: create a python virtual environment (short venv) (highly recommended)
One way to do this is to type:

```
python3 -m venv openai-whisper
```

2. Then activate virtual environment by:

```
source openai-whisper/bin/activate
``` 

3. Install all necessary packages according to https://github.com/openai/whisper

```
pip install -U openai-whisper  
```

5. Put audio or video files that you want to process into the 'input' folder and test the script with the tiny model:

```
script-whisper.py input/Minute-Rice.m4a -o output/ -m "tiny" -l "en" -t "transcribe"
```

The tiny-model will be downloaded the first time you use it. Larger models may take some time to download. Please be also aware that large models require up to 10 Gb of RAM for the "large" model. The newest and most capable model is "large-v2" (as of  Oktober 19th,2023).

6. Check your output folder for results

To show help for possible options, type:

```
python script-whisper.py -h
```

If you feel uncomfortable with these instructions, please do not hesitate to ask ChatGPT or contact someone experienced in this.

More Information about Whisper, see:

- [OpenAI Whisper Research Overview](https://openai.com/research/whisper)
- [Whisper on OpenAI's GitHub Repository](https://github.com/openai/whisper)
- [Whisper Base Model on Hugging Face](https://huggingface.co/openai/whisper-base)

