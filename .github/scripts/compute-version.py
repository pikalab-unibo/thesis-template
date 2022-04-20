import sys


def get_command_value(string, command, default=None):
    if command in string:
        return string.split('}{')[1][0:-1]
    else:
        return default


major = None
minor = None
patch = None


def none_is_none(*args):
    return all((it is not None for it in args))


prefix = "version"


with (open(sys.argv[1], mode='r') if len(sys.argv) > 1 else sys.stdin) as file:
    for line in file.readlines():
        line = line.strip()
        if not line.startswith("%"):
            major = get_command_value(line, f"{prefix}major", major)
            minor = get_command_value(line, f"{prefix}minor", minor)
            patch = get_command_value(line, f"{prefix}patch", patch)
            # print(f"'{line.strip()}' -> major={major}, minor={minor}, patch={patch}")
            if none_is_none(major, minor, patch):
                break


print(major, minor, patch, sep='.')
