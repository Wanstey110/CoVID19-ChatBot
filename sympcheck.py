def sympcheck():
    print("Welcome to the COVID19 symptom checker\nHave you ever experienced these symptoms?")
    symlist=['Coughing','Fever','Shortness of breath','Sore throat','Headache','Loss of taste or smell','Fatigue','Muscle and/or body aches','Runny/stuffy nose','Sneezing','Itchy, red, watery eyes','Itchy and runny nose' ]
    num=0
    for i in symlist:
        num+=1
        print(f'{num}. {i}')
    symptoms = input('If yes, please select the symptoms you have been feeling using their number, and seperate each symptom with a comma (no spaces).\nIf you do not experience any of these symptoms, simply type no, and you will be returned to main menu.')
    if symptoms == 'no' or symptoms =='No':
        return 'You said you have none of these symptoms. You are most likely in a fine condition. Keep in mind this is not a professional diagnosis and consult your doctor if you are feeling very ill '
    cheeseburger = symptoms.split(',')
    print('You have mentioned that you have:')
    clength = len(cheeseburger)
    flag = True
    while flag:
            for i in range(len(cheeseburger)):
                if i == clength - 1:
                    print(f'{symlist[int(cheeseburger[i])-1]}.', end='')
                else:
                    print(f'{symlist[int(cheeseburger[i])-1]}, ', end='')

            flag = False

    
    print(' ')
    print()
    if ("1" in cheeseburger and "2" in cheeseburger and "3" in cheeseburger) or ("3" in cheeseburger and ("1" in cheeseburger or "7" in cheeseburger or "8" in cheeseburger)):
        return 'If you are experiencing Fever, Cough, Shortness of breath and/or muscle pain and body aches, these are all symptoms of the coronavirus. If these are mild, try self isolating, while if these are serious, I advise you to go see a doctor immediately.'
    elif "11" not in cheeseburger and "12" not in cheeseburger:
        return 'You may be suffering from the flu. The flu has all the symptoms listed above, except for shortnes for breath, or itchiness. If you are only experiencing sneezing and/or itchiness, chest tightness, or coughing, perhaps you may be alergic or asmatic. Keep in mind this is not a professional diagnosis and consult your doctor if you are feeling very ill.'
    elif "11" in cheeseburger or "12" in cheeseburger:
        return "Don't worry, if you're only experiencing itchy and runny nose and itchy red watery eyes, then you're suffering from an allergy. Sneezing might also be a symptom of it, and constant couging or chest tightness along with the previous symptoms mentioned might mean youre asmatic. Keep in mind this is not a professional diagnosis and consult your doctor if you are feeling very ill."
    else:
        return 'If you are only experiencing sneezing and/or itchiness or chest tightness perhaps you may be alergic or asmatic. The amin symptoms of coronavirus are difficulty breathing, coughing and fever. The main difference with flu is the fact that the coronavirus targets the cells in your lungs, so while flu does not have the symptom of chest tightness and shortness of breath, the coronavirus does. Keep in mind that this is not a professional diagnosis and consult your doctor if you are feeling very ill '

if __name__ == "__main__":
    x = sympcheck()
    print(x)
