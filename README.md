# Automating Second Language Learner Error Analysis
UBC BREB: **H24-00741**  
Ethics approval certificate is attached.

## Files in this repo:
*Note: files containing participant data will not be available on Github and instead submitted on Canvas.*
1. **finetuning.py**  
This is a copy of the notebook that finetunes the LLM. I used Google Colab for this file because I needed the GPUs. The final model was uploaded [here to HuggingFace](https://huggingface.co/audribean/happy-gec/tree/main)
2. **happy.py**  
The happy file formats the original essays to be properly formatted and spaced, then calls an instance of the model from HuggingFace to correct them.
3. **parse.ipynb**    
parse.ipynb counts error type frequencies from M2 file formats and attaches them to the respective participant.
4. **graphs.ipynb**  
This plots comparisons of the results from results.csv and true_results.csv

## Files submitted on Canvas
*Participants are represented by a code, which matches them across these documents.*
1. **original_essays**  
These are the original essays from participants with errors as-is, including spacing.
2. **spaced_formatted_essays**  
These are the formatted original essays output by happy.py
3. **hand_corrected_m2**  
These are the manual annotations of the original essays, in M2 format. 
4. **model_corrected_txt**  
These are the corrected versions of the essays output by the model in happy.py in text format. These were generated from the original and the text model-corrected essays.
6. **model_corrected_m2**  
These are the model annotations of the original essays by ERRANT, in M2 format.
7. **scores**  
This contains the precision, recall, and F0.5 scores for each essay alongside overall averages. It also contains the bash commands used to activate the errant env, evaluate the model's performance against the manual annotations, and create the files in model_corrected_m2.
8. **participant_data**  
This provides information on the participants who are represented by a code.
9. **model_results**
This displays the error frequency table created by parse.ipynb for model_corrected_m2
10. **manual_results**
This displays the error frequency table created by parse.ipynb for manual_corrected_m2

## ERRANT folder
This is a clone of the ERRANT repo from the papers below, found [here](https://github.com/chrisjbryant/errant).

Christopher Bryant, Mariano Felice, and Ted Briscoe. 2017. Automatic annotation and evaluation of error types for grammatical error correction. In Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). Vancouver, Canada.

Mariano Felice, Christopher Bryant, and Ted Briscoe. 2016. Automatic extraction of learner errors in ESL sentences using linguistically enhanced alignments. In Proceedings of COLING 2016, the 26th International Conference on Computational Linguistics: Technical Papers. Osaka, Japan.
