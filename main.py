import exercise

if __name__ == "__main__":
    csv_parser = exercise.CSVParser()
    csv_parser.read_csv()
    try:
        while True:
            csv_parser.user_menu()
            csv_parser.extra_menu_options()
    except KeyboardInterrupt:
        print("👋 Bye, bye")
