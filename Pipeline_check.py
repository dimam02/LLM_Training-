from transformers import pipeline

ner = pipeline("ner")
result = ner("Apple Inc. is planning to open a new store in New York.")
print(result)