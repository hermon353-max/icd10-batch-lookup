# ICD-10 Batch Lookup

A Python tool that turns a list of plain-English diagnoses into ICD-10-CM codes, and flags codes that aren't billable.

## Why I built this

Looking up one ICD-10 code is easy. Google can do it. But coders and health information staff often work from a whole problem list, and a common, costly mistake is submitting a **non-billable header code** (for example, `E11` instead of a complete code like `E11.9`). Claims with non-billable codes get denied.

This tool takes a full list at once, returns matching codes, and (in progress) flags any code that can't be billed.

I'm a Health Informatics & Health Information Management student at the University of Washington, and this project connects my medical coding coursework to Python.

## How it works

1. You enter a diagnosis, like `asthma`.
2. The program sends it to the [NLM Clinical Tables ICD-10-CM API](https://clinicaltables.nlm.nih.gov/apidoc/icd10cm/v3/doc.html), a free public API from the National Library of Medicine.
3. The API returns matching codes and descriptions, and the program prints them:

```
J45.998 Other asthma
J82.83 Eosinophilic asthma
J45.909 Unspecified asthma, uncomplicated
J45.991 Cough variant asthma
J45.20 Mild intermittent asthma, uncomplicated
```

No patient data is used or stored.

## Status

- [x] Call the NLM API and get results for one diagnosis
- [x] Parse the response and print codes with descriptions
- [ ] Turn the lookup into a reusable function
- [ ] Batch mode: process a whole list of diagnoses at once
- [ ] Flag non-billable (header) codes
- [ ] Export results to CSV
- [ ] Simple web page with Streamlit
- [ ] Suggest more specific codes when a match is too general

## Run it

Requires Python 3.

```
py -m pip install requests
py icd10-batch-lookup.py
```

## Built with

- Python
- `requests` library
- NLM Clinical Tables API
