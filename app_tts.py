import asyncio
import edge_tts
import tempfile
import gradio as gr

# get all the voices
async def extract_voices():
  voices = await edge_tts.list_voices()
  return {f"{v['ShortName']} - {v['Locale']} ({v['Gender']})": v['ShortName'] for v in voices}


# text to speech fuction
async def text_to_speech(text,voice,rate,pitch):
  if not text.strip():
    return None, gr.Warning("Please enter a text to convert.")
  if not voice:
    return None, gr.Warning("Please select a voice.")
  
  voice_short_name = voice.split(" - ")[0]
  rate_str = f"{rate:+d}%"
  pitch_str = f"{pitch:+d}Hz"
  
  communicate = edge_tts.Communicate(text,voice_short_name,rate=rate_str,pitch=pitch_str)
  with tempfile.NamedTemporaryFile(delete=False,suffix=".mp3") as tmp_file:
    tmp_path = tmp_file.name
    await communicate.save(tmp_path)
  
  return tmp_path,None

# gradio interface
def gradio_interface(text,voice,rate,pitch):
  audio,warning = asyncio.run(text_to_speech(text,voice,rate,pitch))
  return audio,warning

# gradio application
async def gradio_app():
  
  voices = await extract_voices()
  
  app = gr.Interface(
    fn = gradio_interface,
    inputs=[
      gr.Textbox(label="Input Text",lines=10),
      gr.Dropdown(choices = [""] + list(voices.keys()),label="Select Voice",value=""),
      gr.Slider(minimum=-50,maximum=50,value=0,label="Speech Rate (%)",step=1),
      gr.Slider(minimum=-20,maximum=20,value=0,label="Pitch (Hz)",step=1)
    ],
    outputs=[
      gr.Audio(label="Generated Audio",type="filepath"),
      gr.Markdown(label='Warning',visible=False)
    ],
    title="Edge TTS Text-to-Speech",
      description="Convert text to speech using Microsoft Edge TTS Model.",
        analytics_enabled=False,
        allow_flagging=False,
        live=False
  )
  return app
  
if __name__ == "__main__":
  demo = asyncio.run(gradio_app())
  demo.launch()