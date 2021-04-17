import moviepy.editor as mp
import argparse
import os
# Insert Local Video File Path
#video_path = "/Users/zaidbhat/Desktop/TAMU-Courses/SE_project/Data/S2/Videos"


def extract_audio(video_path):
    
    
    audio_path = video_path
    audio_path = audio_path.rsplit( ".", 1 )[ 0 ] +'.wav'
    
    clip = mp.VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)

def main():

    #Argument Parser to take inputs from user
    parser = argparse.ArgumentParser(description='Add Arguments')
    parser.add_argument('-i', '--input',type=str,
                        help='Input Video Path')
                  
    args = parser.parse_args()
    input = args.input
    extract_audio(input)
                        
if __name__ == "__main__":
    main()

