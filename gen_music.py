import os
import argparse

def get_music_files(directory):
    # Supported music file extensions
    music_extensions = ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a']
    
    # Initialize an empty list to store music file paths
    music_files = []
    
    # Traverse the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file has a supported music extension
            if os.path.splitext(file)[1].lower() in music_extensions:
                # Append the full path of the music file to the list
                music_files.append(os.path.join(root, file))
    
    return music_files

def main():
    # Define the argument parser
    parser = argparse.ArgumentParser(description='List all music files in a directory')
    parser.add_argument('--directory', required=True, help='Directory to search for music files')
    parser.add_argument('--output_file', required=False, default='music_files.txt', help='Output file to write the list of music files')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Get the list of music files
    music_files = get_music_files(args.directory)
    
    # Write the list of music files to the output file
    with open(args.output_file, "w") as f:
        for file_path in music_files:
            f.write(file_path + "\n")
    
    print(f"List of music files written to {args.output_file}")

if __name__ == "__main__":
    main()