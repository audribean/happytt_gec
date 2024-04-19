# Automating Second Language Learner Error Analysis
UBC BREB: **H24-00741**  
Ethics approval certificate is attached.

## Files in the happy folder:
*Note: files containing participant data will not be available on Github and instead submitted on Canvas.*
1. **essays**  
These are the original essays from participants with errors as-is, including spacing.
2. **finetuning.py**  
This is a copy of the notebook that finetunes the LLM. I used Google Colab for this file because I needed the GPUs. The final model was uploaded [here to HuggingFace](https://huggingface.co/audribean/happy-gec/tree/main)
3. **happy.py, spaced, corrected**  
The happy file formats the original essays to be properly formatted and spaced, then calls an instance of the model from HuggingFace to correct them. The final outputs are in the corrected folder.
4. **errant.txt, m2, hand-cor**  
The errant file contains the bash commands used to run the original and corrected essays through ERRANT. The annotation outputs in M2 format are saved in the m2 file. The files in hand-cor are the manual annotations of the original essays, also in M2 format.
5. **parse.ipynb, data.csv, results.csv, true_results.csv**  
data.csv contains information about the participants. parse.ipynb counts error type frequencies from M2 file formats and attaches them to the respective participant. The model annotation results are output to results.csv and the manual annotation results are output to true_results.csv
6. **errant.txt, scores.txt**  
The errant file contains the command used to evaluate the model's performance against the manual annotations. These scores were saved to scores.txt, with averages manually calculated at the bottom.
7. **graphs.ipynb**  
This plots comparisons of the results from results.csv and true_results.csv

## ERRANT folder
This is a clone of the ERRANT repo from the papers below, found [here](https://github.com/chrisjbryant/errant).

Christopher Bryant, Mariano Felice, and Ted Briscoe. 2017. Automatic annotation and evaluation of error types for grammatical error correction. In Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). Vancouver, Canada.

Mariano Felice, Christopher Bryant, and Ted Briscoe. 2016. Automatic extraction of learner errors in ESL sentences using linguistically enhanced alignments. In Proceedings of COLING 2016, the 26th International Conference on Computational Linguistics: Technical Papers. Osaka, Japan.