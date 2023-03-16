# Word Wrap Solution Using Dynamic programming
# Jonathan Borghese

import copy, random, time

# macro for cleaner code
inf = float('inf')

def recursive(num_words, line_length, lc):

    # contains the line index for each word
    sol = [[] for x in range(num_words + 1)]

    start_time = time.time()

    # returns the cost[index]
    def recursive_helper(index, s):
        # if the subproblem is already solved, return solution
        if index == 0:
            return 0

        nl_index = -1
        lowest = inf

        # find best arrangement
        for j in range(index):
            if lc[j][index - 1] != inf:
                new_cost = recursive_helper(j, s) + lc[j][index - 1]

                if new_cost < lowest:
                    lowest = new_cost
                    nl_index = j

        s[index] = copy.deepcopy(s[nl_index])
        s[index].append(index - nl_index)

        return lowest

    # call recursive function
    recursive_helper(num_words, sol)

    elapsed_time = time.time() - start_time

    return sol, elapsed_time

def top_down(num_words, line_length, lc):
    # define cost array
    cost = [inf for x in range(num_words + 1)]
    cost[0] = 0

    # contains the line index for each word
    sol = [[] for x in range(num_words + 1)]

    start_time = time.time()

    # returns the cost[index]
    def get_cost_helper(index, c, s):
        # if the subproblem is already solved, return solution
        if c[index] != inf:
            return c[index]

        nl_index = -1

        # find best arrangement
        for j in range(index):
            if lc[j][index - 1] != inf:
                new_cost = get_cost_helper(j, c , s) + lc[j][index - 1]

                if new_cost < c[index]:
                    c[index] = new_cost
                    nl_index = j

        s[index] = copy.deepcopy(s[nl_index])
        s[index].append(index - nl_index)

        return c[index]

    # call recursive function
    get_cost_helper(num_words, cost, sol)

    elapsed_time = time.time() - start_time

    return sol, elapsed_time

def bottom_up(num_words, line_length, lc):
    # define cost array
    cost = [inf for x in range(num_words + 1)]
    cost[0] = 0

    # contains the line index for each word
    sol = [[] for x in range(num_words + 1)]

    start_time = time.time()

    # fill cost array
    for i in range(num_words):
        # try every possible combination of previous solutions
        # to find the minimum cost arrangement
        nl_index = -1

        for j in range(i + 1):
            if lc[j][i] != inf:
                new_cost = cost[j] + lc[j][i]

                if new_cost < cost[i + 1]:
                    cost[i + 1] = new_cost
                    nl_index = j

        sol[i + 1] = copy.deepcopy(sol[nl_index])
        sol[i + 1].append(i - nl_index + 1)

    elapsed_time = time.time() - start_time

    return sol, elapsed_time

def visual_print(sol, words):
    index = 0
    print(str(sol) + ':')

    for num in sol:
        out = ""

        for i in range(num):
            for j in range(words[index]):
                out += 'x'
            out += ' '
            index += 1
        print(out)

def generate_lc(words, num_words, line_length):
    start_time = time.time()

    # define line cost array
    lc = [[0 for y in range(num_words)] for x in range(num_words)]

    # fill lc array
    for x in range(num_words):
        for y in range(x, num_words):

            lc[x][y] = inf

            words_length = 0
            for z in range(x, y+1):
                words_length += words[z]

            spaces = line_length - words_length

            if spaces < 0:
                lc[x][y] = inf
            else:
                lc[x][y] = spaces * spaces

    elapsed_time = time.time() - start_time
    return lc, elapsed_time

def generate_words(n):
        # generate word list
        words = [0 for x in range(n)]
        for i in range(n):
            words[i] = random.randint(2, 10)
        return words

def test(n, l, lc):
    NUM_WORDS = n
    LINE_LENGTH = l

    print('n:' + str(n) + '\tl: ' + str(l))

    s, t = bottom_up(NUM_WORDS, LINE_LENGTH, lc)
    print('bottom-up approach time:\t' + str(t))

    s, t = top_down(NUM_WORDS, LINE_LENGTH, lc)
    print('top-down approach time:\t' + str(t))

    #s, t = recursive(NUM_WORDS, LINE_LENGTH, lc)
    #print('recursive approach\t' + str(t))

    visual_print(s[NUM_WORDS], words)

    print(' ')

words = generate_words(100)

lc, t = generate_lc(words, 10, 20)

test(10, 20, lc)

lc, t = generate_lc(words, 100, 50)
test(100, 50, lc)
