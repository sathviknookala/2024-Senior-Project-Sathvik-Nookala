import pandas as pd

df = pd.read_csv('debate_text.csv')

text_str = ''
for t in df['0'].values.flatten():
  text_str = text_str + t + ' '

speakers = ["WELKER", "TRUMP", "BIDEN", "MODERATOR"]

# Initialize a dictionary to hold each speaker's statements.
speaker_statements = {speaker: "" for speaker in speakers}

# Helper function to find the next speaker's position in the text.
def find_next_speaker_position(text, current_pos, speakers):
    next_speaker_pos = len(text)
    next_speaker_name = None
    for speaker in speakers:
        pos = text.find(speaker + ":", current_pos)
        if pos != -1 and pos < next_speaker_pos:
            next_speaker_pos = pos
            next_speaker_name = speaker
    return next_speaker_pos, next_speaker_name

# Parse the text to separate it by speaker.
current_pos = 0
while current_pos < len(text_str):
    next_speaker_pos, next_speaker_name = find_next_speaker_position(text_str, current_pos, speakers)
    if next_speaker_name:
        # Extract the statement for the current speaker.
        end_of_statement_pos = find_next_speaker_position(text_str, next_speaker_pos + len(next_speaker_name) + 1, speakers)[0]
        statement = text_str[next_speaker_pos + len(next_speaker_name) + 1:end_of_statement_pos].strip()
        speaker_statements[next_speaker_name] += " " + statement
        current_pos = end_of_statement_pos
    else:
        break  

speaker_df = pd.DataFrame(speaker_statements, index=[0])

trump_text = speaker_df['TRUMP'].iloc[0]
biden_text = speaker_df['BIDEN'].iloc[0]

with open('trump_text.txt', 'w') as file:
    file.write(trump_text)


