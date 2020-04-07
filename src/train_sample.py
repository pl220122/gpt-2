#read in training file
import json
import jsonlines

'''
with open('data/large-762M-k40.train.jsonl', 'r') as json_file:
	json_list = list(json_file)
	print(len(json_list))
	'''
with jsonlines.open('data/large-762M-k40.train.jsonl', 'r') as reader:
	with jsonlines.open('first_100_train.jsonl', mode='w') as writer:
		for result in reader:
			print(result["id"])
			if int(result["id"])<=100:
				print(result["text"])
				print(result["length"])
				print("="*80)
				writer.write(result)



reader.close()
writer.close()
'''
avg_length = 0
min_length = 1000
low_length = 0
counter = 0
for json_str in json_list:
	counter += 1
	result = json.loads(json_str)
	print(result["id"])
	avg_length += result["length"]


	if result["length"] < min_length:
		min_length = result["length"]

	if result["length"] < 100:
		low_length += 1

	if int(result["id"])%1000 == 0:
		print(result["text"])
		print(result["length"])
		print("="*80)


print("=-"*40)
print(counter)
print(min_length)
print(avg_length/counter)
print(low_length)
'''