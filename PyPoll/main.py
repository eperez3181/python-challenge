import os
import csv
import string

election_data = os.path.join('Resources', 'election_data.csv')


total_votes = 0
candidate_votes = {}
candidate_list = []
winning_count = 0
winning_candidate = ""


with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:
        
        total_votes = total_votes + 1

        candidates = row[2]

        if candidates not in candidate_list:

            candidate_list.append(candidates)

            candidate_votes[candidates] = 0

        candidate_votes[candidates] = candidate_votes[candidates] + 1


output_file = os.path.join("analysis", "results.txt")

with open(output_file, "w") as txt_file:
  
    
    results = (f"Election Results\n"f"------------------------------\n"f"Total Votes: {total_votes}\n"f"------------------------------\n")
    print(results, end="")

    
    txt_file.write(results)

    
    for name in candidate_votes:

        
        votes = candidate_votes.get(name)
        vote_percentage = float(votes) / float(total_votes) * 100

        
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = name

       
        poll_result = f"{name}: {vote_percentage}% ({votes})\n"
        print(poll_result, end="")

        
        txt_file.write(poll_result)

    
    poll_summary = (f"------------------------------\n"f"Winner: {winning_candidate}\n"f"------------------------------\n")
    print(poll_summary)


    txt_file.write(poll_summary)

    


  
