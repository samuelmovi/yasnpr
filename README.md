# YASNPR: Yet Another SecurityNow! Podcast Retriever
Being a fan of SecurityNow! I wanted to create a tool for archiving all its contents.
For each downloaded podcast, it downloads the hi-q and lo-q MP3s, the show's notes, and the transcripts, then places it in an appropiately named folder.

## Requirements
- Python 3.5+
- Requests 2.22.0

## Installation
Clone the repository to your chosen destination

```bash
 git clone git@github.com:samuelmovi/yasnpr.git
 ```

## Usage
The program offers 2 download options:

- Full podcast copy: it will ask for last podcast's number, and will download from 1 to that.
- Single podcast copy: input any valid podcast number and it downloads its contents.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GPLv2](https://choosealicense.com/licenses/gpl-2.0/)
