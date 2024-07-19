# SpecLib-Split

Split mixed ion mass spec spectral Library into Positive and Negative subsets like ALL_GNPS.

## Overview

Locally searching Metabolomics data in MSDIAL or Mzmine using the ALL_GNPS comprehensive library may give false hits due to the wrong ion mode. SpecLib-Split can split the .msp library with compounds from mixed ion mode into POS and NEG subsets.

## Usage

Just load the Python script and change the directory of the input files as needed.

### Requirements

- Python 3.x
- pandas

### Installation

Install the required Python packages:
```bash
pip install pandas
