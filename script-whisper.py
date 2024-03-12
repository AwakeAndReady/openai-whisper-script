# To install got to: https://github.com/openai/whisper or follow the README

import whisper
from whisper.utils import get_writer
import time
import argparse  # For handling command-line arguments

def main():
    # Setting up the argument parser
    parser = argparse.ArgumentParser(description="Transcribe audio files with Whisper")

    # Adding arguments for input file, output directory, model type, language, and task
    parser.add_argument("input_filepath", type=str, help="Path to the input audio file")
    parser.add_argument("-o", "--output_dir", type=str, default="./output/", help="Directory to save the output file(s)")
    parser.add_argument("-m", "--model", type=str, default="tiny", help="Model type for Whisper (e.g., 'tiny')")
    parser.add_argument("-l", "--language", type=str, default="en", help="Language for transcription (e.g., 'en')")
    parser.add_argument("-t", "--task", type=str, default="transcribe", help="Task for the model (e.g., 'transcribe')")

    # Parsing the arguments provided by the user
    args = parser.parse_args()

    # Loading the Whisper model specified by the user (or the default)
    model = whisper.load_model(args.model)
    options = {"language": args.language, "task": args.task}

    # Starting the transcription process and measuring the time taken
    start_time = time.time()
    result = model.transcribe(args.input_filepath, **options)  # Actual transcription
    end_time = time.time()

    # Calculating and displaying the time taken for transcription
    elapsed_time = end_time - start_time
    print(f"Transcription took {elapsed_time:.2f} seconds.")

    # Setting up options for the writer utilities (See documentation link provided)
    write_options = {"max_line_width": 50, "max_line_count": 2, "highlight_words": False}

    # Getting a VTT writer and writing the transcription to an output file
    vtt_writer = get_writer("vtt", args.output_dir)
    vtt_writer(result, args.input_filepath, write_options)

    # Getting a TXT writer and writing the transcription to an output file
    txt_writer = get_writer("txt", args.output_dir)
    txt_writer(result, args.input_filepath, {})

# This ensuresult that the main function is only executed when this script is run directly
if __name__ == "__main__":
    main()

