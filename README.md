# Exercise Badges

![](https://byob.yarr.is/apudasm10/made-template-fau/score_ex1) ![](https://byob.yarr.is/apudasm10/made-template-fau/score_ex2) ![](https://byob.yarr.is/apudasm10/made-template-fau/score_ex3) ![](https://byob.yarr.is/apudasm10/made-template-fau/score_ex4) ![](https://byob.yarr.is/apudasm10/made-template-fau/score_ex5)

# Climate Impact on Urban Mobility: Analyzing Bike-Sharing Demand

Urban bike-sharing systems have emerged as a popular and eco-friendly mode of transportation in many cities, significantly mitigating climate change by reducing dependency on fossil fuels and lowering carbon emissions. The Capital Bikeshare and Seoul Bike Sharing systems are perfect examples of this trend. Understanding the factors that impact bike share rentals is crucial for optimizing efficiency and ensuring rider demand. This study analyzes the factors influencing bike share rentals using data from two different datasets from two countries. By exploring the impact of weather (temperature, humidity, and wind speed), we will try to find trends and patterns in bike rental demand. Thus, this analysis will provide valuable and practical insights into the question, "How does climate change (temperature, humidity, and wind speed) affect bike rentals?". It will also ensure sufficient bike availability and contribute to the fight against climate change by promoting sustainable transportation alternatives.

## Question

How does climate change (temperature, humidity, and wind speed) affect bike rentals?

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Bike Sharing

* Metadata URL: <https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset>

* Data URL: <https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip>

* Data Type: Zip -> CSV

The dataset provides hourly and daily rental bike counts from 2011 to 2012, along with corresponding weather and seasonal data.  It can be used to analyze factors influencing Capital bikeshare rentals.

### Datasource2: Seoul Bike Sharing Demand

* Metadata URL: <https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand>

* Data URL: <https://archive.ics.uci.edu/static/public/560/seoul+bike+sharing+demand.zip>

* Data Type: Zip -> CSV

The dataset provides hourly rental bike counts in Seoul from 2017 to 2018, along with corresponding weather data and holiday information.  It can be used to analyze factors influencing Seoul Bike Sharing System.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Dataset selection
2. Building an Automated Data Pipelines
3. Automated Testing
4. Continuous Integration
5. Feature Engineering and Analysis
6. Reporting on findings
7. Presentation


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

___
___
___


This template project provides some structure for your open data project in the MADE module at FAU.
This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.
Before you begin, make sure you have [Python](https://www.python.org/) and [Jayvee](https://github.com/jvalue/jayvee) installed. We will work with [Jupyter notebooks](https://jupyter.org/). The easiest way to do so is to set up [VSCode](https://code.visualstudio.com/) with the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).

To get started, please follow these steps:
1. Create your own fork of this repository. Feel free to rename the repository right after creation, before you let the teaching instructors know your repository URL. **Do not rename the repository during the semester**.
2. Setup the exercise feedback by changing the exercise badge sources in the `README.md` file following the patter `![](https://byob.yarr.is/<github-user-name>/<github-repo>/score_ex<exercise-number>)`. 
For example, if your user is _myuser_ and your repo is _myrepo_, then update the badge for _exercise 1_ to `![](https://byob.yarr.is/myrepo/myuser/score_ex1)`. Proceed with the remaining badges accordingly.


## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to html: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervalls, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv`
2. `./exercises/exercise2.jv`
3. `./exercises/exercise3.jv`
4. `./exercises/exercise4.jv`
5. `./exercises/exercise5.jv`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
