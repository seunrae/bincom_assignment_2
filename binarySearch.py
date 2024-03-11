li = [2, 3, 4, 5, 6, 7, 8];
key = 5;


def binary_search(li, key):
	low = 0;
	high = len(li)-1;
	mid = 0;

	while low <= high:
		mid = int(low + ((high - low)/2));
		if li[mid] < key:
			low = mid + 1;

		elif li[mid] > key:
			high = mid - 1;

		else:
			return mid;
		
	return -1;

result = binary_search(li, key)

print("key found at index: ", result);
