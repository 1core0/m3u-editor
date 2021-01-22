import re
import linecache


def processFile() -> object:
    counter = 0
    unique_list = []
    line_nr = []
    languages = ['DE Ent',
                 'DE Sports'
                 ]
    with open("list.m3u", "r", encoding="utf-8") as listFile:
        with open("resultList.m3u", "a", encoding="utf-8") as destFile:
            for line in listFile:
                counter += 1
                if "group-title" in line:
                    # split list by space
                    group_title = re.findall(r'(?<=group-title=")(\s)?([A-z]+(\s)?[A-z]*)', line)
                    if group_title:
                        for language in group_title[0]:
                            if not language or " " in language[0]:
                                continue
                            if language not in unique_list:
                                unique_list.append(group_title)
                            if language in languages:
                                line_nr.append(counter)
                    else:
                        continue
                else:
                    continue
            for lineNumber in line_nr:
                line = linecache.getline('list.m3u', lineNumber)
                destFile.write(line)
                line = linecache.getline('list.m3u', lineNumber + 1)
                destFile.write(line)
            print("File has been written")


if __name__ == '__main__':
    processFile()
