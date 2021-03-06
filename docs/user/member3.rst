Parts Implemented by Altay İnci
================================
In this part information about seasons, standings and schedules pages will be given. Our project will be examined under two roles as user and admin. Admin can add, delete, update and search information in above pages. User can view and search these informations entered by admin.  

Seasons Page in User interface
------------------------------------
 
In this page, user can view seasons which are used by other pages. Our seasons are consist of two years like '2004-2005'. Other pages use these seasons for showing their various information or statistics belong to which years.

.. figure:: season-user.png 
      :scale: 50 %
      :alt: Seasons Page


- Searching 
User can search which year are used in our website with search button, and s/he can find if this year exists here, if not, 'No result found for selected criterias' message is shown. 

.. figure:: season-search.png 
      :scale: 50 %
      :alt: Searching
      
- After searching:

.. figure:: result-search-season.png 
      :scale: 50 %
      :alt: Result of searching

- Reset Filter
After user sees results of searching, clicking Reset Filter button, can return page includes all years.



Standings Page in User interface
-----------------------------------
- User interface
In this page, user can see leagues with their seasons and teams. Here aim is to show leagues include which teams in which seasons. Our standings consist of a season, a league name and a team name. Thus our user can examine seasons or teams which is followed by her/him according to leagues.
 
.. figure:: standing-user.png 
      :scale: 50 %
      :alt: Seasons Page

- Searching 
User can search league which teams played in it and in which season with search button. After this s/he can find lists of teams and seasons if this league exists here, if not, 'No result found for selected criterias' message is shown. 

.. figure:: standing-search.png 
      :scale: 50 %
      :alt: Standings Page

- After searching

.. figure:: result-search-standing.png 
      :scale: 50 %
      :alt: Result of searching
      
- Reset Filter
After user sees results of searching, clicking Reset Filter button, can return page includes all standings.


      
Schedules Page in User interface
----------------------------------
- User interface
In this page, user can see schedules of matches with their teams, seasons, league names, saloons, scores and playing states. Team1_name represents home team, team2_name represents away team. Our user takes match information of the team which is supported by her/him. In this way, if this match was not played(state=false), s/he can go this match. If not(state=true), user can only see score of matches. If the match is not played, scores are 0. 
 
.. figure:: schedule-user.png 
      :scale: 50 %
      :alt: Seasons Page

- Searching 
User can search home team with search button. If the searched team exists in database as a first team, s/he can find matches of the this supported home team, so user can access every information of matches. If the team is not found as first team, 'No result found for selected criterias' message is shown. 

.. figure:: schedule-search.png 
      :scale: 50 %
      :alt: Schedules Page

- After searching:

.. figure:: result-search-schedule.png 
      :scale: 50 %
      :alt: Result of searching

- Reset Filter
After user sees results of searching, clicking Reset Filter button, can return page includes all matches and their schedules.

Seasons Page in Admin interface
----------------------------------------
In this page, admin can achieve add, delete,update and search operations. Admin make these operations over *years* item of seasons.

- Add operation
For adding, **year** box in below must be filled and add button must be clicked.
  
.. figure:: add-season.png 
      :scale: 50 %
      :alt: Season Page
      
      After this,
      
.. figure:: add-result-season.png 
      :scale: 50 %
      :alt: Season Page
      

- Delete operation
For deletion, there are two ways. Firstly admin can click delete button near the item which is wanted to delete. However if a item is being used by other items in other pages, because of database organization, this item may not be deleted.
  
.. figure:: add-result-season.png 
      :scale: 50 %
      :alt: Season Page
      
      After deletion, 2009-2010 is deleted.
      
.. figure:: delete-season.png 
      :scale: 50 %
      :alt: Season Page
      
Secondly, admin can delete an item with checkbox near it.

.. figure:: delete-section.png 
      :scale: 50 %
      :alt: Season Page
      
      After this,
      
.. figure:: deleted-section.png 
      :scale: 50 %
      :alt: Season Page

- Update operation
For update, admin can click update button near the item will be updated. After this, update box exists below. New value is entered and this item is updated. 

.. figure:: update-season.png 
      :scale: 50 %
      :alt: Season Page
      
      After this,
      
.. figure:: updated-season.png 
      :scale: 50 %
      :alt: Season Page
      
- Search operation
For searching, admin enters the search key and clicks the search button. For example if 2002 is entered, result exists as in this image:

.. figure:: search-season-admin.png 
      :scale: 50 %
      :alt: Season Page

Standings Page in Admin interface
--------------------------------------
In this page, admin can achieve add, delete,update and search operations. Admin make these operations over *years*, *team names* and *league names* items of standings.

- Add operation
For adding, **year**, **league name** and **team name**  in selection boxes must be selected and add button must be clicked.
  
.. figure:: add-standing.png 
      :scale: 50 %
      :alt: standing Page
      
      After this,
      
.. figure:: add-result-standing.png 
      :scale: 50 %
      :alt: standing Page
      

- Delete operation
For deletion, there are two ways. Firstly admin can click delete button near the item which is wanted to delete. 
  
.. figure:: delete-standing.png 
      :scale: 50 %
      :alt: standing Page
      
      After deletion, item which is in the most below is deleted.
      
.. figure:: deleted-standing.png 
      :scale: 50 %
      :alt: standing Page
      
Secondly, admin can delete an item with checkbox near it.

.. figure:: delete-standing-section.png 
      :scale: 50 %
      :alt: standing Page
      
      After this,
      
.. figure:: deleted-section-standing.png 
      :scale: 50 %
      :alt: Season Page

- Update operation
For update, admin can click update button near the item will be updated. After this, update box exists below. New value is entered and this item is updated. 

.. figure:: update-standing.png 
      :scale: 50 %
      :alt: Season Page
      

      
- Search operation
For searching, admin enters the league name and clicks the search button. For example if Turkish is entered, result exists as in this image:

.. figure:: standing-search-admin.png 
      :scale: 50 %
      :alt: standing Page


      
Schedules Page in Admin interface
--------------------------------------
In this page, admin can achieve add, delete,update and search operations. Admin make these operations over *team_1*, *team_2*, *season*, *league name*, *date*, *saloon*, *scores* and *state* items of standings.

- Add operation
For adding, **team_1**, **team_2** , **year** and **league name** in selection boxes must be selected and after this, **date**, **saloon**, **score1**, **score2** and **state** must be filled. At the following, admin must click add button.
  
.. figure:: add-schedule.png 
      :scale: 50 %
      :alt: schedule Page
      
      After this,
      
.. figure:: add-schedule-result.png 
      :scale: 50 %
      :alt: schedule Page
      

- Delete operation
For deletion, there are two ways. Firstly admin can click delete button near the item which is wanted to delete. 
  
.. figure:: delete-schedule.png 
      :scale: 50 %
      :alt: schedule Page
      
      After deletion, item which is in the most below is deleted.
      
.. figure:: deleted-schedule.png 
      :scale: 50 %
      :alt: schedule Page
      
Secondly, admin can delete an item with checkbox near it.

.. figure:: delete-schedule-section.png 
      :scale: 50 %
      :alt: schedule Page
      
      After this,
      
.. figure:: deleted-schedule-section.png 
      :scale: 50 %
      :alt: schedule Page

- Update operation
For update, admin can click update button near the item will be updated. After this, update box exists below. New values are entered and this item is updated. 

.. figure:: update-schedule.png 
      :scale: 50 %
      :alt: schedule Page
      

      
- Search operation
For searching, admin enters the home team (team_1) name and clicks the search button. For example if 'SAN ANTONIO' is entered, result exists as in this image:

.. figure:: schedule-search-admin.png 
      :scale: 50 %
      :alt: schedule Page


