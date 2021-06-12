# techdegree-project-2

The Basketball team creator tool.

I went for all the exceeds expectation parts and wanted to put as much as I can into different functions that all try to do one thing.

For some extras I wanted the interface to load the team names from the constant and to make it show the different teams by loading this. I thought this would be more scalable towards the future where the team names might change. I looked up how to make the index into a capital letter instead of a number so it would look good right away in the team menu.

Some UX things I added. In the team picker it allows both a/b/c or team name. I reckoned when you ask a user which team they want to have more input in they're more likely to type the full name.

Sadly in the empty list variables, the balance team and the team selection function I still hardcoded the team-names. In a future iteration I would remove this. Making empty lists team_one would avoid the necessity for the team name but would still require adding/removing teams every year depending on how many get into the selection. I think the best fix would be one empty team list that I would fill on demand when the user requests the team but this added a lot of complexity in my head that I didn't manage to write out properly yet
