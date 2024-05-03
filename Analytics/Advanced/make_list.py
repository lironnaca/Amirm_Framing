import csv
import ast


def convert_to_list(string):
    return ast.literal_eval(string)


if __name__ == '__main__':

    with open('combinedData_GPT_result_preprocessed.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        fieldnames = csv_reader.fieldnames

        with open('output_file.csv', 'w', newline='') as output_csv_file:
            csv_writer = csv.DictWriter(output_csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()

            for row in csv_reader:
                row['your_column'] = convert_to_list(row['your_column'])
                csv_writer.writerow(row)

