def mean(a):
    if(len(a) == 0):
        return 0
    else:
        sum = 0.0
        for i in a :
            sum += i
        return sum/len(a)

def sd(mean, a):
    sqrt_add = 0.0
    for i in a:
        sqrt_add += (i - mean) ** 2
    return (sqrt_add/len(a))**0.5

def display(test, assign):
    tests = len(test)
    assigns = len(assign)
    weight = 0.0
    print("Type        #    min    max    avg   std")
    print("========================================= ")
    if(tests != 0):
        test_min = min(test)
        test_max = max(test)
        test_avg = mean(test)
        test_sd = sd(test_avg, test)
        weight += test_avg * 0.6
        print("Tests        %d    %.2f    %.2f    %.2f    %.2f"%(tests, test_min, test_max, test_avg, test_sd))
    else:
        test_min = "n/a"
        test_max = 'n/a'
        test_avg = "n/a"
        test_sd = "n/a"
        print("Tests        0    n/a    n/a    n/a    n/a")
    if(assigns != 0):
        assign_min = min(assign)
        assign_max = max(assign)
        assign_avg = mean(assign)
        assign_sd = sd(assign_avg, assign)
        weight += assign_avg * 0.4
        print("Programs     %d    %.2f    %.2f    %.2f    %.2f" %(assigns, assign_min, assign_max, assign_avg, assign_sd))
    else:
        assign_min = 'n/a'
        assign_max = 'n/a'
        assign_avg = "n/a"
        assign_sd = "n/a"
        print("Programs     0    n/a    n/a    n/a    n/a")
    print()
    print("the weighted score is ==> %.2f"%(weight))

def main():
    scores = [ ]
    assign_scores = [ ]
    while True:
        print()
        print("        Grade Menu")
        print("1 - Add a Test")
        print("2 - Remove a Test")
        print("3 - Clear Tests")
        print("4 - Add an Assignment")
        print("5 - Remove an Assignment")
        print("6 - Clear Assignments")
        print("D - Display Scores")
        print("Q - Quit")
        print()
        user_input = input("===> ")

        if (user_input == '1'):
            print()
            ar = float(input("Enter the new Test score 0-100 ===> "))
            while (ar < 0):
                ar = float(input("Enter the new Test score 0-100 ===> "))
            scores.append(ar)
        elif (user_input == '2'):
            print()
            ar = float(input("Enter the Test score to remove 0-100 ===> "))
            cleared = False
            for i in scores:
                if (i == ar):
                    scores.remove(ar)
                    cleared = True
            if(cleared == False):
                print("Could not find that score to remove")
        elif(user_input == '3'):
            scores.clear()
        elif(user_input == '4'):
            print()
            ar = float(input("Enter the new Assignment score 0-100 ===> "))
            while (ar < 0):
                ar = float(input("Enter the new Assignment score 0-100 ===> "))
            assign_scores.append(ar)
        elif (user_input == '5'):
            print()
            ar = float(input("Enter the Assignment to remove 0-100 ===> "))
            cleared = False
            for i in assign_scores:
                if (i == ar):
                    assign_scores.remove(ar)
                    cleared = True
            if(cleared == False):
                print("could not find that score to remove")
        elif (user_input == '6'):
            assign_scores.clear()
        elif(user_input == 'D' or user_input == 'd'):
            display(scores, assign_scores)

        elif(user_input == 'Q' or user_input == 'q'):
            break
        else:
            print("Please choose a valid option.")

main()
            
