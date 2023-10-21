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
The project has the bonus goal of having an objective, modify data according to that objective and have a written analysis with the final conclusion of our investigation.

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
- `Investigator_or_source`: where the data is comming from.
- `PDF`: pdf name ref of the attack.
- `href formulas`: online pdf of the attack.
- `href`: online pdf of the attack.
- `case number 1`: duplicate of case number column.
- `case number 2`: duplicate of case number column.
- `original order`: order in which the attacks were registered.
- `unnamed 22` & `unnamed 23`: nan columns.

Some of the columns are poorly written (for example, there is an space after the "Sex " column name) and have some inconsistencies on their name, so normalization of the column names is going to be a priority.

Also, I'm going to rearrange the columns so their order makes more sense to me, as well as filling duplicated columns with 0 (since dropping them is forbidden).

## 2.2. Cleaning nan values
General cleaning of nan and null values.

## 2.3. Checking for incorrect values
When reading the data I saw some values that were weird, such as some weird values in sex (which should be M or F (or unknown)), some inconsistencies in the case number, etc.

- 1) I focused on the 'binary' columns: `sex` and `fatal`.
- 2) `case_number` used to have a pattern that got lost somehow, so I'm going to fix that using the `pdf` column.
- 3) Fix incorrect dtypes in `year` and `original order`.
- 4) Normalizing data on `activity` column.
- 5) Normalizing data on `species` column.
- 6) Normalizing `time` column.

# 3. Investigation

## 3.1. Procedure

My objective is to see how each species of shark like their food: swimming, surfing, diving... and to see when do they prefer to eat, categorizing them between early bird eater, afternoon yummys guy, evening diner guy and late snacker.

- 1. Make a slice of the dataframe with the columns needed.
- 2. Make a dataframe using groupby with the mode of the prefered food.
- 3. Make another one but with the prefered time of the day.
- 4. Adding a column to the last one with the kind of snacker.
- 5. Merge the two together.
- 6. Import it as csv.

Finally, I'm going to create a little computer program to access to the information and adding new if wanted.

## 3.2. Conclussions

Sharks are very funny guys and they like their food when they are fishing, literally hunter being hunted! Instant karma! Also, the majority are afternoon yummy guys, meaning that they prefer to eat after working hours, isn't that relatable? They are just like us.

# 4. Program Use
When initialized, it will ask for a shark species and search for it in the database. If the species doesn't exist in the database, it will ask if you want to add that species to the database and then be prompted to add its prefered food and when does it like to eat. The csv will be overwritted with the data inputted there.