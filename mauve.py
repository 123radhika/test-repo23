from evaluate import load
import mauve

mauve = load('mauve')
predictions = ["hello world", "goodnight moon"]
references = ["hello world",  "goodnight moon"]
mauve_results = mauve.compute(predictions=predictions, references=references)
print(mauve_results.mauve)