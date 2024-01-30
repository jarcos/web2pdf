# Web Page to PDF Converter

This project is a Python script that scrapes content from a specified web page and its subpages, and then compiles this content into a single PDF document. It's particularly useful for consolidating information from multiple web pages into one easily accessible file.

## Requirements

The script requires the following:

- `python 3.7` or above

## Dependencies

The script relies on several Python libraries:

- `requests`: For making HTTP requests to fetch web pages.
- `beautifulsoup4`: For parsing HTML and extracting information.
- `weasyprint`: For converting HTML content to a PDF file.

## Installation

Before running the script, you'll need to ensure you have Python installed on your system. The script has been tested with Python 3.7 and above.

1. **Clone the repository:**

   ```bash
   git clone [repository-url]
   cd [repository-directory]
   ```

2. **Set up a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install requests beautifulsoup4 weasyprint
   ```

   Note: `WeasyPrint` has additional dependencies that might need to be installed separately. Please refer to the [WeasyPrint Documentation](https://weasyprint.readthedocs.io/en/stable/install.html) for detailed installation instructions.

## Running the Script

To run the script, simply execute it with Python:

```bash
python scraper.py
```

The script will prompt you for the URL of the main page, then scrape content from this page and its subpages, compiling everything into a PDF.

## Customization

You can modify the script to point to different URLs or adjust the PDF settings as per your requirements.

## License

GPL-3.0 License. See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.html) for more information.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## Contact

For any queries or assistance, feel free to open an issue in the repository.
