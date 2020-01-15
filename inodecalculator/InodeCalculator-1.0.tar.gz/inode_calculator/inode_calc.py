def calc_indirect_block(start_ptr, num_ptr_per_block,num_blocks):
	'''
	Creates a indirect chain with specified starting file offset(start_ptr)
	and number of pointers in a block(num_ptr_per_block) and 
	number of blocks(num_blocks) to include in the chain.
	Returns the indirect chain.
	Example output: [[1,2,3],[4,5,6]]
	'''
	indirect_block = []
	cur_ptr = start_ptr
	for i in xrange(num_blocks):
		direct_block=[]
		for j in xrange(num_ptr_per_block):
			direct_block.append(cur_ptr)
			cur_ptr += 1
		indirect_block.append(direct_block)
	return indirect_block

def find_block(chain,file_offset):
	'''
	Searches for the block where file_offset can be found in the chain.
	The chain input is a indirect chain for format eg. [[1,2,3],[4,5,6]]
	Returns the block number(start from 1) if found, -1 if not found.
	'''
	for i in xrange(len(chain)):
		for j in chain[i]:
			if j==file_offset:
				return i+1
	return -1


def calc_block_access_chain(block_size,pointer_size,file_offset):

	ptr_per_block = block_size/pointer_size 	#number of pointers ber block
	# file offset start from 0.
	# fo == file_offset
	# maximum file offsets per type of block
	max_fo_direct = (ptr_per_block*12) - 1 
	max_fo_indirect = (ptr_per_block**2) + max_fo_direct
	max_fo_double_indirect = (ptr_per_block**3) + max_fo_indirect
	max_fo_triple_indirect = (ptr_per_block**4) + max_fo_double_indirect

	# to store the block access chain
	start_block = []

	# print error if exceeds maximum file offset
	if file_offset > max_fo_triple_indirect:
		print "File offset exceeded max pointers available."
		return

	# direct block
	if file_offset < max_fo_direct:
		start_block.append((file_offset/ptr_per_block)+1)
	# indirect block
	elif file_offset <= max_fo_indirect:
		start_block.append(13)
		indirect_chain = calc_indirect_block(max_fo_direct+1,ptr_per_block,block_size)
		start_block.append(find_block(indirect_chain,file_offset))
	# double indirect block
	elif file_offset > max_fo_indirect and file_offset <= max_fo_double_indirect:
		start_block.append(14)
		double_indirect_chain = []
		cur_offset = max_fo_indirect+1
		for i in xrange(block_size):
			double_indirect_chain.append(calc_indirect_block(cur_offset,ptr_per_block,block_size))
			cur_offset += ptr_per_block**2
		for j in xrange(len(double_indirect_chain)):
			find_offset = find_block(double_indirect_chain[j],file_offset)
			if find_offset != -1:
				start_block.append(j+1)
				start_block.append(find_offset)
	# triple indirect block
	else:
		start_block.append(15)
		triple_indirect_chain = []
		cur_offset = max_fo_double_indirect+1
		for i in xrange(block_size):	
			triple_indirect_dob_chain = []
			#build double_indirect chain to append
			for j in xrange(block_size):
				triple_indirect_dob_chain.append(calc_indirect_block(cur_offset,ptr_per_block,block_size))
				cur_offset += ptr_per_block**2
			triple_indirect_chain.append(triple_indirect_dob_chain)
			
		for k in xrange(len(triple_indirect_chain)):
			for l in xrange(len(triple_indirect_chain[k])):
				find_offset = find_block(triple_indirect_chain[k][l],file_offset)
				if find_offset != -1:
					start_block.append(k+1)
					start_block.append(l+1)
					start_block.append(find_offset)
	return start_block