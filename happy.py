from happytransformer import HappyTextToText, TTSettings
import re

essays = [620, 702, 718, 798, 775, 783, 784, 797, 799, 801]

# GEC model can be found here https://huggingface.co/audribean/happy-gec/tree/main
happy_tt = HappyTextToText("T5", "audribean/happy-gec")
args = TTSettings(num_beams=5, min_length=1)

# Format essays for processing
# for e in essays:
#     input_txt = f'essays/{e}.txt'
#     output_txt = f'spaced/{e}.txt'
#     separate_sentences(input_txt, output_txt)

# Run GEC on each line of each essay
for e in essays:
    input_file = f'spaced/{e}.txt'
    output_file = f'corrected/{e}.txt'
    output_content = ''
    with open(input_file, 'r') as i_file:
        for line in i_file:
            # Generate_text adapted from https://huggingface.co/vennify/t5-base-grammar-correction
            # Add the prefix "grammar: " before each input 
            result = happy_tt.generate_text(f"grammar: {line}", args=args)
            with open(output_file, 'a') as o_file:
                o_file.write(result.text + '\n')
        o_file.close()
    i_file.close()    

# To separate sentences by punctuation
def separate_sentences(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()

    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', content)
    new_content = '\n'.join(sentences)

    with open(output_file, 'w') as f:
        f.write(new_content)