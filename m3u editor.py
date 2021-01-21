import re
import linecache



def processFile():
    counter = 0
    uniqueGroupList = []
    lineNumberList = []
    languages = ['YOUR PLAYLISTS'

                 ]
    with open("list.m3u", "r", encoding="utf-8") as listFile:
        with open ("resultList.m3u", "a", encoding="utf-8") as destFile:
            for line in listFile:
                counter += 1
                if "group-title" in line:
                    resultList = re.findall(r'"([^"]*)"', line)
                    languageTitle = resultList[3]
                    if languageTitle not in uniqueGroupList:
                        uniqueGroupList.append(languageTitle)
                    if languageTitle in languages:
                        lineNumberList.append(counter)

                else:
                    continue
            for lineNumber in lineNumberList:
                line = linecache.getline('list.m3u', lineNumber)
                destFile.write(line)
                line = linecache.getline('list.m3u', lineNumber+1)
                destFile.write(line)
            print(uniqueGroupList)
            print(lineNumberList)

if __name__ == '__main__':
    processFile()


