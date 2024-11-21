
# Audio Transcription with Whisper

This project demonstrates how to use OpenAI's Whisper library for transcribing audio into text. The provided script includes a `Transcription` class that initializes a Whisper model and transcribes audio waveforms.

## Features

- Supports multiple Whisper model types (e.g., `base`, `small`, `medium`, `large`).
- Converts PyTorch tensors to NumPy arrays for compatibility.
- Processes audio waveforms and returns transcription text.

---

## Installation

### Prerequisites

Ensure you have Python 3.8 or higher installed on your system.

### Install Required Libraries

Install the necessary libraries using pip:

```bash
pip install whisper
```

---

## Usage

1. **Load the Script**

   Save the script below as `whisper_transcription.py`:

   ```python
   import whisper

   class Transcription:
       def __init__(self, modelType="base"):
           # Load the Whisper model
           self.model = whisper.load_model(modelType)
        
       def transcript(self, waveform, sample_rate):
           # Convert to numpy array as Whisper requires numpy array input
           audio_numpy = waveform.squeeze().numpy()

           # Transcribe the audio using Whisper
           result = self.model.transcribe(audio_numpy)
           transcription = result['text']
           return transcription
   ```

2. **Run the Script**

   - Initialize the `Transcription` class with the desired model type.
   - Pass an audio waveform and its sample rate to the `transcript` method.

   Example:

   ```python
   import torch
   from whisper_transcription import Transcription

   # Example audio waveform (PyTorch tensor)
   waveform = torch.randn(1, 16000)  # Simulated 1-second audio at 16kHz
   sample_rate = 16000

   # Initialize the transcription model
   transcriber = Transcription(modelType="base")

   # Transcribe the audio
   transcription = transcriber.transcript(waveform, sample_rate)
   print("Transcription:", transcription)
   ```

3. **Output**

   The script will output the transcription of the provided audio waveform.

---

## Notes

- Ensure the input waveform is a PyTorch tensor and matches the sample rate required by the model.
- Use a higher-tier Whisper model for improved transcription accuracy.
- The script assumes audio preprocessing (e.g., resampling) has been handled.

---

## License

This project is licensed under the MIT License. Please refer to the `LICENSE` file for details.