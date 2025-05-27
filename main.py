import sys

from stats import count_words, count_characters, sort_list
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

book_path = sys.argv[1]


def get_book_text(path):
	try:
		with open(path) as f:
			return f.read()
	except FileNotFoundError:
		print(f"Error: File not found: {path}")
		sys.exit(1)


def main():
	book_text = get_book_text(book_path)
	word_count = count_words(book_text)
	print(f"Found {word_count} total words")

	char_count = count_characters(book_text)
	sorted_char_report = sort_list(char_count)

	for entry in sorted_char_report:
		print(f"{entry['char']}: {entry['num']}")

if __name__ == "__main__":
    main()
