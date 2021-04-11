yesNo = (input('This is power generator service organizer, would you like to see data? (type "dome howler for model of dome howler"): ')).lower()
if yesNo == 'yes':
     print('Existing and functiong generators are the following: Gas/Nuclear generator, Solar panels ' )
     whichGen = (input('Which generator would you like to inspect?')).lower()
     
     if whichGen == 'gas' or whichGen == 'nuclear':
          import random
          for x in range(1):
               percentage = random.randint(1,100)
               if 10> percentage >= 1 :
                    percentage = str(percentage)
                    print('The Gas generator is producing ' + percentage + '% of the total energy consumption, Poor')
               elif 30> percentage >= 10 :
                    percentage = str(percentage)
                    print('The Gas generator is producing ' + percentage + '% of the total energy consumption, Okay')
               elif 60> percentage >= 30 :
                    percentage = str(percentage)
                    print('The Gas generator is producing ' + percentage + '% of the total energy consumption, Normal')
               elif 75> percentage >= 60 :
                    percentage = str(percentage)
                    print('The Gas generator is producing ' + percentage + '% of the total energy consumption, Better')
               elif 100> percentage >= 75 :
                    percentage = str(percentage)
                    print('The Gas generator is producing ' + percentage + '% of the total energy consumption, Excellent')
     elif whichGen == 'solar panel' or whichGen == 'solar':
          import random
          for x in range(1):
               percentage = random.randint(1,100)
               if 10> percentage >= 1 :
                    percentage = str(percentage)
                    print('The Solar Panels are producing ' + percentage + '% of the total energy consumption, Poor')
               elif 30> percentage >= 10 :
                    percentage = str(percentage)
                    print('The Solar Panels are producing ' + percentage + '% of the total energy consumption, Okay')
               elif 60> percentage >= 30 :
                    percentage = str(percentage)
                    print('The Solar Panels are producing ' + percentage + '% of the total energy consumption, Normal')
               elif 75> percentage >= 60 :
                    percentage = str(percentage)
                    print('The Solar Panels are producing ' + percentage + '% of the total energy consumption, Better')
               elif 100> percentage >= 75 :
                    percentage = str(percentage)
                    print('The Solar Panels are producing ' + percentage + '% of the total energy consumption, Excellent')
elif yesNo == 'no':
    print('Ok,shutting down inspection')
    shutDown = (input('Manual override to continue inspection?')).lower()
    if shutDown == 'yes':
         if yesNo == 'yes':
          print('Existing and functiong generators are the following: Gas/Nuclear generator, Solar panels ' )
          whichGen = input('Which generator would you like to inspect?')
    else:
         print('Override failed, thank you for using service')
         quit()

     

elif yesNo == 'dome howler':
     from PIL import Image
     image = Image.open(r"C:\Users\Aryan\Pictures\domehowler.png")
     image.show()
     
