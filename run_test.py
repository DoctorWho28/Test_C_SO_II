import os

LEN_TEXT=10000
FLAG_PAR="-p"

def test_comp1_mono(file):
    print("Testando file:",file,"compito 1 monoprocesso")
    os.system(f'./ANSI-C -1 input/{file} csv/{file.removesuffix(".txt")}.csv')
    print("Creato file")
    if not os.path.exists(f'expected_csv/{file.removesuffix(".txt")}_expected.csv'):
        if os.path.exists(f'csv/{file.removesuffix(".txt")}.csv'):
            print("Test fallito! Csv non dovrebbe essere presente\n")
            return 0
        else:
            print("Test passato!\n")
            return 1
        

    with open(f'expected_csv/{file.removesuffix(".txt")}_expected.csv',"r")as F:
        lines_expected=F.readlines()
    if os.path.exists(f'csv/{file.removesuffix(".txt")}.csv'):
        with open(f'csv/{file.removesuffix(".txt")}.csv',"r") as F:
            lines_c=F.readlines()
    else:
        print("Test fallito! Csv dovrebbe essere presente\n")
        return 0
    

    passed=True
    line_wrong=[]
    for i,line in enumerate(lines_c):
        tmp_line=line.split(",")
        line=[tmp_line[0]]
        for j in range(1,len(tmp_line),2):
            line.append(tmp_line[j]+","+tmp_line[j+1])
        for word in line:
            if word not in lines_expected[i]:
                passed=False
                if i+1 not in line_wrong:
                    line_wrong.append(i+1)
    if passed:
        print("Test passato!\n")
        return 1
    else:
        print("Test fallito! Linee sbagliate:")
        for ind in line_wrong:
            print(ind)
            print("\n")
        return 0



def test_comp2_mono(file):
    print("Testando file:",file,"compito 2 monoprocesso")
    os.system(f'./ANSI-C -2 csv/{file} random_text/{file.removesuffix(".csv")}_random.txt {LEN_TEXT}')
    if not os.path.exists(f'random_text/{file.removesuffix(".csv")}_random.txt'):
        print("Test fallito! Txt dovrebbe essere presente\n")
        return 0
    with open(f'csv/{file}',"r") as F:
        lines_csv=F.readlines()
    with open(f'random_text/{file.removesuffix(".csv")}_random.txt',"r") as F:
        line_txt=F.readline()
    words={}
    for line in lines_csv:
        split_line=line.split(",")
        words[split_line[0]]=[]
        for j in range(1,len(split_line),2):
            words[split_line[0]].append(split_line[j])#aggiusta
    word_txt=line_txt.split()
    word_final=[]
    for word in word_txt:
        word_final.append(word.lower())
    
    
    if(len(word_final)!=LEN_TEXT):
        print(f'Test fallito! Il testo è lungo {len(word_final)} al posto di{LEN_TEXT}')
        return 0

    passed=True
    word_wrong=[]
    for i in range(1,len(word_final)):
        if word_final[i] not in words[word_final[i-1]]:
            passed=False
            word_wrong.append((word_final[i-1],word_final[i]))
    if passed:
        print("Test passato!\n")
        return 1
    else:
        print("Test fallito! Parole sbagliate:")
        for ind in word_wrong:
            print(ind[1]+"non successiva a"+ind[0]+"nel csv\n")
            print("\n")
        return 0

    



if __name__=="__main__":
    tot_test=0
    test_passed=0
    for file in os.listdir("input"):
        tot_test+=1
        test_passed+=test_comp1_mono(file)
    for file in os.listdir("csv"):
        tot_test+=1
        test_passed+=test_comp2_mono(file)
    

    print("\n\n\nPassati",test_passed,"/",tot_test)

                