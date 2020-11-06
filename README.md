# flag-on-the-play

![header_image](images/header1.jpg)

## Desciption

This repo is home to a project I embarked on for two purposes; firstly to utilize a dataset I had put together from several publicly available sources for analyzing questions relating to NFL penalties and whether or not a given team (in my case the Seattle Seahawks for purely personal reasons) is being unfairly targeted by the officiating team for penalties. The second purpose for this project is essentially to gain extra practice with my AWS skillset by the instantiation of a SQL Server database with AWS' RDS which I then utilized to conduct the bulk of the analysis used for addressing the fundamental question behind this project. I was then able to provide this database along with the questions that I was interested in answering with it as a platform to host a bi-monthly sql practice night organized by fellow data scientist Isaac Campbell-Smith. For those interested, his primary repository for the SQL practice nights can be found [here](https://github.com/isaac-campbell-smith/Pokestars). The practice workbook for that event can be found within this repo although for security reasons the login credentials for the database instance have been removed. If anyone is interested in utilizing this workbook for practicing their sql skills, please feel free to contact me, and access can be arranged. 


## The Problem 

As an NFL fan, (and a fan of the Seattle Seahawks in particular) I occasionally find myself watching football with my dad, and whenever I do, the accusation inevitably creeps in that the referees are biased in the way that they make penalty calls – specifically that for a given illegal action, a penalty will be called against the Seahawks for a higher percentage of the instances of the illegal action than the opposing team. Personally, I’m not good enough at spotting penalties to know, and to be honest, my suspicion is that this feeling of one’s own team being unfairly persecuted is one harbored by most sports fans regardless of the team they root for. It occurs to me though, that as a data scientist, this sports fan is uniquely qualified to actually grab some data and attempt to vet this theory as it applies to my own team.  

## Methodology

The heart of this accusation has to do with penalties that are not called, for which there is no record, which makes this claim very hard to definitively confirm or refute. However, data on called penalties *is* published and publicly available, and through thoughtful analysis of what *was* called, we can at least see if there is evidence of a bias towards calling penalties against certain teams more often than others. 

The first thing to do is to compare the number of penalties that each team accrues across the league. However, even seeing that the Seahawks rank relatively high on the list of most penalized teams at number five is not evidence to say that these high penalty numbers are unwarranted. The tricky thing to find here is evidence that the Seahawks high penalties numbers are due to some sort of bias rather than the alternate explanation that the team simply has a play or coaching style that is inherently less careful about adhering to the rules. So how does one find evidence that these penalties are not fairly called on account of a more careless play style of the team? 

The answer is to look not at the team as a whole, but to look at the players individually; specifically players who have a record of penalties when playing for other teams as well as for Seattle. If examination of the numbers points to a trend of the same players receiving less penalties when playing on another team then when playing on Seattle, this could be strong evidence that there is something to this theory. As with any statistical hypothesis testing, the presence of such a trend would not be proof of such a bias, but it would be evidence that there is reason to look into the issue further. 




## DataBase Schema

guest.teams table

|id 			   | Description                                | Type      |
|------------------|:-------------------------------------------|:----------|
| year      	   | Year of football season                    | INT       |
| team_city 	   | City where team is located                 | VARCHAR   |
| team_id   	   | id number unique to team                   | INT       |
| coach_name       | Name of team coach                         | VARCHAR   |
| coach_id         | id number unique to coach                  | INT       |
| ranking          | Rank of most to least penalized            | INT       |
| games     	   | Games played that season                   | INT       |
| plays            | Number of plays that season                | INT       |
| against_count    | Number of flags against team               | INT       |
| agnst_yrds       | Total yards penalized in season            | INT       |
| ben_count        | Number of flags on opposing team           | INT       |
| ben_yrds     	   | Yards given for opposing flags             | INT       |
| net_count        | Team flags less opposing flags	            | INT       |
| net_yrds         | Yards lost plus yards gained from penalties| INT       |
| total_flags      | Total flags thrown in team's games         | INT       |


guest.players table

|id 	        | Description                                | Type      |
|---------------|:-------------------------------------------|:----------|
| year      	| Year of football season                    | INT       |
| player_name 	| Name of player                             | VARCHAR   |
| player_id   	| id number unique to player                 | INT       |
| position      | Abreviation for player's position          | VARCHAR   |
| team          | City where team is located                 | VARCHAR   |
| team_id       | id number unique to team                   | INT       |
| pen_count     | Number of inforced penalties against player| INT       |
| yards         | Yards lost due to flags on player          | INT       |
| n_flags       | All player penalties, includes declined    | INT       |
| pre_snap      | Flags by player prior to start of play     | INT       |
| per_game      | Number of times penalized per game         | INT       |
| yards_game    | Yards lost from penalites per game         | INT       |
| of_team       | Percentage of teams penalties from player  | INT       |
