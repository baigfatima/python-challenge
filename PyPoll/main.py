import csv

file_to_load = "raw_data/election_data.csv"
file_to_output = "analysis/election_analysis.txt"

total_votes = 0

candidate_choices = []
candidate_votes = []

winning_candidate = ""
winning_count = 0

with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:

        print(".", end=""),
        total_votes = total_votes + 1
        candidate_name = row["Candidate"]
        if candidate_name not in candidate_choices:
            candidate_choices.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(file_to_output, "w") as txt_file:

    election_results = (
        f"\n\nElection Results\n"
        f"----------------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"----------------------------------------\n")

    print(election_results, end="")

    txt_file.write(election_results)

    for candidate in candidate_votes:

        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) + 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

            voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
            print(voter_output, end="")

            txt_file.write(voter_output)

        winning_candidate_summary = (
            f"----------------------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"----------------------------------------\n")
        print(winning_candidate_summary)

        txt_file.write(winning_candidate_summary)

