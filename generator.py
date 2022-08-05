#!/usr/bin/env python3

import argparse
from os import path

# Feel free to modify them
delimiters = ["", "-", "_", "."]


def print_banner():
    separator = "#" * 50
    banner_text = "# Potential Usernames Generator v0.1" + " " * 13 + "#\n"
    banner_text += "# By terasi" + " " * 38 + "#\n"
    banner_text += "# https://github.com/tera-si" + " " * 21 + "#"

    print(separator)
    print(banner_text)
    print(separator + "\n")


def check_output_exists(output_file):
    return path.exists(output_file)


def generate(names):
    results = []

    for delimiter in delimiters:
        results.append(names[0] + delimiter + names[-1])
        results.append(names[-1] + delimiter + names[0])
        results.append(names[0][0] + delimiter + names[-1])
        results.append(names[-1][0] + delimiter + names[0])
        results.append(names[0] + delimiter + names[-1][0])
        results.append(names[-1] + delimiter + names[0][0])
        results.append(names[0][0] + delimiter + names[-1][0])
        results.append(names[-1][0] + delimiter + names[0][0])

    return results

def generate_with_case(names):
    results = []

    def cap_full_word(word):
        return word[0].upper() + word[1:]

    def cap_first_char(word):
        return word[0].upper()

    #? Is there another way to do this faster/more automated?
    for delimiter in delimiters:
        results.append(names[0] + delimiter + names[-1])
        results.append(cap_full_word(names[0]) + delimiter + names[-1])
        results.append(names[0] + delimiter + cap_full_word(names[-1]))
        results.append(cap_full_word(names[0]) + delimiter + cap_full_word(names[-1]))

        results.append(names[-1] + delimiter + names[0])
        results.append(cap_full_word(names[-1]) + delimiter + names[0])
        results.append(names[-1] + delimiter + cap_full_word(names[0]))
        results.append(cap_full_word(names[-1]) + delimiter + cap_full_word(names[0]))

        results.append(names[0][0] + delimiter + names[-1])
        results.append(cap_first_char(names[0]) + delimiter + names[-1])
        results.append(names[0][0] + delimiter + cap_full_word(names[-1]))
        results.append(cap_first_char(names[0]) + delimiter + cap_full_word(names[-1]))

        results.append(names[-1][0] + delimiter + names[0])
        results.append(cap_first_char(names[-1]) + delimiter + names[0])
        results.append(names[-1][0] + delimiter + cap_full_word(names[0]))
        results.append(cap_first_char(names[-1]) + delimiter + cap_full_word(names[0]))

        results.append(names[0] + delimiter + names[-1][0])
        results.append(cap_full_word(names[0]) + delimiter + names[-1][0])
        results.append(names[0] + delimiter + cap_first_char(names[-1]))
        results.append(cap_full_word(names[0]) + delimiter + cap_first_char(names[-1]))

        results.append(names[-1] + delimiter + names[0][0])
        results.append(cap_full_word(names[-1]) + delimiter + names[0][0])
        results.append(names[-1] + delimiter + cap_first_char(names[0]))
        results.append(cap_full_word(names[-1]) + delimiter + cap_first_char(names[0]))

        results.append(names[0][0] + delimiter + names[-1][0])
        results.append(cap_first_char(names[0]) + delimiter + names[-1][0])
        results.append(names[0][0] + delimiter + cap_first_char(names[-1]))
        results.append(cap_first_char(names[0]) + delimiter + cap_first_char(names[-1]))

        results.append(names[-1][0] + delimiter + names[0][0])
        results.append(cap_first_char(names[-1]) + delimiter + names[0][0])
        results.append(names[-1][0] + delimiter + cap_first_char(names[0]))
        results.append(cap_first_char(names[-1]) + delimiter + cap_first_char(names[0]))

    return results

def output_to_stdout(results):
    for result in results:
        print(result)

def output_to_file(results, output_file):
    try:
        with open(output_file, "w") as out_file:
            for result in results:
                out_file.write(result + "\n")

    except Exception as e:
        print(f"[!] Error when writing to {output_file}:")
        print(e)
        exit()


def main():
    description = """Generate a list of simple usernames from a list of full
                  names."""
    separator = "=" * 50

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("name_list", help="A list of full names. Each full name must be on a new line; first and last name must be separated by a space; middle names are ignored.")
    parser.add_argument("output_file", help="File name for the output file, optional. If none are provided, will output to STDOUT.", nargs="?")
    parser.add_argument("-c", "--case", help="Enable case sensitive mode. If enabled, generated usernames will contain basic variations in upper and lowercase. Off by default, preserving original casing.", dest="case_switch", action="store_true")
    parser.set_defaults(case_switch=False)

    args = parser.parse_args()
    name_list = args.name_list
    output_file = args.output_file
    case_switch = args.case_switch

    print_banner()

    if output_file:
        if check_output_exists(output_file):
            print(f"[!] Output file {output_file} already exists\n[!] Aborting...")
            exit()

    print(f"[*] Using delimiters: {delimiters}")
    print(separator)

    total_results = []

    try:
        with open(name_list, "r") as in_file:
            for line in in_file:
                if case_switch:
                    line = line.lower()

                names = line.split()

                if not case_switch:
                    results = generate(names)
                else:
                    results = generate_with_case(names)

                total_results += results

            if not output_file:
                output_to_stdout(total_results)
            else:
                output_to_file(total_results, output_file)
                print(f"[*] Output to file {output_file} successful")

    except Exception as e:
        print(f"[!] Error:")
        print(e)
        exit()


if __name__ == "__main__":
    main()
