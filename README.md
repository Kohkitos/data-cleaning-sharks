![cover](https://github.com/Kohkitos/data-cleaning-sharks/blob/main/img/shark2.jpg)

# Data Cleaning Project
Iron Hack's second week Data Cleaning project with Pandas using a data set about Shark Attacks globaly.

This `README.md` will work as kind of a blog of my procedure during the project. Any insights will be inside the `sharks.ipynb`.

# 1. Project Description
## The Goal
The goal of the project is to clean the messy data set using the knowledge acquired during the bootcamp's week 2.

## Project Restrictions
- None of the columns can be removed, only modified.
- There should be ***at least*** 2.500 rows.

## Bonus goal
The project has the bonus goal of having an objective, modify data according to that objective and have a written analysis with the final conclusion of our study.

# 2. Procedure
## 2.1. Exploration
First, I tried to understand the dataframe and make sense out of every column before stablishing an objective.
- `Case Number`: it started with a real case number, but most recent data are just dates (yyyy.mm.dd).
- `Date`: the date. Some of them are on a range (eg. 1845-1853), others a relative date (eg. Before 1903) and specic dates (dd-mnth-yyyy).
- `Year`: the year. Some are the precise year, but in ranges or relatives date is a 0.0.
- `Type`: how it happened.
- `Country`: which country.
- `Area`: on which area of the country.
- `Location`: on which location of the country.
- `Activity`: what was the victim doing.
- `Name`: name of the victim.
- `Sex`: sex of the victim [M/F].
- `Age`: age of the victim.
- `Injury`: injury of the vitim.
- `Fatal`: was it fatal [Y/N].
- `Time`: time of the attack.
- `Species`: species of the shark.
- `Investigator`: who investigated the case.
- `PDF`: pdf name ref of the attack.
- `href formulas`: online pdf of the attack.
- `href`: online pdf of the attack.
- `case number 1`:
- `case number 2`:
- `original order`: order in which the attacks were registered.
- `unnamed 22` & `unnamed 23`: nan columns.

Some of the columns are poorly written (for example, there is an space after the "Sex " column name) and have some inconsistencies on their name, so normalization of the column names is going to be a priority.

## 2.2. Cleaning nan values
General cleaning of nan and null values.

## 2.3. Checking for incorrect values
When reading the data I saw some values that were weird, such as some weird values in sex (which should be M or F (or unknown)), some inconsistencies in the case number, etc.

- 1) I focused on the 'binary' columns: `sex` and `fatal`.
- 2) `case_number` used to have a pattern that got lost somehow, so I'm going to fix that using the `pdf` column.
- 3) `species` column is specially messy, and it needs really important care.
- 4) The same as `species` goes with `activity`.

### 3. Objective
My objective is to see how each species of shark like their food: swimming, surfing, diving... so I'm going to take a slice of the dataframe taking the data I need for this important ivestigation.