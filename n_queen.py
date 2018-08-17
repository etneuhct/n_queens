

class NQueen():

    """
    Implémentation d'un algorithme pour resoudre le probleme des N Reines (jeu d'échec)
    """

    def __init__(self, col, row, prohibited_positions, final):

        self.col = col
        table = {}

        for element in range(col):
            temp = []
            for item in range(row):
                if (element, item) not in prohibited_positions:
                    temp.append(item)

            table[element] = temp

        self.table = table
        self.final = final

    def new_table(self, position, table):

        result = {}
        for element in table.keys():
            temp = []
            if element != position[0]:
                for item in table[element]:
                    if item != position[1]:
                        if abs(element - position[0]) != abs(item - position[1]):
                            temp.append(item)

            result[element] = temp
        return result

    def loop(self, table, col, p, first_item):

        first_col = self.get_first_col(table)
        #first_item = True
        if first_col:
            for element in first_col[1]:
                position = (first_col[0], element)
                value = *p, position
                table_2 = self.new_table(position, table)
                if len(value) == col+1:
                    value = [(value[0:2]), *value[2:]]
                    self.final.append(value)
                self.loop(table_2, col, value, first_item)

    def get_first_col(self, table):
        for i in range(len(table)):
            if len(table[i]) > 0:
                return i, table[i]

    def start(self, i, j):

        table = self.table
        init_position = (i, j)
        table = self.new_table(init_position, table)
        self.loop(table, self.col, init_position, True)


def run(n):
    result = []
    for x in range(n):
        solution = []
        NQueen(n, n, [], solution).start(0, x)
        for item in solution:
            result.append(item)

    return result


for i in run(8):
    print(i)
