def get_data():
    input_list = []
    input_list.append(int(input("How many houses with 0 occupants: ")))
    input_list.append(int(input("How many houses with 1 occupant: ")))
    input_list.append(int(input("How many houses with 2 occupants: ")))
    input_list.append(int(input("How many houses with 3 occupants: ")))
    input_list.append(int(input("How many houses with 4 occupants: ")))
    input_list.append(int(input("How many houses with 5 occupants: ")))
    input_list.append(int(input("How many houses with 6 occupants: ")))
    input_list.append(int(input("How many houses with 6+ occupants: ")))
    
    return input_list

thedata = get_data()



def cal_percentage():
    percentage_list = []
    totalhouses = sum(thedata)
    for i in thedata:
        percentage_list.append(round(i/totalhouses*100,1))
    return percentage_list

thepercentages = cal_percentage()


def display_results():
    
    perc0,perc1,perc2,perc3,perc4,perc5,perc6,perc6more = thepercentages
    sentance1 = '{:>12} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7} '.format('Occupants:','0','1','2','3','4','5','6','>6')
    sentance2 = '{:>12} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7} '.format('No. houses:',*thedata)
    sentance3 = '{:>12} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7} '.format('Percentage:',str(perc0)+"%",str(perc1)+"%",str(perc2)+"%",str(perc3)+"%",str(perc4)+"%",str(perc5)+"%",str(perc6)+"%",str(perc6more)+"%")
    print(sentance1)
    print(sentance2)
    print(sentance3)
    
    
display_results()