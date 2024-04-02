import os
import argparse
import time
from datetime import timedelta
import whisper

# Define a constant for supported file formats
# Define a constant for supported file formats
SUPPORTED_FORMATS = ['.mp3', '.mp4', '.m4a', '.ogg', '.mkv']

def transcribe_audio(input_path, model_size, output_format='srt', language='pt'):
    """
    Transcribe an audio or video file using Whisper.
    """
    
    start_time = time.time()
    print(f"Loading Whisper model '{model_size}'...")
    model = whisper.load_model(model_size)
    
    print(f"Transcribing in '{language}'... This may take some time depending on the length of the audio.")
    options = {"language": language}
    
    # Handle .mkv files
    if input_path.endswith('.mkv'):
        # Temporary audio file path
        temp_audio_path = 'temp.wav'
        
        # Extract audio from the .mkv file using ffmpeg
        os.system(f"ffmpeg -i {input_path} -vn -acodec pcm_s16le -ar 44100 -ac 2 {temp_audio_path}")
        
        # Transcribe the extracted audio
        result = model.transcribe(temp_audio_path, **options)
    else:
        result = model.transcribe(input_path, **options)

    if output_format == 'srt':
        with open(input_path + '.srt', 'w', encoding='utf-8') as file:
            for i, segment in enumerate(result['segments']):
                start = timedelta(seconds=segment['start'])
                end = timedelta(seconds=segment['end'])
                file.write(f"{i+1}\n")
                file.write(f"{str(start)} --> {str(end)}\n")
                file.write(f"{segment['text']}\n\n")
    else:
        with open(input_path + '.txt', 'w', encoding='utf-8') as file:
            for segment in result['segments']:
                file.write(f"{segment['text']} ")

    print(f"Transcription completed in {time.time() - start_time:.2f} seconds.")

def transcribe_directory(directory_path, model_size, output_format, language):
    """
    Transcribe all audio and video files in a directory using Whisper.
    """
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1].lower() in SUPPORTED_FORMATS:
            transcribe_audio(file_path, model_size, output_format, language)

def main():
    """
    Main function to Transcribe an audio or video file or a directory of files using Whisper.
    """
    parser = argparse.ArgumentParser(description="Transcribe audio and video files.")
    parser.add_argument("file_path", help="Path to the input audio or video file or directory.")
    parser.add_argument("--output-format", choices=['srt', 'txt'], default='srt', help="Output format for the transcription.")
    parser.add_argument("--model", choices=['tiny', 'base', 'small', 'medium', 'large'], default='small', help="Whisper model size. Larger models may improve accuracy but take longer to process. 'small' is the default and recommended for a balance between speed and accuracy.")
    parser.add_argument("--language", default='pt', help="Language code for the transcription. Default is 'pt' for Portuguese.")

    args = parser.parse_args()

    if not os.path.exists(args.file_path):
        print("Error: The specified path does not exist.")
        return

    if os.path.isdir(args.file_path):
        transcribe_directory(args.file_path, args.model, args.output_format, args.language)
    elif os.path.isfile(args.file_path):
        file_extension = os.path.splitext(args.file_path)[1].lower()
        if file_extension not in SUPPORTED_FORMATS:
            print(f"Unsupported file format: {file_extension}. Supported formats are: {', '.join(SUPPORTED_FORMATS)}.")
            return
        transcribe_audio(args.file_path, args.model, args.output_format, args.language)
        print(f"Output file: {args.file_path}.{args.output_format}")
    else:
        print("Error: The specified path is neither a file nor a directory.")

if __name__ == "__main__":
    main()
