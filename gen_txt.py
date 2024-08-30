import argparse

# Define the argument parser
parser = argparse.ArgumentParser(description='Generate file paths for audio segments')
parser.add_argument('--base_dir', required=True, help='Base directory for the audio files')
parser.add_argument('--output_file', required=True, help='Output file to write the file paths')

# Parse the arguments
args = parser.parse_args()

# Define the file name format
file_name_format = "segment_{}_{}-{}.mp3"

# Open the output file in write mode
with open(args.output_file, "w") as f:
    # Initialize the start and end times
    start_time = 0
    end_time = 10000
    
    # Loop over the segment numbers from 0 to 720
    for segment in range(1, 361):
        # Create the file path
        file_path = args.base_dir + file_name_format.format(segment, start_time, end_time)
        # Write the file path to the text file
        f.write(file_path + "\n")
        
        # Update the start and end times for the next segment
        start_time = end_time
        end_time += 5000

print(f"File paths written to {args.output_file}")