   #! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.

import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range (3):
    #quiz and  anwer key

    quizFile= open('capitalsquiz%s.txt' % (quizNum+1), 'w')
   # answerKeyFile = open('capitalsquiz_answer%s' % (quizNum +1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
    #header for quiz
    quizFile.write ("Name:\n\nDate:\n\nPeriod:\n\n")
    quizFile.write((" "*20)+"State Capital Quiz (Form %s)" %(quizNum +1))
    quizFile.write("\n\n")

                   
    #shuffle states
    states=list(capitals.keys())
    random.shuffle(states)

    
    #makea  question for each
    for questionNum in range (50):
        #right and wrong answers
        correctAnswer=capitals[states[questionNum]] #goes to dict using state ie. capitals["alabama"]
        wrongAnswers=list(capitals.values())  #gives a list of all capitals (the values)
        del wrongAnswers[wrongAnswers.index(correctAnswer)] #this is tricky, first it gives the index of correct
        #and then modfied the wrong answer list to REMOVE that answer from it,
        #ie 0 = montgomery for correct
        #, then uses montogmry to find whatever index it is, and deletes it
        wrongAnswers = random.sample(wrongAnswers, 3) # pick 3 random ones of the 49
        answerOptions= wrongAnswers+ [correctAnswer]   #so what happens is c.a. is a string, its converted to a list here 
        random.shuffle(answerOptions)




        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Write out the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
##
##        quizFile.write("%s  What is the capital of %s? \n" %(questionNum +1, states[questionNum]))                    
##        for i in range(4):
##            quizFile.write(" %s. %s\n" % ("ABCD"[i], answerOptions[i]))
##        quizFile.write("\n")
####        for i in range(4):
####            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
####            quizFile.write('\n')
##
##            #answer key to file
##        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
##        #answerKeyFile.write("%s. %s\n" %(questionNum +1, "ABCD"[answerOptions.index(correctAnswer)]))
##    quizFile.close()
##    answerKeyFile.close()

                               
