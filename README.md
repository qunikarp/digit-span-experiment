# Digit span experiment

A short description about the project and/or client.

NOTE: I'm not an expert and shown way is just how I tried 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The things you need before running experiment.

* [OpenSesame](https://osdoc.cogsci.nl/), open sourced software for creating and running psychology experiments
* [JASP](https://jasp-stats.org/), open sourced software for running statistics
* [MindProbe account (registration on requeest only](https://mindprobe.eu/) 
* [Jatos](https://www.jatos.org) (MindProbe connects to Jatos, Jatos delivers a database)
* [Replit account](https://replit.com/) OR Python (optional)


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

