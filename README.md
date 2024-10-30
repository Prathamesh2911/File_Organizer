# File Organizer Script

A Python script that organizes files in the current directory into subdirectories based on their file types: Images, Documents, Media, and Others. The script utilizes the `tqdm` library to display a progress bar during file movement.

## Features

- Automatically categorizes files into designated folders:
  - **Images**: `.png`, `.jpg`, `.jpeg`
  - **Documents**: `.txt`, `.docx`, `.doc`, `.pdf`
  - **Media**: `.mp4`, `.mp3`, `.flv`
  - **Others**: Any other file types
- Provides a visual progress bar for file moving operations.
- Outputs a summary of files moved after completion.

## Prerequisites

- Python 3.x
- `tqdm` library

To install the `tqdm` library, run:
```bash
pip install tqdm
