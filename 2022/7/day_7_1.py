from collections import defaultdict

disk_size = 70_000_000
required_unused = 30_000_000

def run():
    sizes = defaultdict(int)

    file_path = "/"
    files = []

    total_size = 0

    for line in open("input.txt", "r").readlines()[1:]:
        line = line.strip()

        if line == "$ ls":
            continue
        elif line.startswith("dir "):
            continue
        elif line == "$ cd ..":
            dir_size = sizes[file_path]
            if dir_size <= 100000:
                total_size += dir_size

            file_path = file_path[:-len(files.pop())]

            sizes[file_path] += dir_size

        elif line.startswith("$ cd"):
            cur_file = line[5:]
            files.append(cur_file)
            file_path += cur_file
        else:
            (size, _) = line.split(" ")
            sizes[file_path] += int(size)

    dir_size = sizes[file_path]
    if dir_size <= 100000:
        total_size += dir_size


    disk_space = 70_000_000
    used_space = sizes["/"]
    unused_space = disk_space - used_space
    min_to_delete = 30_000_000 - unused_space

    a = [s for s in sizes.values()]
    a.sort()

    for i in a:
        if i > min_to_delete:
            to_delete = i
            break

    print(total_size) #1723892
    print(to_delete) #8474158


if __name__ == '__main__':
    run()