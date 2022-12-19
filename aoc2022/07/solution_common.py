import sys

def _parse_directory_impl(path, iterable):
    size = 0
    for line in iterable:
        cmd = line[:-1].split(' ')
        if cmd[0] == '$' and cmd[1] == 'cd' and cmd[2] != '..':
            for subdir, subdir_size in _parse_directory_impl(path + [cmd[2]], iterable):
                yield subdir, subdir_size
                if len(subdir) == len(path) + 1:
                    size += subdir_size
        elif cmd[0] == '$' and cmd[1] == 'cd' and cmd[2] == '..':
            yield path, size
            return
        elif cmd[0] == '$' and cmd[1] == 'ls':
            pass
        elif cmd[0] == 'dir':
            pass
        else:
            size += int(cmd[0])
    # The special case where we've reached the end of input but no "$ cd .." is found.
    # But since we start by passing in an empty list we need to ignore this for the outermost call.
    if path:
        yield path, size


if sys.hexversion >= 0x03030000:
    def parse_directory_recursive(iterable):
        yield from _parse_directory_impl([], iterable)
else:
    # Python 2 does not support yield from
    def parse_directory_recursive(iterable):
        for item in _parse_directory_impl([], iterable):
            yield item


def parse_directory_iterative(iterable):
    # We will, at some cost to the caller, make a copy of the path when we
    # yield it, or a caller who constucts a list from it will find that all
    # paths are the same object. Use slice syntax rather than copy method
    # to stay compatible with Python 2.
    path = []
    sizes = []
    size = 0
    for line in iterable:
        cmd = line[:-1].split(' ')
        if cmd[0] == '$' and cmd[1] == 'cd' and cmd[2] != '..':
            path.append(cmd[2])
            sizes.append(size)
            size = 0
        elif cmd[0] == '$' and cmd[1] == 'cd' and cmd[2] == '..':
            yield path[::], size
            path.pop()
            size += sizes.pop()
        elif cmd[0] == '$' and cmd[1] == 'ls':
            pass
        elif cmd[0] == 'dir':
            pass
        else:
            size += int(cmd[0])
    while path:
        yield path[::], size
        path.pop()
        size += sizes.pop()
