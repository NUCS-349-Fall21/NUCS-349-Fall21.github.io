<a name="top"></a>
# Northwestern University CS349: Machine Learning, Fall 2021
 
|[**Top**](#top) | [**Policies**](#policies) |  [**Calendar**](#calendar) | [**Materials**](#materials) | [**Contributors**](#contributors) |

## Course Description
Machine learning is the study of algorithms that improve automatically through experience. This is an overview class that covers the fundamentals: classification, regression, and model training and evaluation across a variety of approaches, both old and new.

### Prerequisites
For this course, it is extremely helpful to be familiar with probability, statistics, python programming and matrix math. We expect students to come prepared with those skills. Here are some [prerequisite materials](prerequisites.md) to get up to speed, in case you need a refresher.

### Class Meeting Time & Place 
Section 1: Mon Wed 9:30AM - 10:50AM Frances Searle Building 2107  
Section 2: Tue Thu 8:00AM - 9:20AM  Harris Hall 107   
Videos lectures will be available on Canvas.

### Office Hours

#### Instructors
[Bryan Pardo](https://bryan-pardo.github.io): Tue Thu 9:40am - 11:00am via Zoom.   
Go [here](https://bryan-pardo-office-hours.youcanbook.me/) to book a 10 minute meeting. 

[Zach Wood-Doughty](https://zachwd.com): Mon Fri 1:30-3pm via [Zoom](https://northwestern.zoom.us/my/zachwd)

#### Teaching Assistants
[Hugo Flores Garcia](https://hugofloresgarcia.github.io): Tue Thu @ 5-6pm via [Zoom](https://northwestern.zoom.us/j/96030754244)

[Patrick O'Reilly](https://interactiveaudiolab.github.io/people-current/7_patrick-oreilly.html): Sat 2-4pm via [Zoom](https://northwestern.zoom.us/j/5823751606)

#### Peer Mentors
Alex Tai: Sun 9-11am in Tech EG20

Boaz Cogan: Mon Wed 8-9am in Tech EG20

Noah Schaffer: Fri 9-11am in Tech EG20

Aldo Aguilar: Mon Wed 5-6pm via [Zoom](https://northwestern.zoom.us/j/8681365936?pwd=eVJKOXFnM1hCdElYT0hTVzJOcGE3QT09)

Garphy Tam: Tue Wed 3-4pm via [Zoom](https://northwestern.zoom.us/j/9873082823)

Simran Gadkari: Tue Fri 12-1pm via [Zoom](https://northwestern.zoom.us/j/99055111724)

Utkarsh Mishra: Wed Thu 6-7pm Mishra via [Zoom](https://northwestern.zoom.us/j/2677857534)

<a name="policies"></a>
## Policies 
* *Grading:* There are 6 assignments, each worth 20 points. We will calculate your grade as follows: Throw out the lowest grade, average the other 5 and scale to the range 0-100. You're graded on a basis of 100 points. 93-100 is an A, 90 - 92 is an A-, 87-89 is a B+, 83-86 is a B, 80-82 is a B-...and so on. There is no curve. 

* *Extra Credit:* The first assignment is extra-credit, extremely easy and worth 20% of the total points. **No special additional extra credit will be given**. Remember, we're also dropping your lowest-graded assignment. Practically speaking, this means you can entirely skip any one assignment and still get 100 out of 100. This can be helpful if you are ill at some point or have other commitments.  

* *When and Where to Submit Assignments:*  Free responses are due on [Canvas](http://www.it.northwestern.edu/education/login.html) 
by 11:59pm on the due date.  Code is due in your individual GitHub Classroom code repository, also at 11:59pm on the due date. 

* *Late Policy:*  If there is nothing on Canvas by 11:59pm on the due date, the free response grade is 0. If there is nothing in your github repository by 11:59pm on the due date, the coding grade is 0. The most recent code on github at 11:59pm on the due date is the code we will grade. The most recent submission in Canvas at that point, is the one we grade. A good approach is to continually check in and push to GitHub as you work. Also, put up a "safety" submission on Canvas with what you currently have, an hour prior to the deadline. 

* *Cheating & Academic Dishonesty:* Do your own work. This includes free response answers and code. Penalties include failing the class and can be more severe than that. If you have a question about whether something may be considered cheating, ask, prior to submitting your work. We will be checking for code duplication. Academic dishonesty will be dealt with as laid out in [the student handbook](https://www.northwestern.edu/communitystandards/student-handbook/). We will be using [MOSS](https://theory.stanford.edu/~aiken/moss/) for checking on academic dishonesty.

* *Attendance* is not graded. You are not required to attend. Videos of the Tuesday/Thursday lectures will be made available on Canvas. 

* *COVID 19 and Health:* Videos will be available for all course lecture content. If you have tested postive for COVID19 do not come to class. If you feel ill, do not come to class. Watch the video of the lecture instead. **If anyone is seen in class without a mask covering their mouth and nose, class will be halted until that person either leaves or puts on a mask.** 

* *Announcements* and discussions will take place on [CampusWire](https://campuswire.com/p/GBC330FBB). You can sign up for the page at that link using the sign-up code 5975.

<a name="calendar"></a>
## Course Calendar

This is a prediction of what will be covered in each week but the schedule is subject to change as the course progresses.

| Week  | Due    | Topic (click on topic for slides)    | Lecturer     |        
|-------|--------|--------------------------------------|--------------|
| 09/20 |        | No class                             |    
|       |        | [Intro to ML](lectures/cs349_intro_to_ml.pdf)                          | Pardo        |     
| 09/27 | HW 0   | [P-norms and Distance Measures](lectures/cs349_measuring_distance.pdf)        | Pardo        | 
|       |        | [Nearest Neighbor Classifiers](lectures/cs349_nearest_neighbor.pdf)         | Pardo        |    
| 10/04 |        | Linear and Polynomial Regression     | Wood-Doughty |
|       |        | Linear Discriminants                 | Wood-Doughty |
| 10/11 | HW 1   | Decision trees                       | Pardo        | 
|       |        | Boosting & Statistical Tests         | Pardo        |    
| 10/18 |        | Support vector machines + Kernels    | Pardo        | 
|       |        | Multilayer Perceptrons and Backprop  | Pardo        |  
| 10/25 | HW 2   | Convolutional Networks               | Pardo        | 
|       |        | More Deep Learning                   | Pardo        |  
| 11/01 |        | Expectation Maximization             | Wood-Doughty | 
|       |        | Gaussian Mixture Models              | Wood-Doughty |   
| 11/08 | HW 3   | Graphical Models                     | Wood-Doughty | 
|       |        | Graphical Models                     | Wood-Doughty |  
| 11/15 |        | Hidden Markov Models                 | Wood-Doughty | 
|       |        | Hidden Markov Models                 | Wood-Doughty |   
| 11/22 | HW 4   | Reinforcement Learning               | Pardo        |
|       |        | *NO CLASS: THANKSGIVING*             |   
| 11/29 |        | Fairness, accountability and Ethics  | Wood-Doughty |   
|       |        | Current research topics in ML        | Wood-Doughty | 
| 12/06 | HW 5   | *NO CLASS: Finals week*              | 


<a name="materials"></a> 
## Materials
### Helpful Reading 

#### 09/27 
* [Elements of Statistical Learning, Sections 2.1 - 2.3](https://web.stanford.edu/~hastie/Papers/ESLII.pdf)
* [Recommender Systems, Sections 2.1 - 2.3](readings/Recommender_Systems_An_Introduction_Chpt2.pdf)
* [The Wikipedia page on metrics](https://en.wikipedia.org/wiki/Metric_(mathematics))

#### 10/04
* [Elements of Statistical Learning, Sections 3.1 - 3.3](https://web.stanford.edu/~hastie/Papers/ESLII.pdf)
* ...

#### 10/11
* [Machine Learning Chapter 3: Decision Trees](readings/mitchell-ch3-dtrees.pdf)
* [An Introduction to Boosting](readings/intro_to_boosting.pdf)
* [Machine Learning Chapter 5: Evaluating Hypotheses](readings/mitchell-ch5-eval.pdf)
* [Elements of Statistical Learning, Chapter 7](https://web.stanford.edu/~hastie/Papers/ESLII.pdf)


### Lectures Slides
The lecture slides will be made available on the course calendar above, as the course progresses.

### Lecture Videos
Videos of the Tuesday/Thursday lectures will be made available on Canvas (via Panopto) on the same day they are recorded. 

### Additional Links 

1. [CS229 at Stanford](http://cs229.stanford.edu/syllabus-summer2020.html)
2. [Beautiful Cheetsheet on supervised Machine Learning](https://stanford.edu/~shervine/teaching/cs-229/cheatsheet-supervised-learning)
3. [Lecture Notes by Miguel A. Carreira-Perpinan](https://faculty.ucmerced.edu/mcarreira-perpinan/teaching/CSE176/lecturenotes.pdf)
4. [Well curated course notes (and slides) by Sebastian Raschka](https://sebastianraschka.com/pdf/lecture-notes/stat479fs18/). [Go here for the intro pdf](https://sebastianraschka.com/pdf/lecture-notes/stat479fs18/01_ml-overview_notes.pdf)
5. [Andrew Ng - Lecture Notes](https://sgfin.github.io/files/notes/CS229_Lecture_Notes.pdf) and [from someone that wrote alternate notes based on these lectures](http://www.holehouse.org/mlclass/)

<a name="contributors"></a> 
### Contributors
People who contributed to the design of this course and the homeworks:

Bryan Pardo, Prem Seetharaman, Bongjun Kim, Max Morrison, Ethan Manilow, Fatemeh Pishdadian, Lukas Justen, Oliver Coissart, Florian Schiffers, Sushobhan Ghosh, Ze Zhu

|[**Top**](#top) | [**Policies**](#policies) |  [**Calendar**](#calendar) | [**Materials**](#materials) | [**Contributors**](#contributors) |


