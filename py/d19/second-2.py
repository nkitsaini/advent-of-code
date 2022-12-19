def answer(first_check, second_check, max_iter):
	m1, i1 = first_check
	m2, i2 = second_check
	gaps_i = i2 - i1
	gaps_m = m2 - m1
	total_iter = (max_iter - i1) // gaps_i
	print(f"{total_iter=}, {gaps_i=}, {gaps_m=}, {max_iter=}")
	ans = m1 + (total_iter*(gaps_m))
	print('Take this', ans, 'and add whatever is answer of this iteration after repeat', (max_iter-i1)%(gaps_i))
	return ans
# vals = [(56, 33), (109, 68)]

vals = [(695, 433), (3406, 2148)]
answer(*vals, 2022)
answer(*vals, 1000000000000)
