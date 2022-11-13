for i in range(2, 21) :
	f = open(f"multiplication_table/multiplication_table_of_{i}", "w")
	for j in range(1, 11) :
		f.write(f"{i} X {j} = {i*j}\n")
	f.close()
