import sys

def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    from stats import create_report
    create_report(sys.argv[1])

main()