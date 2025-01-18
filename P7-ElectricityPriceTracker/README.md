# Electricity Price Tracker

This Python script fetches real-time electricity prices and identifies the cheapest upcoming hours for electricity consumption.

## Description

The Electricity Price Tracker is a Python utility that:

- Retrieves current electricity prices from an API
- Processes and formats the timestamp data
- Identifies the 5 cheapest upcoming hours
- Displays results in an easy-to-read format with prices in cents per kilowatt-hour (c/KWh)

## Prerequisites

- Python 3.6 or higher
- `requests` library
- Internet connection to access the API

## Installation

1. Clone this repository or download the script
2. Install the required package:

```bash
pip install requests
```

## Configuration

Before running the script, you need to:

1. Set up your API_URL in the script
2. Ensure your timezone settings are correct (currently set to UTC+2)

## Usage

Run the script using Python:

```bash
python electricity_tracker.py
```

The script will output:

- Confirmation when data is received
- A list of the 5 cheapest upcoming hours with their corresponding prices

Example output:

```
data received

Cheapest 5 upcoming hours:

1. 15.01 Klo: 23:00 - 3.45 c/KwH
2. 15.01 Klo: 22:00 - 3.67 c/KWH
3. 16.01 Klo: 02:00 - 3.89 c/KWH
4. 16.01 Klo: 03:00 - 4.12 c/KWH
5. 16.01 Klo: 01:00 - 4.23 c/KWH
```

## Features

- Real-time price data fetching
- Automatic timezone adjustment (UTC+2)
- Sorting of prices to find cheapest hours
- Formatted datetime display
- Focus on upcoming hours only

## Code Structure

- `get_prices()`: Main function that:
  - Fetches data from API
  - Processes timestamps
  - Filters for upcoming hours
  - Sorts and displays cheapest hours

## Future Improvements

- Add configuration file for API URL and timezone settings
- Implement price alerts
- Add historical price analysis
- Create visualization of price trends
- Add error handling for API failures
- Implement caching to reduce API calls

## Contributing

Feel free to fork this repository and submit pull requests. You can also open issues for bugs or feature suggestions.

## License

This project is open source and available under the MIT License.

## Author

Aleksi

## Acknowledgments

- Thanks to the electricity price API provider
- Inspired by the need for smart energy consumption
