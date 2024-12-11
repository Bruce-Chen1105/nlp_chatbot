from datasets import load_dataset
import pandas as pd

ds = load_dataset("iarfmoose/qa_evaluator")

df = ds['train'].to_pandas()

df.to_csv("data/qa_evaluator.csv", index=False)
