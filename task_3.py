
#A program that determines what award a partcipate wiill recieve dependant on there total triathlon time.


print("Thank you for participating in this years Triathlon. Please enter the required date below.")
swimming_time = int(input("Please enter swim time in minutes: ")) #An input for each event of the triathlon
cycling_time = int(input("Please enter cycle time in minutes: "))
running_time = int(input("Please enter run time in minutes: "))

total_time = swimming_time + cycling_time + running_time # Calculation to count all the event times to equal a total

if total_time >= 100: # if total time is within qualifying time. print Provincial Colours awarded
    print("Congratulations your time was", total_time ," minutes you have been awarded Provincial Colours.")
elif total_time <=5: # if total time is within 5 minutes of qualifying time. print Provincial half Colours awarded
    print("Congratulations your time was", total_time ,"minutes you have been awarded Provincial Half Colours.")
elif total_time >=10: # if total time is within 10 minutes of qualifying time.  print Provincial Scroll awarded
    print("Congratulations your time was", total_time ,"minutes you have been awarded Provincial Scroll.")
elif total_time + 10: # if total time is more than 10 minutes of qualifying time.  print you haven't qualified for an award
    print("Congratulations your time was", total_time ,"unfortunatley you haven't qualified for an award.")