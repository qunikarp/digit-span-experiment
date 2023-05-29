import csv
import Levenshtein


# Open the input file
with open('Experiment-results.csv', 'r') as input_file:
  # Create a CSV reader
  reader = csv.reader(input_file)

  # Create a list to store the updated rows
  updated_rows = []

  # Iterate over the rows and update similarity and correctness
  for row in reader:
    
    # Get the correct_response and response from columns C and D
    correct_response = row[2] # Index number depends on the CSV
    response = row[3] # Index number depends on the CSV

    # Calculate similarity and correctness
    distance = Levenshtein.distance(correct_response, response)
    similarity = 1 - (distance / len(correct_response))

    correct_digits = sum(1 for c1, c2 in zip(correct_response, response)
                         if c1 == c2)
    correctness = correct_digits / len(correct_response)

    # Update the similarity and correctness values in the row
    row.append(str(similarity))  # Add similarity value at the end
    row.append(str(correctness))  # Add correctness value at the end

    # Append the updated row to the list
    updated_rows.append(row)

# Write the updated rows to a new CSV file
with open('Updated-results.csv', 'w', newline='') as output_file:
  writer = csv.writer(output_file)
  writer.writerows(updated_rows)
