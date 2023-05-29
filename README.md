# Digit span experiment
*** IMPORTANT NOTE: This is a project conducted for the purposes of a cognitive psychology class. I am not a psychologist, researcher or expert in conducting experiments.***

A short description about the project and/or client.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The things you need before running experiment.

* [OpenSesame](https://osdoc.cogsci.nl/), open sourced software for creating and running psychology experiments
* [JASP](https://jasp-stats.org/), open sourced software for running statistics
* [MindProbe account (registration on requeest only](https://mindprobe.eu/) 
* [Jatos](https://www.jatos.org) (MindProbe connects to Jatos, Jatos delivers a database)
* [Replit account](https://replit.com/) OR Python (optional)

## Experiment methodology
#### Participants
* Participants in the study will be people between the ages of 18 and 65 who do not have any memory disorders (under the age of 18 you need to have consent)
* The number of participants in the study should be at least 50 for the results to be accurate

#### Preparation of the test
- Prepare a list of digits/numbers that will be displayed on the test participant's screen
- Each set will consist of 12 numbers
- Each set will have a different length of digits
  - one digit
  - two digits
  - three digits


#### Preparation of participants
- Introduction to the study, using on-screen messages
- Instructing to prepare an adequate environment; removing possible distractors
- Asking them to fill out a simple metric
- Informing them of the estimated duration of the survey
- Asking participants not to write down the numbers displayed


#### Conducting the survey:
- Displaying each of the 3 prepared sets sequentially with 1.5 seconds to remember
- Displaying successively each of the 3 prepared sets with 4 seconds to memorize time
- After each set is displayed, there will be a short fifteen second pause
- Participants will be asked to memorize the displayed digits/numbers in the correct order

#### Analysis of the results
- Calculation of the correctness and similarity of the answers for each number (using levenshtein distance)
- The results will be statistically analyzed to determine the veracity of the hypotheses posed


## Hypothesis
- Numbers with fewer digits will be remembered more correctly than numbers with more digits.
- The average correctness of number memorization will be 70%, with a standard deviation of 20% in both directions.
<!-- The number display time (1.5 s or 4 s) will not have a significant effect on the correctness of number memorization.
 -->

## Usage

#### 1.0 Running experiment locally 
```
$ Download OpenSesame and import digitspan.osepx
$ Run the experiment pressing by "CTRL+R"
```

#### 1.1 Running experiment on web
```
$ Open OpenSesame and import digitspan.osepx 
$ open the 'Tools' and 'OSWeb'
$ 'Export experiment as a JATOS study'
$ Login to mindprobe account
$ import the study 
$ press on 'Properties' and enable 'Allow reload'
$ go to 'Study Links' and enable 'General Multiple'
$ copy the link for share
```

#### 2. Getting results
```
$ go to 'Study Results'
$ export results as 'Data only'
$ convert .json to .csv
$ combine multiple .csv into one
$ prepare the .csv for statistics
```

#### Statistics
```
$ Open JASP and import the .csv file
$ Follow the tutorial from provided link in Additional Documentation
```


## Additional Documentation

* [youtube: Creating a psychology experiment with OpenSesame 3.1](https://www.youtube.com/watch?v=FCXcnAv9aMA&t)
* [youtube: OpenSesame 3.1 tutorial: Cats, Dogs, and Capybaras](https://www.youtube.com/watch?v=ICa0vPoYrYw&t=)
* [youtube: One-Way Between Subjects ANOVA Using JASP](https://www.youtube.com/watch?v=2jY1eM6BKIw)

