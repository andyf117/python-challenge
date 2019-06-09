import pandas as pd

dataframe_ = pd.read_csv('election_data.csv')

# `Voter ID`, `County`, and `Candidate`.

#   * The total number of votes cast /

#   * A complete list of candidates who received votes /

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

#Getting the length of voters ID list will give us how many voters voted
votes_cast = dataframe_['Voter ID'].tolist() #ARRAY
votes_cast = len(votes_cast) #Length of the array, and overwrite whats within the variable
print("Votes casts is: " + str(votes_cast))

#Getting the candidates Series
#Then turn it to list
#Delete duplicates
#We'll get the list of candidates

dict_list = []

print("These are the candidates: \n\n")
candidates = dataframe_['Candidate'].tolist()
candidates = list(dict.fromkeys(candidates)) #GIVES US THE UNIQUE VALUES WITHIN THE ARRAY IN THE VARIABLE 'candidates'

for candidate in candidates:
    print(candidate)



candidates_ = dataframe_['Candidate']

for candidate in candidates: #4 Iterations
    print(str(candidate))
    
    frames = dataframe_.loc[dataframe_['Candidate'] == candidate] #Locates the rows/frames that has the item 'khan'
    

    percentage_won = (float(len(frames))/float(len(candidates_)))*100
    
    
    #The located frames are the rows where the candidate in each iteration is voted
    dict_ = {
        "Candidate": candidate,
        "Votes": str(len(frames)),
        "Percentage Won": percentage_won,
    }
    dict_list.append(dict_)


    
print("\n\n\n")

votes = []
for dict_ in dict_list:
    votes.append(int(dict_['Votes']))
    print("Candidate " + str(dict_['Candidate']) + " won " + str(dict_['Votes']) + ' which is ' + str(dict_['Percentage Won']) +"%")


won = max(votes)
index_of_winner = votes.index(won)

print("Winner is: " + str(candidates[index_of_winner]))


