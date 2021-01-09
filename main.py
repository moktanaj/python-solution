import sys
import csv
import json
import analysis


def open_file(filename, mode):
    try:
        file = open(filename, mode)
        return file
    except Exception as e:
        close_file_and_exit(None, "Error in file operation " + str(e))


def close_file_and_exit(filename_handler, error_msg):
    print("Error: ", error_msg)
    if filename_handler:
        try:
            filename_handler.close()
        except Exception as e:
            print("Error closing file.")
            sys.exit(1)
    sys.exit(1)

# Reading from csv file and creating a DataDict Dictionary.


def read_csv(filename):

    data = {}
    file_handler = open_file(filename, 'r')
    csv_rows = csv.DictReader(file_handler)
    for csv_row in csv_rows:
        if "user_pseudo_id" in csv_row:
            user_pseudo_id = csv_row["user_pseudo_id"]
            data[user_pseudo_id] = csv_row

    file_handler.close()
    return data


# # Creating a sandbox.json file using dataDict Dictionary variable.

def write_json(filename):
    #
    data_dict = {"sandbox-installs": read_csv(filename)}
    json_file_handler = open_file("data/sandbox.json", "w")
    # exception handling for writing json file
    try:
        json_file_handler.write(json.dumps(data_dict, indent=4))
    except Exception as e:
        close_file_and_exit(json_file_handler, "Error while writing json data " + str(e))

    json_file_handler.close()


# Generate a SQL insert statement for all rows in the CSV file

def sql_insert_statement(filename):
    csv_rows = None
    insert_file_handler = open_file(filename, 'r')
    try:
        csv_rows = csv.reader(insert_file_handler, delimiter=',')
    except Exception as e:
        close_file_and_exit(insert_file_handler, "Error reading file as CSV " + str(e))

    # skipping the header
    next(csv_rows)
    for row in csv_rows:
        for i in range(len(row)):
            if row[i] == "":
                row[i] = "NULL"

        print("INSERT INTO table_name VALUES %r;" % (tuple(row),))
        # sys.exit(1)
    insert_file_handler.close()
    # close_file_and_exit(insert_file_handler, "Error reading file as CSV ")


def main():
    msg = """
    usage: {} <file_name.csv>
    example: {} data/example.csv
    example: {} -h

    
    """.format(sys.argv[0],sys.argv[0], sys.argv[0])

    if len(sys.argv) != 2:
        print("usage: " + sys.argv[0] + " <file_name.csv>")

        sys.exit(1)
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print(msg)
        sys.exit(0)
    filename = sys.argv[1]
    write_json(filename)
    print("Json file created")
    sql_insert_statement(filename)
    csv_test_dict = read_csv(filename)
    print(csv_test_dict)
# Analysis module functions
    analysis.main_analysis(filename)


if __name__ == "__main__":
    main()
