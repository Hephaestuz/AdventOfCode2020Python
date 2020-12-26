# ---- Part 1 ----

class HexCoord:

    def __init__(self, north=0, east=0):
        self.n = north
        self.e = east

    def get(self):
        return self.n, self.e

    def step_east(self):
        self.e += 2

    def step_west(self):
        self.e -= 2

    def step_ne(self):
        self.n += 1
        self.e += 1

    def step_se(self):
        self.n -= 1
        self.e += 1

    def step_nw(self):
        self.n += 1
        self.e -= 1

    def step_sw(self):
        self.n -= 1
        self.e -= 1

    def east(self):
        return HexCoord(self.n, self.e + 2)

    def west(self):
        return HexCoord(self.n, self.e - 2)

    def ne(self):
        return HexCoord(self.n + 1, self.e + 1)

    def se(self):
        return HexCoord(self.n - 1, self.e + 1)

    def nw(self):
        return HexCoord(self.n + 1, self.e - 1)

    def sw(self):
        return HexCoord(self.n - 1, self.e - 1)

    def get_neighbours(self):
        return [self.east(), self.west(), self.ne(), self.se(), self.nw(), self.sw()]


def parse(tile_reference):
    pos = HexCoord()
    first = True
    last = 'x'
    for i, ch in enumerate(tile_reference):
        if first:
            if ch == 'e':
                pos.step_east()
            if ch == 'w':
                pos.step_west()
            if ch == 'n':
                first = False
                last = 'n'
            if ch == 's':
                first = False
                last = 's'
        else:
            first = True
            if last == 'n':
                if ch == 'e':
                    pos.step_ne()
                if ch == 'w':
                    pos.step_nw()
            else:
                if ch == 'e':
                    pos.step_se()
                if ch == 'w':
                    pos.step_sw()
    return pos


def read_reference(file):
    with open(file, 'r') as f:
        for row in f:
            yield row.strip()


def part1():

    black_tiles = set()

    for ref in read_reference('day24_input.txt'):
        tile = parse(ref).get()
        if tile in black_tiles:
            black_tiles.discard(tile)
        else:
            black_tiles.add(tile)

    print("Flipped tiles: ", len(black_tiles))

    return black_tiles

# ---- Part 2 ----


def update_tile(hex_tile, black_tiles, black):
    count = 0
    for neighbour in hex_tile.get_neighbours():
        if neighbour in black_tiles:
            count += 1
    if black:
        if count == 0 or count > 2:
            return True
        else:
            return False
    else:
        if count == 2:
            return True
        else:
            return False


if __name__ == '__main__':
    tiles = part1()

