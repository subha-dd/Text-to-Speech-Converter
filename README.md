# 🗣️ Text-to-Speech (TTS) Converter with Voice Style & Language Selection

This project is a **Text-to-Speech (TTS)** converter built in **Jupyter Notebook**, which takes input text and converts it into speech using pre-trained models from **Hugging Face Transformers**. Users can choose different voice styles such as **male/female** and **multiple languages** for a more personalized and multilingual audio output experience.

---

## 🎯 Features

- 🔤 Convert custom input text to speech audio
- 👨‍🦰👩‍🦰 Choose between male and female voices (if supported by the model)
- 🌐 Support for multiple languages (like English, French, Hindi, etc.)
- 🤖 Uses pre-trained TTS models from [Hugging Face 🤗](https://huggingface.co)
- 💻 Easy-to-use Jupyter Notebook interface
- 🔊 Outputs downloadable `.wav` or `.mp3` files

---

## 🧰 Technologies & Libraries

- Python 3.x
- Jupyter Notebook
- Hugging Face `transformers` and `datasets`
- `TTS` by [coqui.ai](https://github.com/coqui-ai/TTS) or similar
- `IPython.display.Audio` (for audio playback)
- `gTTS` (for fallback in some cases)
- `torchaudio` or `pydub` (for audio handling)

---

##🧠 How It Works
-The project loads a pre-trained TTS model (Edge tts model)
-Text is tokenized and processed
=Model outputs waveform
-Waveform is saved as .wav and optionally played inline

---

🌍 Supported Languages & Voices
Voice availability depends on the selected model.

✅ English (US, UK)

✅ French

✅ Hindi

✅ German

✅ More


