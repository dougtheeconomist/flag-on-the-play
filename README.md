# flag-on-the-play

![header_image](images/header1.jpg)

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
