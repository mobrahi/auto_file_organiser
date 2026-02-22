# Automatic File Organizer

A Python script that automatically organizes your Downloads folder by sorting files into categorized folders based on their file types or name patterns.

## 📋 Features

- **Smart Categorization**: Automatically sorts files into appropriate folders (Documents, Images, Videos, etc.)
- **Screenshot Detection**: Special handling for screenshots based on filename patterns
- **Duplicate Handling**: Automatically renames files if a duplicate exists
- **Dry Run Mode**: Preview changes without actually moving files
- **Continuous Monitoring**: Watch folders and organize new files automatically
- **Date-based Organization**: Alternative organization by file modification date
- **Custom Path Support**: Can organize any folder, not just Downloads
- **Logging**: Keeps a record of all file movements

## 🗂️ File Categories

| Category | File Types |
|----------|------------|
| **Documents** | .pdf, .doc, .docx, .txt, .rtf, .odt, .xls, .xlsx, .ppt, .pptx, .csv, .md |
| **Images** | .jpg, .jpeg, .png, .gif, .bmp, .svg, .tiff, .webp, .ico, .heic |
| **Screenshots** | Files containing 'screenshot', 'screen shot', 'captura' in name |
| **Videos** | .mp4, .avi, .mkv, .mov, .wmv, .flv, .webm, .m4v, .mpg, .mpeg |
| **Music** | .mp3, .wav, .flac, .aac, .ogg, .m4a, .wma |
| **Archives** | .zip, .rar, .7z, .tar, .gz, .bz2, .iso, .dmg |
| **Executables** | .exe, .msi, .app, .deb, .rpm, .sh, .bat, .cmd |
| **Code** | .py, .js, .html, .css, .cpp, .c, .java, .php, .rb, .go, .rs, .json, .xml, .yaml |
| **Others** | Files that don't match any category |

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only standard library)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/mobrahi/auto_file_organiser.git
cd auto_file_organiser
```

2. **Make the script executable (Linux/Mac):**
```bash
chmod +x auto_file_organiser.py
```

## 📖 Usage

### Basic Usage

Organize your Downloads folder:
```bash
python auto_file_organiser.py
```

### Command Line Options

| Option   | Description |
|----------|------------|
 -p, --path PATH | Organize a custom folder path
 -d, --dry-run   | Preview changes without moving files
 -m, --monitor   | Monitor mode (organize continuously)
 -i, --interval SECONDS   | Monitoring interval (default: 60 seconds)
-b, --by-date   | Organize by date instead of type
--no-log        | Disable logging

### Examples

Preview changes without moving files:

```bash
python file_organizer.py --dry-run
```

Organize a custom folder:

```bash
python file_organizer.py --path "C:\Users\YourName\Desktop\TestFolder"
```

Continuous monitoring (check every 5 minutes):

```bash
python file_organizer.py --monitor --interval 300
```

Organize by date:

```bash
python file_organizer.py --by-date
```

## ⚙️ Configuration

You can customize file categories by modifying the 

```python
file_categories dictionary in the script:

self.file_categories = {
    "Photos": ['.jpg', '.png', '.gif'],  # Renamed category
    "PDFs": ['.pdf'],  # New specific category
    # Add more as needed
}
```

## 🤖 Automation

### Windows Task Scheduler

Create a scheduled task to run daily:

```bash
schtasks /create /tn "FileOrganizer" /tr "python C:\path\to\file_organizer.py" /sc daily /st 09:00
```

### Cron Job (Linux/Mac)

Add to crontab to run daily at 9 AM:

```bash
0 9 * * * /usr/bin/python3 /path/to/file_organizer.py
```

### LaunchAgent (Mac)

Create a plist file in ~/Library/LaunchAgents/ for continuous monitoring.

## 📝 Logging

The script creates a log file file_organizer.log in the same directory, recording:

- All file movements
- Errors and warnings
- Organization statistics

## 🛠️ How It Works

1. Scans the specified folder (default: Downloads)
2. For each file, determines its category based on extension or name
3. Creates category folders if they don't exist
4. Moves files to appropriate folders
5. Handles duplicate filenames by adding numbers
6. Logs all actions

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

- Add new file categories
- Improve screenshot detection patterns
- Add support for more file types
- Enhance the monitoring feature
- Improve error handling
- Add tests

## 📄 License

This project is licensed under the MIT License - see the **LICENSE** file for details.


## ⚠️ Disclaimer

Always use the --dry-run option first to preview changes. The author is not responsible for any accidental file loss.

## 📬 Contact

GitHub: @mobrahi
Project Link: https://github.com/mobrahi/auto_file_organiser

## 🙏 Acknowledgments

Inspired by the need for a tidy Downloads folder
Thanks to all contributors and users

## ⭐ Star this repository if you find it useful!