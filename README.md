# PersonalSchedulerUbicomp2019
This repository holds all materials associated with the Personal Scheduling Assistant (PSA) Project for CS284A (Ubiquitous Computing), Winter 2019, UCI
Authors: John English & Daniel Ruiz

## Instructions
In order to run the PSA prototype, simply run:

```
python PSA_main.py in your console.
```

Note that Event.py and Schedule.py are required for the correct execution of the main PSA script.

## Details
This script runs the prototype in demonstration mode, which initializes an internally tracked schedule to contain two static events (Work & Dinner with Parents).

You will then receive a welcome message, and immediately be prompted for the name and duration of an event. Please note that our prototype operates on half-hour increments. Therefore, you must account for this when prompted for event duration. Below are some examples of correct input:
* 2 hour event -> enter 4
* 1.5 hour event -> enter 3
* 5 hour event -> enter 10

After providing the required input, the prototype will simulate interaction with various APIs, in order to acquire information on external
factors that could influence its scheduling recommendation (i.e. weather, estimated driving time, estimated wait time, etc). Each time the prototype is run, these factors are randomized so the results will always vary. PSA will collectively refer to these simulated external factors as "external disruption", and rank the results between 0 and 2.

Next, based on the external disruptions for each available time slot, PSA will find the optimal place for the new event on the schedule, and make a recommendation to the user. In the event no optimal spot is found, PSA will let the user know that scheduling an event on this day is not recommended. Shortening the duration of the event makes this scenario less likely. Lastly, PSA will display a representation of the internal schedule and corresponding external disruptions for visualization purposes.

Please refer to the included report for more information.
