from Utils.extractAudio import extract_audio
from Utils.SplitAudio import AudioSplit
from Utils.speech_recognition import AudioToLang
import csv
import argparse
from datetime import timedelta

def model(input_file):
    
    extract_audio(input_file)
    chunk_len = AudioSplit("Data/Processed/output.wav")
    #chunk_len = 16
    start_time = timedelta(hours = 0, minutes = 0, seconds = 0)
    output = []
    for i in range(chunk_len):
        chunk_path = "Data/Processed/chunk{}.wav".format(i)
        try:
            lang = AudioToLang(chunk_path)
        except Exception as e:
            lang = 6
            print("Empty chunk :", i, e )
        
        deltatime = timedelta(seconds = 20)
        end_time = start_time + deltatime
        timestamp = str(start_time) + "-" + str(end_time)
        start_time = start_time + deltatime
        arr = [input_file, timestamp, lang]
        output.append(arr)
        head = ["File Name","TimeStamp","Language"]
        
    with open("Data/Output/output.csv", 'w+', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(head)
        for arr in output:
            wr.writerow(arr)

    print("Saved the output file")


    """for i, chunk in enumerate(split_audio):
        # chunk_name = "Data/Processed/chunk{0}.wav".format(i)
        # print ("exporting", chunk_name)
        # chunk.export(chunk_name, format="wav")
        lang, score = AudioToLang(chunk)
        print(lang, score)"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add Arguments')
    parser.add_argument('-i', '--input',type=str,
                        help='Input Video Path')
                  
    args = parser.parse_args()
    input_file = args.input
    model(input_file)
    
