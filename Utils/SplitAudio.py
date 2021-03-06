from pydub import AudioSegment
from pydub.utils import make_chunks

# myaudio = AudioSegment.from_file("C:/Users/marne/VS_programs/Sample.wav" , "wav") 
# chunk_length_ms = 20000 # pydub calculates in millisec
# chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of 20 sec

# #Export all of the individual chunks as wav files


# for i, chunk in enumerate(chunks):
#     chunk_name = "C:/Users/marne/VS_programs/chunk{0}.wav".format(i)
#     print ("exporting", chunk_name)
#     chunk.export(chunk_name, format="wav")


def AudioSplit(input_file, split_length = 20000):
    myaudio = AudioSegment.from_file(input_file , "wav") 
    chunk_length_ms = split_length # pydub calculates in millisec‘
    chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of 20 sec
    #print(type(chunks[0]))
    #return chunks

    #Export all of the individual chunks as wav files


    for i, chunk in enumerate(chunks):
        chunk_name = "Data/Processed/chunk{0}.wav".format(i)
        print ("exporting", chunk_name)
        chunk.export(chunk_name, format="wav")
    return len(chunks)
