from deepfilternet import DeepFilterNet

# Initialize the model
model = DeepFilterNet()

# Define the paths for input and output audio
input_audio_path = "path_to_your_input_audio.wav"
output_audio_path = "path_to_save_processed_audio.wav"

# Apply noise reduction
model.process_file(input_audio_path, output_audio_path)

print(f"Processed audio saved at: {output_audio_path}")
