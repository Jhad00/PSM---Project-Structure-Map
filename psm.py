import os
import sys

# File extensions to skip (binary files)
BINARY_EXTENSIONS = {
    '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp', '.svg',
    '.mp4', '.avi', '.mov', '.wmv', '.mkv', '.flv', '.webm',
    '.mp3', '.wav', '.flac', '.ogg', '.m4a', '.aac',
    '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
    '.zip', '.rar', '.7z', '.tar', '.gz'
}

def explore_directory(directory_path):
    """
    Explore the contents of a directory and export its structure with support for large files.
    """
    if not os.path.exists(directory_path):
        print(f"Error: Path {directory_path} does not exist.")
        return

    output_file = 'project_structure.txt'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("📄 Project Exploration Report\n")
        f.write(f"Path: {directory_path}\n")
        f.write("=" * 50 + "\n\n")

        f.write("📂 Project Structure:\n")
        for root, dirs, files in os.walk(directory_path):
            level = root.replace(directory_path, '').count(os.sep)
            indent = '    ' * level
            relative_path = os.path.relpath(root, directory_path)
            
            if relative_path == '.':
                f.write(f"{indent}📁 {os.path.basename(directory_path)}/\n")
            else:
                f.write(f"{indent}📁 {os.path.basename(root)}/\n")
            
            subindent = indent + '    '
            for file in files:
                f.write(f"{subindent}📄 {file}\n")

        f.write("\n" + "=" * 50 + "\n\n")

        f.write("📄 Text File Contents:\n")
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                ext = os.path.splitext(file)[1].lower()

                if ext in BINARY_EXTENSIONS:
                    # Binary file - do not read content
                    f.write(f"\n🗂️ Binary file: {file_path}\n")
                    continue

                try:
                    with open(file_path, 'r', encoding='utf-8') as content_file:
                        f.write(f"\n📄 File: {file_path}\n")
                        f.write("-" * 40 + "\n")
                        f.write(content_file.read() + "\n")
                        f.write("-" * 40 + "\n")
                except UnicodeDecodeError:
                    try:
                        with open(file_path, 'r', encoding='latin-1') as content_file:
                            f.write(f"\n📄 File: {file_path}\n")
                            f.write("-" * 40 + "\n")
                            f.write(content_file.read() + "\n")
                            f.write("-" * 40 + "\n")
                    except Exception as e:
                        f.write(f"Could not read file {file_path}: {str(e)}\n")
                except Exception as e:
                    f.write(f"Could not read file {file_path}: {str(e)}\n")

        # Add GitHub link at the end
        f.write("\n" + "=" * 50 + "\n")
        f.write("🔗 Explore more projects: https://github.com/Jhad00\n")

    print(f"Report generated: {output_file}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python psm.py <directory_path>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    explore_directory(directory_path)

if __name__ == "__main__":
    main()
