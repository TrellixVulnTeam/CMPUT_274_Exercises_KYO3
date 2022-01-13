import random

def mapper (probability: int, prob_list: list):
    u_list = [0]
    s = 0
    for item in prob_list:
        s = s + item
        u_list.append(s)
        
        
        
        
    m = len(u_list)
    i = 1

    while i < m:
        
        if u_list[i - 1] <= probability < u_list[i]:
            return i
        else:
            i = i + 1
        
    
    
    
    
def biased_rolls(prob_list , s, n):
    """ Simulate n rolls of a biased m-sided die and return a list containing the results.
    Arguments:
    prob_list: a list of the probabilities of rolling the
    number on each side of the m-sided die. The list will always have the length m (m >= 2), where m is the number of sides numbered 1 to m. Therefore,
    for example, the probability stored at index 0 in the list is the probability of rolling a 1 on
    the m-sided die.
    
    s: the seed to use when initializing the PRNG n: the number of rolls to return
    Return:
    rolls: a list (of length n) containing each of the n rolls of the
    """
    
    random.seed(s)
    

        
    output_list = []
    
    for i in range(n):
        probability = random.random()
        output_list.append(mapper(probability, prob_list))
        
        
    return output_list    
pass

def draw_histogram(m, rolls, width):
    """ Draws a frequency histogram of the rolls of an m-sided die mapped to a fixed width.
    Arguments:
    m (int): the number of sides on the die
    
    rolls (list): the list of rolls generated by the biased die width (int): the fixed width of the histogram, in characters
    (this is the length of the longest bar in the histogram, to maximize space in the chart)
    
    eturns:
    None (but prints the histogram to standard output) """
    print("Frequency Histogram: {0}-sided Die".format(m))
    
    hound_count_list = []
    for i in range(m):
        
        hound_count = 0
        hyphen_count = 0
        for item in rolls:
            if item == i + 1:
                hound_count = hound_count + 1
        hound_count_list.append(hound_count)


    ## Need to get max of hound count
    max_hound_count = 0
    for item in hound_count_list:
        if item > max_hound_count:
            max_hound_count = item
    
    ## Got max_hound count
    ## Find the multiplier
    multiplier = width//max_hound_count

    
    ## New Hound count list
    new_hound_count_list = []
    for item in hound_count_list:
        new_hound_count_list.append(round(item * width/max_hound_count))

    
    ## Make a hyphen_list
    hyphen_list = []  
    for item in new_hound_count_list:
        hyphen_list.append(width - item)

    
    for i in range(m):
        hound = '#'* new_hound_count_list[i]
        hyphen = '-'*hyphen_list[i]
        
        print("{0}.{1}{2}".format(i + 1, hound, hyphen))
    
    return None
pass



