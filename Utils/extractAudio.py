import moviepy.editor as mp
import argparse
import os
# Insert Local Video File Path
# global video_path = "Data/Input/sampleVideo.mp4"
# global audio_path = "Data/Processed"

#/Users/zaidbhat/Desktop/TAMU-Courses/SE_project/Data/S2/Videos/1.asf, Data/Input/sampleVideo.mp4
def extract_audio(video_path,\
                    audio_path = "Data/Processed/"):
    path = os.getcwd() + '/Data/'
    path_processed = path + 'Processed'
    dirs = os.listdir( path )
    if 'Processed' not in dirs:
        os.mkdir(path_processed)


    
    
    
    # audio_path = video_path
    #audio_path = audio_path.rsplit( ".", 1 )[ 0 ] +'.wav'
    
    clip = mp.VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path + "output.wav")
"""
def main():

    #Argument Parser to take inputs from user
    parser = argparse.ArgumentParser(description='Add Arguments')
    parser.add_argument('-i', '--input',type=str,
                        help='Input Video Path')
                  
    args = parser.parse_args()
    input = args.input
    extract_audio(input)
                        
if __name__ == "__main__":
    main()"""

