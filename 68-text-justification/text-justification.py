class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        initial_words = words.copy()
        current_space = 0
        length_count = []
        current_line = []
        result=[]
        for i in words:
            length_count.append(len(i))
        while initial_words:
            """print(initial_words)
            print(result)
            print(current_space)"""
            while current_space <= maxWidth:
                if initial_words:
                    current_word = initial_words[0]
                    '''print(current_word)
                    print(result)'''
                    if (current_space == 0 and len(current_word) == maxWidth) or (len(current_word) + current_space < maxWidth):
                        current_line.append(current_word)
                        initial_words.pop(0)
                        if current_space == 0:
                            current_space+= len(current_word)
                        else:
                            current_space += len(current_word) +1
                    else:
                        result.append(current_line)
                        current_space = 0
                        break
                else:
                    result.append(current_line)
                    current_space = 0
                    break
            current_line = []
        print(result)
        final_result = []
        for i in range(len(result)-1):
            final_line = ""
            current_space = maxWidth
            words_count = len(result[i])
            for word in result[i]:
                current_space -= len(word)
            if words_count > 1:
                each_space = current_space // (words_count-1)
            else:
                each_space = 1
            if words_count > 1:
                extra_space = current_space % (words_count-1)
            else:
                extra_space = 0
            for word in range(len(result[i])):
                if extra_space != 0:
                    if final_line != "":
                        final_line= final_line+" "*(each_space+1)+result[i][word]
                        extra_space += -1
                    else:
                        final_line = final_line+result[i][word]
                else:
                    if final_line:
                        final_line= final_line+" "*each_space+result[i][word]
                    else:
                        final_line = final_line+result[i][word]
            if len(final_line) < maxWidth:
                final_line += " " * (maxWidth-len(final_line))
            final_result.append(final_line)
            '''print(each_space)
            print(current_space)'''
        final_line = ""
        for word in result[-1]:

            if final_line:
                final_line = final_line + " " +word
            else:
                final_line = final_line + word
        if len(final_line) < maxWidth:
            final_line += " " * (maxWidth - len(final_line))
        final_result.append(final_line)
        return final_result