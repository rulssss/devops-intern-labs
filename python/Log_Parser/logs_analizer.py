# AI tips:
# The advantage is that it closes automatically, even if an unexpected error occurs in the process:
#def open_file(file_name):
#    with open(file_name, "r") as m:
#       return m.readlines()

# Store the array as tuples:
#  array.append((date, hour, error)) # You add the entire tuple

#for date, hour, error in array:
#   m.write(f"\n- [{date} {hour}] {error}")


def open_file(name):
    text = ""

    m = open(name, "rt")
    text = m.readlines()
    m.close()
    return text


def save_results(name, array):
    m = open(name, "wt")

    c = len(array)

    m.write(f"--- ERRORS ---\nTotal errors: {c}\nList:")

    for date, hour, error in array:
        m.write(f"\n- [{date} {hour}] {error}")

    m.close()


def principal():

    file = open_file("server.log")

    array = []

    for line in file:
        words = line.split()

        for word in words:

            if word == "ERROR":

                date = words[0]
                hour = words[1]
                error = " ".join(words[3:])

                array.append((date, hour, error))

    print("Array : ", array)
    count = len(array)
    print("errors: ", count)

    save_results("errors_report.txt", array)


if __name__ == "__main__":
    principal()
    print("end.")
