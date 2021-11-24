# ENA CRAM Archive Client Docs

The ENA CRAM Archive Client is designed for easy retrieval of reference sequences and their metadata.

## Features

- retrieve reference sequence
- retrieve reference sequence metadata in json format
- retrieve service info in json format

## Installation

```bash
pip install git+https://github.com/alextsaihi/enaCRAM.git
```

## Example

In a case where you would like to print out the metadata
```bash
from enaCRAM import enaCRAM

sequenceID = "3050107579885e1608e6fe50fae3f8d0"
cram = enaCRAM()
print(cram.get_metadata(sequenceID))
```
