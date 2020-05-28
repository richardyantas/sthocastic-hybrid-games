
R = [ [0.1,0.2], [40,70]] 
S = [ [0.09,0.31], [30,80]] 
tau = 300 # 5min
factorTe = 2.5
factorI  = 0.8
factorKe = 1
rate     = 0.01
TwaterIn = 22.5

def query(X): 
	if (40<= X.T and X.T <= 40.4688) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [1,6], [2,1], [4,1], [6,1], [0,1,6], [0,4,1], [0,6,1], [2,0,1], [3,0,7], [3,3,0], [3,5,0], [3,7,0], [4,0,1], [5,0,7], [5,3,0], [5,5,0], [6,0,1], [7,0,7], [7,3,0], [7,5,0], [7,7,0]]
	if (40.4688<= X.T and X.T <= 40.9375) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [1,6], [2,1], [3,0], [4,1], [6,1], [0,1,6], [0,4,1], [0,6,1], [2,0,1], [4,0,1], [5,0,7], [5,3,0], [5,5,0], [6,0,1], [7,0,7], [7,3,0], [7,5,0], [7,7,0]]
	if (40.9375<= X.T and X.T <= 41.4062) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [1,6], [2,1], [3,0], [4,1], [6,1], [0,1,6], [0,4,1], [0,6,1], [2,0,7], [4,0,1], [5,0,7], [5,3,0], [5,5,0], [7,0,7], [7,3,0], [7,5,0], [7,7,0]]
	if (41.4062<= X.T and X.T <= 41.875) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [1,6], [2,1], [3,0], [4,1], [6,1], [0,1,6], [0,4,1], [0,6,1], [1,4,0], [2,0,7], [4,0,1], [5,0,7], [5,3,0], [5,5,0], [6,0,7], [7,0,7], [7,3,0], [7,5,0], [7,7,0]]
	if (41.875<= X.T and X.T <= 42.3438) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [1,6], [3,0], [4,1], [7,0], [0,1,6], [0,4,1], [0,6,3], [1,4,0], [2,0,7], [2,1,6], [2,4,1], [4,0,7], [5,0,7], [5,3,0], [5,5,0], [6,0,7], [6,1,6], [6,4,1]]
	if (42.3438<= X.T and X.T <= 42.8125) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [1,6], [3,0], [4,1], [7,0], [0,1,6], [0,6,3], [1,4,0], [2,0,7], [2,1,6], [4,0,7], [5,0,7], [5,3,0], [5,5,0], [6,0,7], [6,1,6]]
	if (42.8125<= X.T and X.T <= 43.2812) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [1,6], [3,0], [7,0], [0,1,6], [0,6,3], [1,4,0], [2,0,7], [2,1,6], [4,0,7], [4,1,6], [5,0,7], [5,3,0], [5,5,0], [6,0,7], [6,1,6]]
	if (43.2812<= X.T and X.T <= 43.75) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [1,6], [3,0], [7,0], [0,1,6], [0,6,3], [1,4,0], [2,0,7], [2,1,6], [4,0,7], [4,1,6], [5,0,7], [5,3,0], [5,5,0], [6,0,7], [6,1,6]]
	if (43.75<= X.T and X.T <= 44.2188) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [1,6], [3,0], [7,0], [0,6,3], [1,4,0], [2,0,7], [2,1,6], [4,0,7], [4,1,6], [5,0,7], [5,3,0], [5,5,0], [6,0,7]]
	if (44.2188<= X.T and X.T <= 44.6875) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [1,6], [3,0], [7,0], [0,6,3], [1,4,0], [2,0,7], [4,0,7], [4,1,6], [5,0,7], [5,3,0], [5,5,0], [6,0,7]]
	if (44.6875<= X.T and X.T <= 45.1562) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [7,0], [0,6,3], [2,0,7], [4,0,7], [5,0,7], [5,3,0], [5,5,0], [6,0,7]]
	if (45.1562<= X.T and X.T <= 45.625) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,6,3], [2,0,7], [4,0,7], [6,0,7]]
	if (45.625<= X.T and X.T <= 46.0938) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,6,3], [2,0,7], [2,3,0], [4,0,7], [4,3,0], [6,0,7]]
	if (46.0938<= X.T and X.T <= 46.5625) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,7,0], [4,0,7], [4,3,0], [6,0,7]]
	if (46.5625<= X.T and X.T <= 47.0312) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,7,0], [4,0,7], [4,3,0], [6,0,7]]
	if (47.0312<= X.T and X.T <= 47.5) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,7,0], [4,0,7], [4,3,0], [6,0,7]]
	if (47.5<= X.T and X.T <= 47.9688) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,7,0], [4,0,7], [4,3,0], [6,0,7]]
	if (47.9688<= X.T and X.T <= 48.4375) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,7,0], [4,0,7], [4,3,0], [6,0,7], [6,3,0], [6,7,0]]
	if (48.4375<= X.T and X.T <= 48.9062) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,7,0], [4,0,7], [4,3,0], [6,0,7], [6,3,0], [6,7,0]]
	if (48.9062<= X.T and X.T <= 49.375) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,7,0], [4,0,7], [4,3,0], [6,0,7], [6,3,0], [6,7,0]]
	if (49.375<= X.T and X.T <= 49.8438) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,7,0], [4,0,7], [4,3,0], [4,5,0], [6,0,7], [6,3,0], [6,7,0]]
	if (49.8438<= X.T and X.T <= 50.3125) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,7,0], [4,0,7], [4,3,0], [4,5,0], [6,0,7], [6,3,0], [6,7,0]]
	if (50.3125<= X.T and X.T <= 50.7812) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,5,0], [2,7,0], [4,0,7], [4,3,0], [4,5,0], [6,0,7], [6,3,0], [6,7,0]]
	if (50.7812<= X.T and X.T <= 51.25) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,5,0], [2,7,0], [4,0,7], [4,3,0], [4,5,0], [6,0,7], [6,3,0], [6,7,0]]
	if (51.25<= X.T and X.T <= 51.7188) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,5,0], [2,7,0], [4,0,7], [4,3,0], [4,5,0], [6,0,7], [6,3,0], [6,7,0]]
	if (51.7188<= X.T and X.T <= 52.1875) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,5,0], [2,7,0], [4,0,7], [4,3,0], [4,5,0], [6,0,7], [6,3,0], [6,7,0]]
	if (52.1875<= X.T and X.T <= 52.6562) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,5,0], [2,7,0], [4,0,7], [4,3,0], [4,5,0], [6,0,7], [6,3,0], [6,5,0], [6,7,0]]
	if (52.6562<= X.T and X.T <= 53.125) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,5,0], [2,7,0], [4,0,7], [4,3,0], [4,5,0], [6,0,7], [6,3,0], [6,5,0], [6,7,0]]
	if (53.125<= X.T and X.T <= 53.5938) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,5,0], [2,7,0], [4,0,7], [4,3,0], [4,5,0], [6,0,7], [6,3,0], [6,5,0], [6,7,0]]
	if (53.5938<= X.T and X.T <= 54.0625) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,5,0], [2,7,0], [4,0,7], [4,3,0], [4,5,0], [6,0,7], [6,3,0], [6,5,0], [6,7,0]]
	if (54.0625<= X.T and X.T <= 54.5312) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,5,0], [2,7,0], [4,0,7], [4,3,0], [4,5,0], [6,0,7], [6,3,0], [6,5,0], [6,7,0]]
	if (54.5312<= X.T and X.T <= 55) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [3,0], [5,0], [7,0], [0,0,7], [0,6,3], [2,0,7], [2,3,0], [2,5,0], [2,7,0], [4,0,7], [4,3,0], [4,5,0], [6,0,7], [6,3,0], [6,5,0], [6,7,0]]
	if (55<= X.T and X.T <= 55.4688) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [2,0], [3,0], [4,0], [5,0], [7,0], [0,0,7], [0,6,3], [6,0,7], [6,3,0], [6,5,0], [6,7,0]]
	if (55.4688<= X.T and X.T <= 55.9375) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [2,0], [3,0], [4,0], [5,0], [0,0,7], [0,6,3], [6,0,7], [6,5,0], [7,0,6], [7,4,0]]
	if (55.9375<= X.T and X.T <= 56.4062) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [2,0], [4,0], [5,0], [0,0,7], [0,6,3], [3,0,6], [3,4,0], [6,0,7], [6,5,0], [7,0,6], [7,4,0]]
	if (56.4062<= X.T and X.T <= 56.875) and (0.1<= X.V and X.V <= 0.2):
		return [[0,7], [2,0], [4,0], [5,0], [0,6,7], [3,0,6], [3,4,0], [6,0,7], [6,5,0], [7,0,6], [7,4,0]]
	if (56.875<= X.T and X.T <= 57.3438) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [0,6,7], [2,0], [4,0], [5,0], [3,0,6], [6,5,0], [7,0,6]]
	if (57.3438<= X.T and X.T <= 57.8125) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [5,0], [6,0], [3,0,6], [7,0,6]]
	if (57.8125<= X.T and X.T <= 58.2812) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [5,0], [6,0]]
	if (58.2812<= X.T and X.T <= 58.75) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [5,0], [6,0]]
	if (58.75<= X.T and X.T <= 59.2188) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [5,0], [6,0]]
	if (59.2188<= X.T and X.T <= 59.6875) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [5,0], [6,0]]
	if (59.6875<= X.T and X.T <= 60.1562) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [5,0], [6,0], [0,5,0]]
	if (60.1562<= X.T and X.T <= 60.625) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [5,0], [6,0], [0,5,0]]
	if (60.625<= X.T and X.T <= 61.0938) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [5,0], [6,0], [0,5,0]]
	if (61.0938<= X.T and X.T <= 61.5625) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [5,0], [6,0], [0,5,0]]
	if (61.5625<= X.T and X.T <= 62.0312) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [6,0], [0,5,0], [5,0,6]]
	if (62.0312<= X.T and X.T <= 62.5) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [6,0], [5,0,6]]
	if (62.5<= X.T and X.T <= 62.9688) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [6,0], [5,0,6]]
	if (62.9688<= X.T and X.T <= 63.4375) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [6,0], [5,0,6]]
	if (63.4375<= X.T and X.T <= 63.9062) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [6,0]]
	if (63.9062<= X.T and X.T <= 64.375) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [6,0]]
	if (64.375<= X.T and X.T <= 64.8438) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [6,0]]
	if (64.8438<= X.T and X.T <= 65.3125) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [6,0]]
	if (65.3125<= X.T and X.T <= 65.7812) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [6,0]]
	if (65.7812<= X.T and X.T <= 66.25) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [6,0]]
	if (66.25<= X.T and X.T <= 66.7188) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [6,0]]
	if (66.7188<= X.T and X.T <= 67.1875) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [6,0]]
	if (67.1875<= X.T and X.T <= 67.6562) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [6,0]]
	if (67.6562<= X.T and X.T <= 68.125) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [6,0]]
	if (68.125<= X.T and X.T <= 68.5938) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [6,0]]
	if (68.5938<= X.T and X.T <= 69.0625) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [2,0], [4,0], [6,0]]
	if (69.0625<= X.T and X.T <= 69.5312) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [4,0], [2,0,6], [2,4,0], [6,0,6], [6,4,0]]
	if (69.5312<= X.T and X.T <= 70) and (0.1<= X.V and X.V <= 0.2):
		return [[0,6], [4,0], [2,0,6], [2,4,0], [6,0,6], [6,4,0]]
	print("Not Found") 
	return [[-1,-1,-1]]

'''
{{40,40.4688,0.1,0.2},
{40.4688,40.9375,0.1,0.2},
{40.9375,41.4062,0.1,0.2},
{41.4062,41.875,0.1,0.2},
{41.875,42.3438,0.1,0.2},
{42.3438,42.8125,0.1,0.2},
{42.8125,43.2812,0.1,0.2},
{43.2812,43.75,0.1,0.2},
{43.75,44.2188,0.1,0.2},
{44.2188,44.6875,0.1,0.2},
{44.6875,45.1562,0.1,0.2},
{45.1562,45.625,0.1,0.2},
{45.625,46.0938,0.1,0.2},
{46.0938,46.5625,0.1,0.2},
{46.5625,47.0312,0.1,0.2},
{47.0312,47.5,0.1,0.2},
{47.5,47.9688,0.1,0.2},
{47.9688,48.4375,0.1,0.2},
{48.4375,48.9062,0.1,0.2},
{48.9062,49.375,0.1,0.2},
{49.375,49.8438,0.1,0.2},
{49.8438,50.3125,0.1,0.2},
{50.3125,50.7812,0.1,0.2},
{50.7812,51.25,0.1,0.2},
{51.25,51.7188,0.1,0.2},
{51.7188,52.1875,0.1,0.2},
{52.1875,52.6562,0.1,0.2},
{52.6562,53.125,0.1,0.2},
{53.125,53.5938,0.1,0.2},
{53.5938,54.0625,0.1,0.2},
{54.0625,54.5312,0.1,0.2},
{54.5312,55,0.1,0.2},
{55,55.4688,0.1,0.2},
{55.4688,55.9375,0.1,0.2},
{55.9375,56.4062,0.1,0.2},
{56.4062,56.875,0.1,0.2},
{56.875,57.3438,0.1,0.2},
{57.3438,57.8125,0.1,0.2},
{57.8125,58.2812,0.1,0.2},
{58.2812,58.75,0.1,0.2},
{58.75,59.2188,0.1,0.2},
{59.2188,59.6875,0.1,0.2},
{59.6875,60.1562,0.1,0.2},
{60.1562,60.625,0.1,0.2},
{60.625,61.0938,0.1,0.2},
{61.0938,61.5625,0.1,0.2},
{61.5625,62.0312,0.1,0.2},
{62.0312,62.5,0.1,0.2},
{62.5,62.9688,0.1,0.2},
{62.9688,63.4375,0.1,0.2},
{63.4375,63.9062,0.1,0.2},
{63.9062,64.375,0.1,0.2},
{64.375,64.8438,0.1,0.2},
{64.8438,65.3125,0.1,0.2},
{65.3125,65.7812,0.1,0.2},
{65.7812,66.25,0.1,0.2},
{66.25,66.7188,0.1,0.2},
{66.7188,67.1875,0.1,0.2},
{67.1875,67.6562,0.1,0.2},
{67.6562,68.125,0.1,0.2},
{68.125,68.5938,0.1,0.2},
{68.5938,69.0625,0.1,0.2},
{69.0625,69.5312,0.1,0.2},
{69.5312,70,0.1,0.2}
}


{
{{0,7,-1}, {1,6,-1}, {2,1,-1}, {4,1,-1}, {6,1,-1}, {0,1,6}, {0,4,1}, {0,6,1}, {2,0,1}, {3,0,7}, {3,3,0}, {3,5,0}, {3,7,0}, {4,0,1}, {5,0,7}, {5,3,0}, {5,5,0}, {6,0,1}, {7,0,7}, {7,3,0}, {7,5,0}, {7,7,0}},
{{0,7,-1}, {1,6,-1}, {2,1,-1}, {3,0,-1}, {4,1,-1}, {6,1,-1}, {0,1,6}, {0,4,1}, {0,6,1}, {2,0,1}, {4,0,1}, {5,0,7}, {5,3,0}, {5,5,0}, {6,0,1}, {7,0,7}, {7,3,0}, {7,5,0}, {7,7,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {1,6,-1}, {2,1,-1}, {3,0,-1}, {4,1,-1}, {6,1,-1}, {0,1,6}, {0,4,1}, {0,6,1}, {2,0,7}, {4,0,1}, {5,0,7}, {5,3,0}, {5,5,0}, {7,0,7}, {7,3,0}, {7,5,0}, {7,7,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {1,6,-1}, {2,1,-1}, {3,0,-1}, {4,1,-1}, {6,1,-1}, {0,1,6}, {0,4,1}, {0,6,1}, {1,4,0}, {2,0,7}, {4,0,1}, {5,0,7}, {5,3,0}, {5,5,0}, {6,0,7}, {7,0,7}, {7,3,0}, {7,5,0}, {7,7,0}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {1,6,-1}, {3,0,-1}, {4,1,-1}, {7,0,-1}, {0,1,6}, {0,4,1}, {0,6,3}, {1,4,0}, {2,0,7}, {2,1,6}, {2,4,1}, {4,0,7}, {5,0,7}, {5,3,0}, {5,5,0}, {6,0,7}, {6,1,6}, {6,4,1}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {1,6,-1}, {3,0,-1}, {4,1,-1}, {7,0,-1}, {0,1,6}, {0,6,3}, {1,4,0}, {2,0,7}, {2,1,6}, {4,0,7}, {5,0,7}, {5,3,0}, {5,5,0}, {6,0,7}, {6,1,6}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {1,6,-1}, {3,0,-1}, {7,0,-1}, {0,1,6}, {0,6,3}, {1,4,0}, {2,0,7}, {2,1,6}, {4,0,7}, {4,1,6}, {5,0,7}, {5,3,0}, {5,5,0}, {6,0,7}, {6,1,6}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {1,6,-1}, {3,0,-1}, {7,0,-1}, {0,1,6}, {0,6,3}, {1,4,0}, {2,0,7}, {2,1,6}, {4,0,7}, {4,1,6}, {5,0,7}, {5,3,0}, {5,5,0}, {6,0,7}, {6,1,6}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {1,6,-1}, {3,0,-1}, {7,0,-1}, {0,6,3}, {1,4,0}, {2,0,7}, {2,1,6}, {4,0,7}, {4,1,6}, {5,0,7}, {5,3,0}, {5,5,0}, {6,0,7}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {1,6,-1}, {3,0,-1}, {7,0,-1}, {0,6,3}, {1,4,0}, {2,0,7}, {4,0,7}, {4,1,6}, {5,0,7}, {5,3,0}, {5,5,0}, {6,0,7}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {7,0,-1}, {0,6,3}, {2,0,7}, {4,0,7}, {5,0,7}, {5,3,0}, {5,5,0}, {6,0,7}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,6,3}, {2,0,7}, {4,0,7}, {6,0,7}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,6,3}, {2,0,7}, {2,3,0}, {4,0,7}, {4,3,0}, {6,0,7}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,7,0}, {4,0,7}, {4,3,0}, {6,0,7}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,7,0}, {4,0,7}, {4,3,0}, {6,0,7}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,7,0}, {4,0,7}, {4,3,0}, {6,0,7}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,7,0}, {4,0,7}, {4,3,0}, {6,0,7}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,7,0}, {4,0,7}, {4,3,0}, {6,0,7}, {6,3,0}, {6,7,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,7,0}, {4,0,7}, {4,3,0}, {6,0,7}, {6,3,0}, {6,7,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,7,0}, {4,0,7}, {4,3,0}, {6,0,7}, {6,3,0}, {6,7,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,7,0}, {4,0,7}, {4,3,0}, {4,5,0}, {6,0,7}, {6,3,0}, {6,7,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,7,0}, {4,0,7}, {4,3,0}, {4,5,0}, {6,0,7}, {6,3,0}, {6,7,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,5,0}, {2,7,0}, {4,0,7}, {4,3,0}, {4,5,0}, {6,0,7}, {6,3,0}, {6,7,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,5,0}, {2,7,0}, {4,0,7}, {4,3,0}, {4,5,0}, {6,0,7}, {6,3,0}, {6,7,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,5,0}, {2,7,0}, {4,0,7}, {4,3,0}, {4,5,0}, {6,0,7}, {6,3,0}, {6,7,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,5,0}, {2,7,0}, {4,0,7}, {4,3,0}, {4,5,0}, {6,0,7}, {6,3,0}, {6,7,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,5,0}, {2,7,0}, {4,0,7}, {4,3,0}, {4,5,0}, {6,0,7}, {6,3,0}, {6,5,0}, {6,7,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,5,0}, {2,7,0}, {4,0,7}, {4,3,0}, {4,5,0}, {6,0,7}, {6,3,0}, {6,5,0}, {6,7,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,5,0}, {2,7,0}, {4,0,7}, {4,3,0}, {4,5,0}, {6,0,7}, {6,3,0}, {6,5,0}, {6,7,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,5,0}, {2,7,0}, {4,0,7}, {4,3,0}, {4,5,0}, {6,0,7}, {6,3,0}, {6,5,0}, {6,7,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,5,0}, {2,7,0}, {4,0,7}, {4,3,0}, {4,5,0}, {6,0,7}, {6,3,0}, {6,5,0}, {6,7,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {3,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {2,0,7}, {2,3,0}, {2,5,0}, {2,7,0}, {4,0,7}, {4,3,0}, {4,5,0}, {6,0,7}, {6,3,0}, {6,5,0}, {6,7,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {2,0,-1}, {3,0,-1}, {4,0,-1}, {5,0,-1}, {7,0,-1}, {0,0,7}, {0,6,3}, {6,0,7}, {6,3,0}, {6,5,0}, {6,7,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {2,0,-1}, {3,0,-1}, {4,0,-1}, {5,0,-1}, {0,0,7}, {0,6,3}, {6,0,7}, {6,5,0}, {7,0,6}, {7,4,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {2,0,-1}, {4,0,-1}, {5,0,-1}, {0,0,7}, {0,6,3}, {3,0,6}, {3,4,0}, {6,0,7}, {6,5,0}, {7,0,6}, {7,4,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,7,-1}, {2,0,-1}, {4,0,-1}, {5,0,-1}, {0,6,7}, {3,0,6}, {3,4,0}, {6,0,7}, {6,5,0}, {7,0,6}, {7,4,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {0,6,7}, {2,0,-1}, {4,0,-1}, {5,0,-1}, {3,0,6}, {6,5,0}, {7,0,6}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {5,0,-1}, {6,0,-1}, {3,0,6}, {7,0,6}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {5,0,-1}, {6,0,-1}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {5,0,-1}, {6,0,-1}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {5,0,-1}, {6,0,-1}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {5,0,-1}, {6,0,-1}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {5,0,-1}, {6,0,-1}, {0,5,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {5,0,-1}, {6,0,-1}, {0,5,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {5,0,-1}, {6,0,-1}, {0,5,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {5,0,-1}, {6,0,-1}, {0,5,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {6,0,-1}, {0,5,0}, {5,0,6}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {6,0,-1}, {5,0,6}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {6,0,-1}, {5,0,6}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {6,0,-1}, {5,0,6}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {6,0,-1}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {6,0,-1}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {6,0,-1}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {6,0,-1}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {6,0,-1}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {6,0,-1}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {6,0,-1}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {6,0,-1}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {6,0,-1}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {6,0,-1}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {6,0,-1}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {2,0,-1}, {4,0,-1}, {6,0,-1}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {4,0,-1}, {2,0,6}, {2,4,0}, {6,0,6}, {6,4,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},
{{0,6,-1}, {4,0,-1}, {2,0,6}, {2,4,0}, {6,0,6}, {6,4,0}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}, {-2,-2,-2}},}
'''