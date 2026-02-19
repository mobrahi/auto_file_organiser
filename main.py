import os
import shutil
import time
import logging
from pathlib import Path
import argparse
from datetime import datetime

class FileOrganizer:
    def __init__(self, downloads_path=None, log_enabled=True):
        """
        Initialize the File Organizer
        
        Args:
            downloads_path: Path to Downloads folder (uses default if None)
            log_enabled: Enable/disable logging
        """
        # Set up downloads path
        if downloads_path is None:
            self.downloads_path = str(Path.home() / "Downloads")
        else:
            self.downloads_path = downloads_path
        
        # Set up logging
        if log_enabled:
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(message)s',
                handlers=[
                    logging.FileHandler('file_organizer.log'),
                    logging.StreamHandler()
                ]
            )
            self.logger = logging.getLogger(__name__)
        else:
            self.logger = None
        
        # Define file categories and their extensions
        self.file_categories = {
            "Documents": [
                '.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt',
                '.xls', '.xlsx', '.ppt', '.pptx', '.csv', '.md'
            ],
            "Images": [
                '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg',
                '.tiff', '.webp', '.ico', '.heic'
            ],
            "Screenshots": [
                'screenshot', 'screen shot', 'screen capture',
                'captura', 'print screen'
            ],
            "Videos": [
                '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv',
                '.webm', '.m4v', '.mpg', '.mpeg'
            ],
            "Music": [
                '.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a',
                '.wma'
            ],
            "Archives": [
                '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2',
                '.iso', '.dmg'
            ],
            "Executables": [
                '.exe', '.msi', '.app', '.deb', '.rpm', '.sh',
                '.bat', '.cmd'
            ],
            "Code": [
                '.py', '.js', '.html', '.css', '.cpp', '.c',
                '.java', '.php', '.rb', '.go', '.rs', '.swift',
                '.json', '.xml', '.yaml', '.yml'
            ],
            "Others": []
        }
        
        # Create category folders if they don't exist
        self.create_category_folders()
    
    def log(self, message, level='info'):
        """Log messages if logging is enabled"""
        if self.logger:
            if level == 'info':
                self.logger.info(message)
            elif level == 'error':
                self.logger.error(message)
            elif level == 'warning':
                self.logger.warning(message)
        else:
            print(message)
    
    def create_category_folders(self):
        """Create folders for each category in Downloads"""
        for category in self.file_categories.keys():
            folder_path = os.path.join(self.downloads_path, category)
            if not os.path.exists(folder_path):
                try:
                    os.makedirs(folder_path)
                    self.log(f"Created folder: {category}")
                except Exception as e:
                    self.log(f"Error creating folder {category}: {e}", 'error')
    
    def get_file_category(self, filename):
        """
        Determine the category of a file based on its extension or name
        
        Args:
            filename: Name of the file
            
        Returns:
            Category name as string
        """
        file_lower = filename.lower()
        
        # Check for screenshots first (based on name patterns)
        if any(keyword in file_lower for keyword in self.file_categories["Screenshots"]):
            return "Screenshots"
        
        # Check by extension
        file_ext = os.path.splitext(filename)[1].lower()
        for category, extensions in self.file_categories.items():
            if category != "Screenshots":  # Skip as we already checked
                if file_ext in extensions:
                    return category
        
        return "Others"
    
    def organize_files(self, dry_run=False):
        """
        Organize files in the Downloads folder
        
        Args:
            dry_run: If True, only show what would be done without moving files
            
        Returns:
            Dictionary with statistics about organized files
        """
        stats = {
            'moved': 0,
            'skipped': 0,
            'errors': 0,
            'categories': {}
        }
        
        self.log(f"Starting organization of: {self.downloads_path}")
        if dry_run:
            self.log("DRY RUN MODE - No files will be moved")
        
        try:
            # Get all files in Downloads (excluding folders)
            items = os.listdir(self.downloads_path)
            files = [f for f in items if os.path.isfile(os.path.join(self.downloads_path, f))]
            
            for filename in files:
                file_path = os.path.join(self.downloads_path, filename)
                
                # Skip the script itself and log file
                if filename == os.path.basename(__file__) or filename == 'file_organizer.log':
                    stats['skipped'] += 1
                    continue
                
                # Get file category
                category = self.get_file_category(filename)
                
                # Skip if file is already in its category folder
                if os.path.dirname(file_path) == os.path.join(self.downloads_path, category):
                    stats['skipped'] += 1
                    continue
                
                # Prepare destination
                dest_folder = os.path.join(self.downloads_path, category)
                dest_path = os.path.join(dest_folder, filename)
                
                # Handle duplicate filenames
                if os.path.exists(dest_path):
                    name, ext = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(dest_path):
                        new_filename = f"{name}_{counter}{ext}"
                        dest_path = os.path.join(dest_folder, new_filename)
                        counter += 1
                
                if dry_run:
                    self.log(f"[DRY RUN] Would move: {filename} -> {category}/")
                    stats['moved'] += 1
                else:
                    try:
                        shutil.move(file_path, dest_path)
                        self.log(f"Moved: {filename} -> {category}/")
                        stats['moved'] += 1
                        
                        # Update category statistics
                        if category in stats['categories']:
                            stats['categories'][category] += 1
                        else:
                            stats['categories'][category] = 1
                            
                    except Exception as e:
                        self.log(f"Error moving {filename}: {e}", 'error')
                        stats['errors'] += 1
            
            self.log(f"\nOrganization complete!")
            self.log(f"Files moved: {stats['moved']}")
            self.log(f"Files skipped: {stats['skipped']}")
            self.log(f"Errors: {stats['errors']}")
            
            if not dry_run and stats['moved'] > 0:
                self.log("\nFiles moved by category:")
                for category, count in stats['categories'].items():
                    self.log(f"  {category}: {count}")
            
            return stats
            
        except Exception as e:
            self.log(f"Error accessing Downloads folder: {e}", 'error')
            return stats
    
    def monitor_and_organize(self, interval_seconds=60):
        """
        Continuously monitor the Downloads folder and organize new files
        
        Args:
            interval_seconds: Time between scans in seconds
        """
        self.log(f"Starting continuous monitoring (interval: {interval_seconds}s)")
        self.log("Press Ctrl+C to stop")
        
        try:
            while True:
                self.organize_files()
                self.log(f"Waiting {interval_seconds} seconds until next scan...")
                time.sleep(interval_seconds)
        except KeyboardInterrupt:
            self.log("\nMonitoring stopped by user")
    
    def organize_by_date(self, date_format='%Y-%m'):
        """
        Organize files by date (year-month)
        
        Args:
            date_format: Format for date-based folders
        """
        files = [f for f in os.listdir(self.downloads_path) 
                if os.path.isfile(os.path.join(self.downloads_path, f))]
        
        for filename in files:
            file_path = os.path.join(self.downloads_path, filename)
            
            # Get file modification time
            mod_time = os.path.getmtime(file_path)
            date_folder = datetime.fromtimestamp(mod_time).strftime(date_format)
            
            dest_folder = os.path.join(self.downloads_path, f"Date_{date_folder}")
            
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            
            dest_path = os.path.join(dest_folder, filename)
            
            # Handle duplicates
            if os.path.exists(dest_path):
                name, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(dest_path):
                    new_filename = f"{name}_{counter}{ext}"
                    dest_path = os.path.join(dest_folder, new_filename)
                    counter += 1
            
            try:
                shutil.move(file_path, dest_path)
                self.log(f"Moved by date: {filename} -> {date_folder}/")
            except Exception as e:
                self.log(f"Error moving {filename}: {e}", 'error')

def main():
    parser = argparse.ArgumentParser(description='Automatic File Organizer for Downloads')
    parser.add_argument('--path', '-p', help='Custom path to organize (default: Downloads folder)')
    parser.add_argument('--dry-run', '-d', action='store_true', help='Preview changes without moving files')
    parser.add_argument('--monitor', '-m', action='store_true', help='Monitor mode (organize continuously)')
    parser.add_argument('--interval', '-i', type=int, default=60, help='Monitoring interval in seconds')
    parser.add_argument('--by-date', '-b', action='store_true', help='Organize by date instead of type')
    parser.add_argument('--no-log', action='store_true', help='Disable logging')
    
    args = parser.parse_args()
    
    # Create organizer instance
    organizer = FileOrganizer(
        downloads_path=args.path,
        log_enabled=not args.no_log
    )
    
    # Execute based on arguments
    if args.by_date:
        organizer.organize_by_date()
    elif args.monitor:
        organizer.monitor_and_organize(args.interval)
    else:
        organizer.organize_files(dry_run=args.dry_run)

if __name__ == "__main__":
    main()