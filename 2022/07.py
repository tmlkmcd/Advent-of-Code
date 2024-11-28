import sys

lines_in = [line.strip() for line in sys.stdin]

class File:
    def __init__(self, size):
        self.size = size  # we don't care about the name in this puzzle

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []
        self.size = None

    def register_subdir(self, name): self.dirs.append(Dir(name, self))
    def register_file(self, size): self.files.append(File(size))

    def get_size(self):
        if self.size is not None: return self.size
        file_size = sum(file.size for file in self.files)
        dir_size = sum(directory.get_size() for directory in self.dirs)
        self.size = file_size + dir_size
        return self.size

dirs = Dir('/', None)
current_dir = dirs
pointer, limit = 1, len(lines_in)

while pointer < limit:
    line = lines_in[pointer].split(' ')
    if line[1] == 'cd':
        if line[2] == '/': current_dir = dirs
        elif line[2] == '..': current_dir = current_dir.parent
        else: current_dir = next(d for d in current_dir.dirs if d.name == line[2])
    if line[1] == 'ls':
        while not lines_in[pointer + 1].startswith('$'):
            pointer += 1
            next_line = lines_in[pointer]
            if next_line.startswith('dir'):
                current_dir.register_subdir(next_line.split(' ')[1])
            else:
                current_dir.register_file(int(next_line.split(' ')[0]))
            if pointer + 1 >= len(lines_in): break
    pointer += 1

pt1, pt2 = 0, 1e10
total_size = dirs.get_size()

def crawl(directory):
    global pt1, pt2
    s = directory.get_size()
    if s <= 100000: pt1 += s
    if total_size - (70000000 - 30000000) < s: pt2 = min(pt2, s)
    for sub_dir in directory.dirs: crawl(sub_dir)

crawl(dirs)
print(f'part 1: {pt1}; part 2: {pt2}')
