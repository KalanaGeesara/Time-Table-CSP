import csv

inputFile = raw_input("Input file path: ")                                                          #path of the file containing input
outputFile = raw_input("Output file path: ")                                                        #path of the file where output isgoing to write
inputFileArray=[]

#reading csv file 
with open(inputFile, 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:                                                                         #reading a row
         string = row[0][1:len(row[0])-1]                                                           #removing unwanted " marks from the begining and the end of the input
         inputFileArray.append(''.join(string).split(','))                                          #appending to a array
        
subject = []
types = {}
timeSlots = {}
room = []


for i in range(len(inputFileArray)-1):                                                              #going through the array except for last index(it contains rooms)
    subject.append(inputFileArray[i][0])                                                            #appending subjects to subject array              
    types[inputFileArray[i][0]] = inputFileArray[i][1]                                              #appending type(c/o) 
    timeSlots[inputFileArray[i][0]] = inputFileArray[i][2:]                                         #appending time slots

room = inputFileArray[len(inputFileArray)-1]                                                        #appending rooms to the room array
timeTable = {}
def recursiveBacktrackingAssignment(timeTable, subjects, rooms, slots, types):
    if(len(timeTable) == len(subjects)):                                                            #check whether assignment is complete or not
       return timeTable                                                                             #if complete return the complete time table
    else:
        for i in subjects:                                                                          #loop through subjects
            if i not in timeTable:                                                                  #check whether subject i is already being assigned or not
                for j in rooms:                                                                     #loop through rooms
                    for k in slots[i]:
                        failure = False
                        for l in iter(timeTable):                                                   #loop through each key value in already assinged time table subjects
                            if(len(timeTable) == len(subjects)):                                                            #check whether assignment is complete or not
                                return timeTable 
                            if timeTable[l] == [k, j]:                                              #check whether another subject has occupied that room and time slot
                                failure = True
                                break
                            if (types[i] == 'c' and types[l] == 'c' and timeTable[l][0] == k):      #check whether two compulsory subjects are going to share same time slot
                                failure = True
                                break
                        if(failure == False):                                                       #check whether prevoius contraints have been violated
                            timeTable[i] = [k, j]                                                   #if not assign the current time slot and room to the subject
                            recursiveBacktrackingAssignment(timeTable, subjects, rooms, slots, types)   #recurse this operation
            
        return timeTable


print recursiveBacktrackingAssignment(timeTable, subject,room, timeSlots,types)
result = recursiveBacktrackingAssignment(timeTable, subject,room, timeSlots,types)

with open(outputFile, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in iter(result):
            spamwriter.writerow([i] + result[i])
