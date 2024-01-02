# Slice list into 3 equal chunks and reverse each chunk

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk_size = len(sample_list)//3

print("chunk 1", sample_list[0:chunk_size])
print("chunk reverse", list(reversed(sample_list[0:chunk_size])))

print("chunk 2", sample_list[chunk_size:chunk_size+chunk_size])
print("chunk reverse", list(reversed(sample_list[chunk_size:chunk_size+chunk_size])))

print("chunk 3", sample_list[chunk_size+chunk_size:])
print("chunk reverse", list(reversed(sample_list[chunk_size+chunk_size:])))
print()
print()


length = len(sample_list)
chunk_size = length//3

start = 0
end = chunk_size

for i in range(3):
    indexes = slice(start, end)

    list_chunk = sample_list[indexes]
    print("chunk ",i, list_chunk)

    print("After reversing ", list(reversed(list_chunk)))

    start = end
    end+=chunk_size


