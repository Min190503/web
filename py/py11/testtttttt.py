with open("D:/abc.txt", "r", encoding="utf-8") as f_in, open("D:/xyz.txt", "w", encoding="utf-8") as f_out:
    for line in f_in:
        line = line.rstrip()
        if len(line) <= 80:
            f_out.write(line + "\n")
        else:
            while len(line) > 80:
                last_space_index = line[:80].rfind(" ")
                if last_space_index == -1:
                    last_space_index = 80
                f_out.write(line[:last_space_index] + "\n")
        line = line[last_space_inindex + 1 :]
        f_out.write(line + "\n")