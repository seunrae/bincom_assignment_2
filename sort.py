numbers=[20, 11, 15, 17, 2];
temp = 0;
for i in range(len(numbers) - 1):
	for j in range(i+1, len(numbers)):
		if(numbers[i] > numbers[j]):
			temp = numbers[i];
			numbers[i] = numbers[j];
			numbers[j] = temp;			
print(numbers);

		