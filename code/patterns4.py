
R = [ [0.1, 0.3], [40, 70]]
S = [ [0.09, 0.31], [30, 80]]

tau = 300
factorTe = 2.5
factorI  = 0.8
factorKe = 1 
rate     = 0.01 
TwaterIn = 22.5

def query(X): 
	if (40<= X.T and X.T <= 40.4688) and (0.1<= X.V and X.V <= 0.3):
		return [[3], [3,7], [0,7], [1,4], [2,1], [2,1,5], [3,4,1], [3,5,2], [3,6,1], [0,1,4], [0,4,1], [0,5,3], [0,6,1], [2,0,1]]
	if (40.4688<= X.T and X.T <= 40.9375) and (0.1<= X.V and X.V <= 0.3):
		return [[3], [3,7], [0,7], [1,4], [2,1], [2,1,5], [3,4,1], [3,5,2], [3,6,3], [0,1,4], [0,4,1], [0,5,3], [0,6,1], [2,0,7]]
	if (40.9375<= X.T and X.T <= 41.4062) and (0.1<= X.V and X.V <= 0.3):
		return [[3], [3,7], [0,5], [1,4], [2,1], [2,1,5], [3,4,1], [3,5,2], [3,6,3], [0,1,4], [0,4,1], [2,0,7]]
	if (41.4062<= X.T and X.T <= 41.875) and (0.1<= X.V and X.V <= 0.3):
		return [[3], [3,7], [0,5], [1,4], [2,1], [2,1,5], [3,4,1], [3,5,2], [3,6,3], [0,1,4], [0,4,1], [1,0,4], [2,0,7]]
	if (41.875<= X.T and X.T <= 42.3438) and (0.1<= X.V and X.V <= 0.3):
		return [[3], [3,7], [0,5], [1,4], [2,3], [2,3,5], [3,4,3], [3,5,2], [3,6,3], [0,1,4], [0,4,3], [1,0,4], [2,0,7], [2,1,4], [2,2,3]]
	if (42.3438<= X.T and X.T <= 42.8125) and (0.1<= X.V and X.V <= 0.3):
		return [[3], [3,7], [0,5], [1,4], [2,3], [2,3,5], [3,4,3], [3,5,2], [3,6,3], [0,1,4], [0,4,3], [1,0,4], [2,0,7], [2,1,4], [2,2,3]]
	if (42.8125<= X.T and X.T <= 43.2812) and (0.1<= X.V and X.V <= 0.3):
		return [[3], [3,7], [0,5], [1,4], [2,3], [2,3,5], [3,4,3], [3,5,2], [3,6,3], [0,1,4], [0,4,3], [1,0,4], [2,0,7], [2,1,4], [2,2,3]]
	if (43.2812<= X.T and X.T <= 43.75) and (0.1<= X.V and X.V <= 0.3):
		return [[3], [3,7], [0,5], [1,4], [2,3], [2,3,5], [3,4,3], [3,5,2], [3,6,3], [0,1,4], [0,4,3], [1,0,4], [2,0,7], [2,1,4], [2,2,3]]
	if (43.75<= X.T and X.T <= 44.2188) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,7], [0,5], [1,4], [0,4,3], [1,0,4]]
	if (44.2188<= X.T and X.T <= 44.6875) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,7], [0,5], [1,4], [0,4,3]]
	if (44.6875<= X.T and X.T <= 45.1562) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,7], [0,5], [1,4], [0,4,3]]
	if (45.1562<= X.T and X.T <= 45.625) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,7], [0,5], [0,4,3]]
	if (45.625<= X.T and X.T <= 46.0938) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,4,3]]
	if (46.0938<= X.T and X.T <= 46.5625) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,7], [0,4,3]]
	if (46.5625<= X.T and X.T <= 47.0312) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,7], [0,4,3]]
	if (47.0312<= X.T and X.T <= 47.5) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,7], [0,4,3]]
	if (47.5<= X.T and X.T <= 47.9688) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,7], [0,4,3]]
	if (47.9688<= X.T and X.T <= 48.4375) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,7], [0,4,3]]
	if (48.4375<= X.T and X.T <= 48.9062) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,7], [0,4,3]]
	if (48.9062<= X.T and X.T <= 49.375) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,7], [0,4,3]]
	if (49.375<= X.T and X.T <= 49.8438) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,7], [0,4,3]]
	if (49.8438<= X.T and X.T <= 50.3125) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,7], [0,4,3]]
	if (50.3125<= X.T and X.T <= 50.7812) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,7], [0,4,3]]
	if (50.7812<= X.T and X.T <= 51.25) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,7], [0,4,3]]
	if (51.25<= X.T and X.T <= 51.7188) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,7], [0,4,3]]
	if (51.7188<= X.T and X.T <= 52.1875) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,7], [0,4,3]]
	if (52.1875<= X.T and X.T <= 52.6562) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,7], [0,4,3]]
	if (52.6562<= X.T and X.T <= 53.125) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,7], [0,4,3]]
	if (53.125<= X.T and X.T <= 53.5938) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,7], [0,4,3]]
	if (53.5938<= X.T and X.T <= 54.0625) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,7], [0,4,3]]
	if (54.0625<= X.T and X.T <= 54.5312) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,5], [0,4,3]]
	if (54.5312<= X.T and X.T <= 55) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,5], [0,0,5], [0,4,3]]
	if (55<= X.T and X.T <= 55.4688) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,4], [0,4,5], [0,0,5]]
	if (55.4688<= X.T and X.T <= 55.9375) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,3], [2,3,6], [0,4], [0,4,5], [0,0,5]]
	if (55.9375<= X.T and X.T <= 56.4062) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [0,4,5], [2,3,4], [2,4,0], [2,5,0], [0,0,5]]
	if (56.4062<= X.T and X.T <= 56.875) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [0,4,5], [2,3,4], [2,4,0], [2,5,0], [0,0,5]]
	if (56.875<= X.T and X.T <= 57.3438) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [0,4,5], [2,3,4], [2,4,0], [2,5,0], [0,0,5]]
	if (57.3438<= X.T and X.T <= 57.8125) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [0,4,5], [2,4,0], [2,5,0], [0,0,5]]
	if (57.8125<= X.T and X.T <= 58.2812) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [0,4,5], [2,4,0], [2,5,0], [0,0,5]]
	if (58.2812<= X.T and X.T <= 58.75) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [0,4,5], [2,4,0], [2,5,0], [0,0,5]]
	if (58.75<= X.T and X.T <= 59.2188) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [0,4,5], [2,4,0], [2,5,0], [0,0,5]]
	if (59.2188<= X.T and X.T <= 59.6875) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [0,4,5], [2,4,0], [2,5,0], [0,0,5]]
	if (59.6875<= X.T and X.T <= 60.1562) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [0,4,5], [2,4,0], [2,5,2], [0,0,5]]
	if (60.1562<= X.T and X.T <= 60.625) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [0,4,5], [2,4,0], [0,0,5]]
	if (60.625<= X.T and X.T <= 61.0938) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [0,4,5], [2,4,0], [0,0,5]]
	if (61.0938<= X.T and X.T <= 61.5625) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [0,4,5], [2,4,0], [0,0,5]]
	if (61.5625<= X.T and X.T <= 62.0312) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [0,4,5], [2,4,0]]
	if (62.0312<= X.T and X.T <= 62.5) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [2,4,0]]
	if (62.5<= X.T and X.T <= 62.9688) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [2,4,0]]
	if (62.9688<= X.T and X.T <= 63.4375) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [2,4,0]]
	if (63.4375<= X.T and X.T <= 63.9062) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [2,4,0]]
	if (63.9062<= X.T and X.T <= 64.375) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [2,4,0]]
	if (64.375<= X.T and X.T <= 64.8438) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [2,4,0]]
	if (64.8438<= X.T and X.T <= 65.3125) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [2,4,0]]
	if (65.3125<= X.T and X.T <= 65.7812) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [2,4,0]]
	if (65.7812<= X.T and X.T <= 66.25) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [2,4,0]]
	if (66.25<= X.T and X.T <= 66.7188) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [2,4,0]]
	if (66.7188<= X.T and X.T <= 67.1875) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [2,6], [0,4], [2,4,0]]
	if (67.1875<= X.T and X.T <= 67.6562) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [0,4], [2,4,0], [2,6,4]]
	if (67.6562<= X.T and X.T <= 68.125) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [0,4], [2,4,0], [2,6,4]]
	if (68.125<= X.T and X.T <= 68.5938) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [0,4], [2,4,0]]
	if (68.5938<= X.T and X.T <= 69.0625) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [0,4], [2,4,2]]
	if (69.0625<= X.T and X.T <= 69.5312) and (0.1<= X.V and X.V <= 0.3):
		return [[2], [0,4]]
	if (69.5312<= X.T and X.T <= 70) and (0.1<= X.V and X.V <= 0.3):
		return [[0,4], [2,4], [2,0,4], [2,2,4], [4,0,4], [4,2,4]]
	print("Not Found") 
	return [[-1,-1,-1]]