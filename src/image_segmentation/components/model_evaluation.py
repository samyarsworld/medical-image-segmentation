# from datasets import load_from_disk
import torch
import pandas as pd
from tqdm import tqdm
import random

class ModelEvaluation:
    def __init__(self, config):
        self.root_dir = config["root_dir"]
        self.data_path = config["data_path"]
        # self.model_path = config["model_path"]
        # self.arguments_path = config["arguments_path"]
        self.metric_file_name = config["metric_file_name"]

        self.params = config["params"]

    
    def batch_generator(self, list_of_elements, batch_size):
        """
        Splits the dataset into smaller batches using generator to avoid loading the entire sequence into memory.
        This is called 'Lazy Evaluation'.
        
        args:
        list_of_elements: list
        batch_size: int
        """
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i : i + batch_size]

    
    def calculate_metric(self,
                         dataset,
                         metric,
                         model,
                         tokenizer,
                         batch_size=16,
                         device="cpu",
                         column_text="article",
                         column_summary="highlights"):
        """
        Computes the ROUGE score for the given dataset.
        
        args:
        dataset: Dataset
        metric: Metric
        model: Model
        tokenizer: Tokenizer
        batch_size: int
        device: str
        column_text: str
        column_summary: str
        """
        # Load the model and tokenizer
        # model = AutoModelForSeq2SeqLM.from_pretrained(self.model_path).to(device)
        # tokenizer = AutoTokenizer.from_pretrained(self.tokenizer_path)
        # article_batches = list(self.batch_generator(dataset[column_text], batch_size))
        # target_batches = list(self.batch_generator(dataset[column_summary], batch_size))

        # for article_batch, target_batch in tqdm(zip(article_batches, target_batches),
        #                                         total=len(article_batches)):
            
        #     inputs = tokenizer(
        #         article_batch,
        #         max_length=1024, 
        #         truncation=True,
        #         padding="max_length",
        #         return_tensors="pt"
        #     )
            
        #     summaries = model.generate(
        #         input_ids=inputs["input_ids"].to(device),
        #         attention_mask=inputs["attention_mask"].to(device), 
        #         length_penalty=0.8, num_beams=8, max_length=128
        #     )

            
        #     # Decode the generated texts 
        #     decoded_summaries = [
        #         tokenizer.decode(s, skip_special_tokens=True, clean_up_tokenization_spaces=True) for s in summaries
        #     ]      
            
        #     decoded_summaries = [d.replace("", " ") for d in decoded_summaries]
            
            
        #     metric.add_batch(predictions=decoded_summaries, references=target_batch)
            
        # #  Finally compute and return the ROUGE scores.
        # score = metric.compute()
        # return score


    def evaluate(self):
        """
        Evaluates the model on the test set.
        """
        # Device agnostic code
        # DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

        # # Load pretrained model and tokenizer
        # model = AutoModelForSeq2SeqLM.AutoModelForSeq2SeqLM.from_pretrained(self.model_path).to(DEVICE)(self.model_path).to(DEVICE)
        # tokenizer = AutoTokenizer.from_pretrained(self.tokenizer_path)
       
        # # Load data from disk
        # dataset = load_from_disk(self.data_path)

        # # Initialize metric
        # rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]
        # rouge_metric = evaluate.load('rouge')

        # # Calculate rouge scores
        # score = self.calculate_metric(
        #     dataset=dataset["test"][:20],
        #     metric=rouge_metric,
        #     model=model,
        #     tokenizer=tokenizer,
        #     batch_size = 2,
        #     device=DEVICE,
        #     column_text = 'dialogue',
        #     column_summary= 'summary'
        # )

        # rouge_dict = dict((rn, score[rn].mid.fmeasure ) for rn in rouge_names )

        # # Save rouge scores to a data frame on a csv file
        # df = pd.DataFrame(rouge_dict, index = ['pegasus'] )
        # df.to_csv(self.metric_file_name, index=False)



