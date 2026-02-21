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



