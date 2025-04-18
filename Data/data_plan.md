In this file, you will find the structure that I followed to create the data I'm going to use in order to train my model.

First things first, I asked myself the basic question: "What am I going to predict? What's the output?"  
The answer to that question was obvious: the quality of sleep of a user based on the data from their phone.  
This answer was not precise enough, so it led me to ask myself a second question: what is the type of that output?  
A score out of 10? Which means I'm going to use regression, because the variable is continuous.  
Or a binary output: 0 for poor quality and 1 for excellent quality?  
I wasn't convinced by the second option, because it doesn't really help users understand how good or bad their sleep was.  
That’s what led me to choose the first option: a score out of 10.

Secondly, I wanted to know the input that would help me predict the score.  
We often refer to that "input" as **features**.  
I initially made a list of 10 features that could help train the model, but I sorted them by importance and selected the 5 most relevant:

i)  Screen time – how much time is spent using the phone?  
ii) Duration of sleep  
iii) Time of going to bed  
iv) Is the person using dark mode?  
v)  Type of apps used – (A person scrolling on Instagram for 7 hours is not the same as someone watching a 7-hour video on YouTube.  
There are plenty of external factors, such as dopamine hits, when you're scrolling through short-format videos.)

Talking about external factors that can affect the score, I asked myself other questions:  
"Can a person use their phone in moderation and still have trouble sleeping?"  
"What if they don’t use their phone but use their computer instead?"  
"What if they scroll endlessly and still get good sleep?"  
In this case, the score would be low, which could cause bias.  

The answer was yes: several factors can affect sleep quality.  
So how can I reduce this bias?  
Well, I will add **random noise** to simulate more realistic results.

Once I defined the features, the next step was to outline how to get the data:

i) Manually – each night, add the features to a table using Pandas, Excel, or another tool  
ii) Using tracking apps – such as Health (iOS) or Sleep Cycle (Android), I could automatically export features into a CSV or JSON file  
iii) A Python script – that automatically generates realistic features

I'm going to follow the last option (iii), as it's the simplest way to begin.  
Later, during the deployment phase, I plan to use smartphone data directly to make a logical prediction for the user who wants to know the quality of their sleep.

For the dataset structure, I plan to use a public one from **Kaggle**.  
The features will be saved in a CSV file.  
(I also thought about using a database like SQLite or PostgreSQL later on.)

Once all of that is done, I’ll have to verify whether the script generates realistic data by creating a **comparison graph** using real-world resources.

