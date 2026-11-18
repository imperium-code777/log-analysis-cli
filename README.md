# Log Analysis CLI

A lightweight Python command-line utility designed to parse system or application log files, track event frequencies, and summarize critical errors or warnings.

## Features
- Scans plain text log files line by line efficiently.
- Counts total lines processed, warnings, and errors.
- Displays a concise summary list of top errors for fast debugging.

## Requirements
- Python 3.x

## Usage
Run the script from your terminal providing the path to your log file:

```bash
python analyzer.py path/to/logfile.log
