# ENA CRAM Archive Client Docs

The ENA CRAM Archive Client is designed for easy retrieval of reference sequences and their metadata.

## Features

- *get_metadata(self, sid)* retrieve reference sequence 
- *get_sequence(self, sid)* retrieve reference sequence metadata in json format 
- *get_service_info()* retrieve service info in json format 

## Installation

```bash
pip install git+https://github.com/alextsaihi/enaCRAM.git
```

## Example

In a case where you would like to print out the metadata, use *get_metadata* function
```bash
from client import enaCRAM

sequenceID = "3050107579885e1608e6fe50fae3f8d0"
cram = enaCRAM()
print(cram.get_metadata(sequenceID))
```
