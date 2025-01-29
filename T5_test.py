from transformers import T5ForConditionalGeneration, T5Tokenizer
import os
from transformers import AutoModel

os.environ["TRANSFORMERS_CACHE"] = "D:\Translation"
os.environ["HF_HOME"] = "D:\Translation"

modelname = 'google/madlad400-10b-mt'
model = T5ForConditionalGeneration.from_pretrained(modelname, device_map="auto", cache_dir="D:\Translation")
tokenizer = T5Tokenizer.from_pretrained(modelname, cache_dir="D:\Translation")

print ("موفق")

text = "<2fa> Hello"
input_ids = tokenizer(text, return_tensors="pt").input_ids.to(model.device)
outputs = model.generate(input_ids=input_ids)

tokenizer.decode(outputs[0], skip_special_tokens=True)
text = "<2fa> Hello"
input_ids = tokenizer(text, return_tensors="pt").input_ids.to(model.device)
outputs = model.generate(input_ids=input_ids)

p = tokenizer.decode(outputs[0], skip_special_tokens=True)
print (p)